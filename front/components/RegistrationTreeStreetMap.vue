<template>
    <div class="landing-map">
        <div class="landing-welcome">
            <div class="registration-welcome">
                <img :class="props.brandSlug !== 'sxt'
                        ? 'registration-welcome-brand-logo'
                        : 'registration-welcome-brand-logo-sxt'
                    " :src="brandLogo" />
                <p class="registration-welcome-text">
                    Le da la bienvenida a la ruta solidarity xmas tree
                </p>
                <RegistrationLink :href="`/registration/${brandId}/form/`" target="_parent">Regístrese y acceda a la
                    ruta</RegistrationLink>
            </div>
            <div class="registration-advice">
                <p class="registration-advice-text">
                    <span class="registrese">
                        REGÍSTRESE
                        <span style="font-style: italic">para</span></span>
                    DESCUBRIR
                    <span style="font-style: italic">en</span> EXCLUSIVA
                    <span style="font-style: italic">los</span> ÁRBOLES DE
                    NAVIDAD SOLIDARIOS
                    <span style="font-style: italic">de</span> LA RUTA
                    SOLIDARITY XMAS TREE
                    <span style="font-style: italic">del</span>
                    <span style="font-weight: 400">
                        19 <span style="font-style: italic">AL</span> 25 DE
                        NOVIEMBRE</span>
                </p>
            </div>
            <div class="registration-process">
                <p class="registration-process-text">
                    ¡VISITE, VALIDE
                    <span style="font-style: italic">y</span> GANE!
                </p>
            </div>
        </div>
        <div class="map-container">
            <img class="map-trees" src="~/assets/img/maps/trees.svg" />
        </div>
    </div>
</template>

<script setup>
import RegistrationLink from "../components/generic/RegistrationLink.vue";

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
    brandSlug: {
        type: String,
        default: "",
    },
});
</script>

<style lang="scss" scoped>
@import "assets/css/variables";

.landing-map {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    background-color: $primary;
    gap: 60px;

    @media (max-width: $default-breakpoint) {
        gap: 50px;
    }

    .landing-welcome {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 80px;

        @media (max-width: $default-breakpoint) {
            padding: 50px 0;
        }

        .registration-welcome {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 30px;

            .registration-welcome-brand-logo {
                padding: 0;
                filter: invert(1);

                @media (max-width: $default-breakpoint) {
                    height: auto;
                }
            }

            .registration-welcome-brand-logo-sxt {
                max-width: 108px;
                width: 100%;
                height: auto;
                padding: 0;

                @media (max-width: $default-breakpoint) {
                    max-width: 108px;
                    width: 100%;
                    height: auto;
                }
            }

            .registration-welcome-text {
                text-transform: uppercase;
                color: white;
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

        .registration-advice {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;

            max-width: $max-width-lg;

            .registration-advice-text {
                color: white;
                text-align: center;
                font-size: $font-size-large;
                font-weight: 250;
                line-height: 44px;
                width: 682px;
                margin: 0;

                @media (max-width: $default-breakpoint) {
                    max-width: 300px;
                    width: 100%;
                    font-size: $font-size-large-mobile;
                    line-height: 36px;
                }

                .registrese {
                    @media (max-width: $default-breakpoint) {
                        word-break: break-word;
                        word-spacing: 1000px;
                    }
                }
            }
        }

        .registration-process {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;

            .registration-process-text {
                color: white;
                text-align: center;
                font-size: $font-size-large;
                font-weight: 250;
                line-height: 44px;
                width: 100%;
                margin: 0;

                @media (max-width: $default-breakpoint) {
                    width: 100%;
                    font-size: $font-size-large-mobile;
                    line-height: 36px;
                }
            }
        }
    }

    .map-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
        background: rgb(232, 100, 100);
        background: linear-gradient(rgba(232, 100, 100, 1) 3%,
                rgba(159, 8, 29, 1) 100%);
        padding: 109px 0 66px 0;
        gap: 100px;

        @media (max-width: $default-breakpoint) {
            padding: 64px 30px 24px 30px;
            gap: 44px;
        }

        .map-trees {
            width: 100%;
            max-width: 573px;
            height: auto;
        }
    }
}
</style>
