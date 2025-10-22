<template>
    <div class="registration-message-container">
        <BigSXTLogo></BigSXTLogo>
        <p class="registration-message-text">
            GRACIAS, SE HA REGISTRADO EN LA RUTA CON EL EMAIL
            {{ registrationEmail }}
        </p>
        <YellowTree></YellowTree>
        <div class="registration-welcome">
            <img class="registration-welcome-brand-logo" :src="brandLogo" />
            <p class="registration-welcome-text">
                Le da la bienvenida a la ruta solidarity xmas tree
            </p>
        </div>
        <YellowTree></YellowTree>
    </div>
</template>

<script setup>
import BigSXTLogo from "~/components/generic/BigSXTLogo.vue";
import YellowTree from "~/components/generic/YellowTree.vue";

// props
const props = defineProps({
    brandLogo: {
        type: String,
        required: true,
    },
    brandId: {
        type: String,
        required: true,
    },
    registrationEmail: {
        type: String,
        required: true,
    },
});
</script>

<style scoped lang="scss">
@import "assets/css/variables";

.registration-message-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: 80px;
    padding: 60px 0 0 0;
    max-width: $max-width-lg;
    width: 100%;
    height: auto;

    .yellow-tree-container {
        max-width: 360px;
    }

    @media (max-width: $default-breakpoint) {
        gap: 50px;
        padding: 80px 46px 80px 46px;
        width: 100%;
        height: auto;
    }

    .registration-message-text {
        max-width: 870px;
        width: 100%;
        height: auto;
        font-size: $font-size-medium;
        font-style: normal;
        font-weight: 300;
        line-height: 44px;
        letter-spacing: 1.76px;
        text-transform: uppercase;
        word-wrap: break-word;
        word-break: break-word;

        @media (max-width: $default-breakpoint) {
            max-width: 375px;
            width: 100%;
            height: auto;
            font-size: $font-size-medium-mobile;
            letter-spacing: 1.44px;
            line-height: 24px;
        }
    }

    .registration-welcome {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 30px;

        .registration-welcome-brand-logo {
            padding: 0;

            @media (max-width: $default-breakpoint) {
                height: auto;
            }
        }

        .registration-welcome-text {
            text-transform: uppercase;
            text-align: center;
            font-size: $font-size-medium;
            font-weight: 300;
            line-height: 30px;
            letter-spacing: 1.76px;
            font-style: normal;
            max-width: 870px;
            width: 100%;
            margin: 0;

            @media (max-width: $default-breakpoint) {
                max-width: 317px;
                width: 100%;
                align-self: stretch;
                font-size: $font-size-medium-mobile;
                line-height: 24px;
                letter-spacing: 1.44px;
            }
        }
    }
}
</style>
