<template>
    <StickyHeader v-if="!state.isLoading" class="header-confirmation" ref="header" />
    <div v-if="!state.isLoading" class="landing-container-confirmation">
        <RegistrationMessage :brand-logo="state.brandLogo" :brand-id="state.brandId" :registration-email="state.email">
        </RegistrationMessage>
        <RegistrationTreeStreetMapConfirmation :postal-address="state.brandPostalAddress" :brand-name="state.brandName"
            :brand-slug="state.brand.slug"></RegistrationTreeStreetMapConfirmation>
        <ContestInformation />
        <Donations />
        <BrandCarousel />
    </div>
    <RegistrationFooter v-if="!state.isLoading" class="footer-confirmation" />
    <div v-if="state.isLoading" class="loader-container">
        <div class="loading-dual-ring"></div>
    </div>
</template>

<script setup>
import StickyHeader from "../../../components/StickyHeader.vue";
import RegistrationTreeStreetMapConfirmation from "@/components/RegistrationTreeStreetMapConfirmation.vue";
import RegistrationMessage from "@/components/generic/RegistrationMessage.vue";
import { onBeforeMount, reactive } from "vue";
import API from "@/utils/axios";
import Donations from "@/components/generic/Donations.vue";
import BrandCarousel from "@/components/generic/BrandCarousel.vue";

// route
const route = useRoute();

// head
useHead({
    title: "Confirmación de registro",
});

// page meta
definePageMeta({
    layout: "confirmation",
    middleware: "confirmation",
});

// state
const state = reactive({
    brand: {},
    brandLogo: "",
    brandId: "",
    brandPostalAddress: "",
    brandName: "",
    email: "",
    isLoading: true,
});

// get brand info
async function getBrandInfo() {
    // get the brand id
    const brand_id = route.params.brand_id;
    // get the email from cookies
    state.email = useCookie("email").value;
    // check if the brand exists in the database
    try {
        const res = await API.get(`/back/api/brands/${brand_id}/`);
        // if the brand exists
        if (res.status === 200) {
            // store the brand info
            state.brand = res.data;
            if (state.brand.slug === "foundations") {
                state.brandLogo = "/img/brands/galerias.svg";
            } else {
                state.brandLogo = `/img/brands/${state.brand.slug}.svg`;
            }
            state.brandId = brand_id;
            state.brandPostalAddress = state.brand.postal_address;
            state.brandName = state.brand.name;
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

.header-confirmation {
    width: 100%;
}

.landing-container-confirmation {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    gap: 100px;
    padding-bottom: 100px;

    @media (max-width: $default-breakpoint) {
        gap: 80px;
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

.footer-confirmation {
    width: 100%;
}
</style>
