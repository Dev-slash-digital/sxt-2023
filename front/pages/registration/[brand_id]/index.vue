<template>
    <StickyHeader v-if="!state.isLoading" class="register-header" :with-registration-button="true" ref="header" />
    <div v-if="!state.isLoading" class="landing-container-2">
        <RegistrationTreeStreetMap :brand-logo="state.brandLogo" :brand-id="state.brandId"
            :brand-slug="state.brand.slug" />
        <ContestInformation />
        <Donations />
        <SmallTree></SmallTree>
        <BrandCarousel />
    </div>
    <div v-if="state.isLoading" class="loader-container">
        <div class="loading-dual-ring"></div>
    </div>
    <RegistrationFooter v-if="!state.isLoading" class="sxt-container-registration--footer" />
</template>

<script setup>
import RegistrationTreeStreetMap from "@/components/RegistrationTreeStreetMap.vue";
import ContestInformation from "@/components/ContestInformation.vue";
import Donations from "@/components/generic/Donations.vue";
import BrandCarousel from "@/components/generic/BrandCarousel.vue";
import SmallTree from "@/components/generic/SmallTree.vue";
import { reactive, onBeforeMount } from "vue";
import API from "@/utils/axios";

// head
useHead({
    title: "Registro",
});

definePageMeta({
    layout: "registration",
    middleware: "registration",
    name: "robots",
    content: "noindex, nofollow",
});

// route
const route = useRoute();

// state
const state = reactive({
    brand: {},
    brandLogo: "",
    brandId: "",
    isLoading: true,
});

// Functions
async function getBrandInfo() {
    // get the brand id
    const brand_id = route.params.brand_id;
    // check if the brand exists in the database
    try {
        const res = await API.get(`/back/api/brands/${brand_id}/`);
        // if the brand exists
        if (res.status === 200) {
            state.brand = res.data;
            if (res.data.slug === "sxt") {
                state.brandLogo = "/img/brands/sxt2.svg";
            } else if (res.data.slug === "foundations") {
                state.brandLogo = "/img/brands/galerias.svg";
            } else {
                state.brandLogo = `/img/brands/${state.brand.slug}.svg`;
            }
            state.brandId = brand_id;
        }
    } catch (error) {
        // if the brand does not exist
        if (error.response.status === 404) {
            // return page not found error
            return abortNavigation();
        }
    }
}

// Lifecycle
onBeforeMount(async () => {
    await getBrandInfo();
    state.isLoading = false;
});
</script>

<style lang="scss" scoped>
@import "assets/css/variables";

.register-header {
    width: 100%;
}

.landing-container-2 {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 100px;
    width: 100%;
    padding-bottom: 100px;

    @media (max-width: $default-breakpoint) {
        padding-bottom: 66px;
        gap: 66px;
    }
}

.loader-container {
    display: flex;
    align-items: center;
    min-height: 100vh;
    justify-content: center;

    .loading-dual-ring::after {
        border: 6px solid $primary;
        border-color: $primary transparent $primary transparent;
    }
}

.sxt-container-registration--footer {
    width: 100%;
}
</style>
