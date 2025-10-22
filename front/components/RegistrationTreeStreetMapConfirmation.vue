<template>
    <div class="landing-registration-map">
        <div class="landing-welcome">
            <BrandRegistrationMessage
                :brand-slug="props.brandSlug"
                :brand-name="props.brandName"
                :postal-address="props.postalAddress"
            ></BrandRegistrationMessage>
            <div class="map-container">
                <img class="map-trees" src="~/assets/img/maps/trees.svg" />
            </div>
        </div>
    </div>
</template>

<script setup>
import BrandRegistrationMessage from "~/components/generic/BrandRegistrationMessage.vue";

// props
const props = defineProps({
    postalAddress: {
        type: String,
        required: true,
    },
    brandName: {
        type: String,
        required: true,
    },
    brandSlug: {
        type: String,
        default: "",
    },
});
</script>

<style lang="scss" scoped>
@import "assets/css/variables";

.landing-registration-map {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    background: rgb(232, 100, 100);
    background: linear-gradient(
        rgba(232, 100, 100, 1) 3%,
        rgba(159, 8, 29, 1) 100%
    );
    padding-bottom: 30px;

    @media (max-width: $default-breakpoint) {
        padding-bottom: 20px;
    }

    .landing-welcome {
        display: flex;
        flex-direction: column;
        align-items: center;

        width: 100%;

        .map-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            width: 100%;

            max-width: $max-width-lg;
            margin: 109px 0 0 0;
            gap: 100px;

            @media (max-width: $default-breakpoint) {
                margin: 64px 0 0 0;
                padding: 0 24px 0 24px;
                gap: 44px;
            }

            .map-trees {
                width: 100%;
                max-width: 573px;
                height: auto;
            }
        }
    }
}
</style>
