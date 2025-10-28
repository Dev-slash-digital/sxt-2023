<template>
    <div class="landing-container">
        <div class="landing-intro">
            <div id="weare" style="opacity: 0">
                <img class="logo-purple" width="106.6" height="100" src="~/assets/img/logo-purple.svg" />
            </div>
            <p class="intro-text">
                SOLIDARITY XMAS TREE
                <span style="font-style: italic">es un </span>EVENTO SOLIDARIO
                EN EL QUE LAS MARCAS DE LUJO MÁS IMPORTANTES DEL MUNDO
                <span style="font-style: italic">crean</span> ÁRBOLES DE NAVIDAD
                ÚNICOS <span style="font-style: italic">y</span> EXCLUSIVOS
                <span style="font-style: italic">que se </span>SUBASTAN A FAVOR
                DE TRES FUNDACIONES BENÉFICAS
            </p>
            <div class="trees-carousel">
                <div class="trees-carousel--header">
                    <SmallTree></SmallTree>
                    <p>DESCUBRA LOS ÁRBOLES DE EDICIONES ANTERIORES</p>
                </div>
                <LazyCarousel v-if="state.isMobile" :pictures="pictures" :trees-carousel="true"></LazyCarousel>
                <CustomCarousel v-else :pictures="pictures" :trees-carousel="true">
                </CustomCarousel>
            </div>
        </div>
        <div class="landing-map">
            <div class="info-container">
                <img class="info-logo" width="140" height="180" src="~/assets/img/logo-red-home.svg" />
                <p class="info-text">
                    DEL
                    <span style="font-weight: 400">18 <span style="font-style: italic">al</span> 24 DE
                        NOVIEMBRE,</span>
                    <span style="font-style: italic"> los </span>ÁRBOLES DE
                    NAVIDAD SE EXPONEN
                    <span style="font-style: italic">en las</span> BOUTIQUES DE
                    <span style="font-style: italic">las</span>
                    MARCAS PARTICIPANTES FORMANDO LA RUTA SOLIDARITY XMAS TREE
                </p>
            </div>
            <div class="map-container">
                <img class="map-trees" src="~/assets/img/maps/trees.svg" />
            </div>
        </div>
        <div class="landing-brands">
            <BrandCarousel></BrandCarousel>
        </div>
        <div class="landing-videos">
            <Donations></Donations>
        </div>
    </div>
</template>

<script setup>
import LazyCarousel from "../components/LazyCarousel.vue";
import CustomCarousel from "../components/CustomCarousel.vue";
import BrandCarousel from "../components/generic/BrandCarousel.vue";
import SmallTree from "../components/generic/SmallTree.vue";
import Donations from "../components/generic/Donations.vue";

import { onMounted, reactive } from "vue";

useHead({
    title: "Home",
});

const state = reactive({
    isMobile: false,
});

const pictures = [
    ["/img/trees/1.webp", "Cartier, Solidarity Xmas Tree 2024"],
    ["/img/trees/2.webp", "Maison Valmont, Solidarity Xmas Tree 2024"],
    ["/img/trees/3.webp", "Chopard, Solidarity Xmas Tree 2024"],
    ["/img/trees/4.webp", "Jaeger-LeCoultre, Solidarity Xmas Tree 2024"],
    ["/img/trees/5.webp", "Loewe, Solidarity Xmas Tree 2024"],
    ["/img/trees/6.webp", "NUBA, Solidarity Xmas Tree 2024"],
    ["/img/trees/7.webp", "Omega, Solidarity Xmas Tree 2024"],
    ["/img/trees/8.webp", "Suarez, Solidarity Xmas Tree 2024"],
    ["/img/trees/9.webp", "Stefano Ricci, Solidarity Xmas Tree 2024"],
    ["/img/trees/10.webp", "ZE, Solidarity Xmas Tree 2024"],
    ["/img/trees/11.webp", "Giorgio Armani, Solidarity Xmas Tree 2024"],
    ["/img/trees/12.webp", "Chaumet, Solidarity Xmas Tree 2024"],
    ["/img/trees/13.webp", "Hermes, Solidarity Xmas Tree 2024"],
    ["/img/trees/14.webp", "IWC, Solidarity Xmas Tree 2024"],
    ["/img/trees/15.webp", "Chanel, Solidarity Xmas Tree 2021"],
    ["/img/trees/16.webp", "Etro, Solidarity Xmas Tree 2017"],
    ["/img/trees/17.webp", "Stella Mc Cartney, Solidarity Xmas Tree 2022"],
    ["/img/trees/18.webp", "Zimmermann, Solidarity Xmas Tree 2022"],
    ["/img/trees/19.webp", "Prada, Solidarity Xmas Tree 2021"],
    ["/img/trees/20.webp", "Loro Piana, Solidarity Xmas Tree 2020"],
    ["/img/trees/21.webp", "Brunello Cucinelli, Solidarity Xmas Tree 2019"],
];

function isMobile() {
    return (
        navigator.userAgent.match(/Android/i) ||
        navigator.userAgent.match(/webOS/i) ||
        navigator.userAgent.match(/iPhone/i) ||
        navigator.userAgent.match(/iPad/i) ||
        navigator.userAgent.match(/iPod/i) ||
        navigator.userAgent.match(/BlackBerry/i) ||
        navigator.userAgent.match(/Windows Phone/i)
    );
}

onMounted(() => {
    if (isMobile()) {
        state.isMobile = true;
    } else {
        state.isMobile = false;
    }
});
</script>

<style lang="scss" scoped>
@import "assets/css/variables";

p {
    margin: 0;

    @media (max-width: $default-breakpoint) {
        padding-right: 25px;
        padding-left: 25px;
    }
}

.landing-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 100px;
    width: 100%;

    @media (max-width: $default-breakpoint) {
        gap: 66px;
    }

    .landing-intro {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 100px;
        width: 100%;
        max-width: $max-width-lg;

        @media (max-width: $default-breakpoint) {
            gap: 66px;
        }

        .intro-text {
            font-size: 41px;
            font-weight: 250;
            text-align: center;

            font-style: normal;
            line-height: 44px;
            width: 870px;

            @media (max-width: $default-breakpoint) {
                font-size: $font-size-large-mobile;
                line-height: 36px;
                width: 100%;
            }
        }

        .trees-carousel {
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 100%;
            gap: 50px;

            @media (max-width: $default-breakpoint) {
                gap: 32px;
            }

            .trees-carousel--header {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                text-align: center;
                gap: 20px;

                @media (max-width: $default-breakpoint) {
                    gap: 15px;
                }

                p {
                    font-size: $font-size-medium;
                    line-height: 30px;
                    font-style: normal;
                    font-weight: 300;
                    letter-spacing: 1.76px;

                    @media (max-width: $default-breakpoint) {
                        line-height: 24px;
                        letter-spacing: 1.44px;
                        font-size: $font-size-medium-mobile;
                    }
                }
            }
        }
    }

    .landing-map {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;

        .info-container {
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 100px 0;

            @media (max-width: $default-breakpoint) {
                padding: 50px 0px;
            }

            background-color: $primary;

            .info-logo {
                width: 100%;
                max-width: 160px;
                height: auto;
                margin-bottom: 50px;

                @media (max-width: $default-breakpoint) {
                    max-width: 83.25px;
                    margin-bottom: 40px;
                }
            }

            .info-text {
                color: white;
                text-align: center;
                font-size: $font-size-large;
                font-weight: 250;
                line-height: 44px;
                max-width: 930px;

                @media (max-width: $default-breakpoint) {
                    width: 100%;
                    font-size: $font-size-large-mobile;
                    line-height: 36px;
                }
            }
        }

        .map-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            width: 100%;
            background: #088296;
            padding: 55px 0 55px 0;
            gap: 100px;

            @media (max-width: $default-breakpoint) {
                padding: 40px 0px 40px 0px;
                gap: 44px;
            }

            .map-trees {
                width: 100%;
                max-width: 665px;
                height: auto;
            }
        }
    }

    .landing-brands {
        width: 100%;

        max-width: $max-width-lg;
    }

    .landing-videos {
        margin-bottom: 100px;

        max-width: $max-width-lg;

        @media (max-width: $default-breakpoint) {
            margin-bottom: 112px;
        }
    }
}

.logo-purple {
    width: 100%;
    max-width: 106.6px;
    height: auto;
}
</style>
