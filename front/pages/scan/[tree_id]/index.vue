<template>
    <div v-if="!state.isLoading" class="visits-container">
        <div class="brand-logo">
            <img :src="state.brandLogo" />
        </div>
        <div class="visit-info">
            <div class="info-banner">
                <p>
                    SU VISITA AL ÁRBOL DE
                    <span style="text-transform: uppercase">{{ state.brand?.name }}
                    </span>
                    SE HA VALIDADO CON ÉXITO
                </p>
            </div>
            <div class="info-tree--validate">
                <img width="50" height="50" src="~/assets/img/scan/star.svg" />
                <div class="tree-validate--text">
                    <p class="text-counter">
                        <span>{{ state.visitsCount }}</span> DE <span>15</span>
                    </p>
                    <p class="text-trees">ÁRBOLES VALIDADOS</p>
                </div>
                <img width="50" height="50" src="~/assets/img/scan/star.svg" />
            </div>
            <div class="info-text--validate">
                <p v-if="state.visitsCount < 7 && state.visitsCount !== 6" class="text-validate--progress">
                    VALIDE {{ 7 - state.visitsCount }} ÁRBOLES MÁS PARA
                    PARTICIPAR EN EL EXCLUSIVO SORTEO
                    <span>DE UNA EXPERIENCIA DE LUJO ÚNICA EN EL PALACIO ARRILUCE
                        HOTEL EN GETXO</span>
                </p>
                <p v-if="state.visitsCount < 7 && state.visitsCount === 6" class="text-validate--progress">
                    VALIDE 1 ÁRBOL MÁS PARA PARTICIPAR EN EL EXCLUSIVO SORTEO
                    <span>DE UNA EXPERIENCIA DE LUJO ÚNICA EN EL PALACIO ARRILUCE
                        HOTEL EN GETXO</span>
                </p>
                <div v-if="state.visitsCount < 7" class="text-validate--remaining">
                    <p>
                        TIENE HASTA EL 25 DE NOVIEMBRE PARA
                        <span>COMPLETAR LA RUTA</span>
                    </p>
                </div>
                <p v-if="state.visitsCount === 7" class="text-validate--progress">
                    ¡ENHORABUENA! <br />
                    YA HA ENTRADO EN EL SORTEO
                    <span>DE UNA EXPERIENCIA DE LUJO ÚNICA EN EL PALACIO ARRILUCE
                        HOTEL EN GETXO</span>
                </p>
                <div v-if="state.visitsCount === 7" class="text-validate--remaining">
                    <p>
                        TIENE HASTA EL 25 DE NOVIEMBRE PARA VER LOS 8 ÁRBOLES DE
                        NAVIDAD QUE LE FALTAN PARA <br />
                        <span>COMPLETAR LA RUTA</span>
                    </p>
                </div>
                <p v-if="state.visitsCount > 7 && state.visitsCount < 15" class="text-validate--progress">
                    RECUERDE QUE YA PARTICIPA EN EL EXCLUSIVO SORTEO DE
                    <span>DE UNA EXPERIENCIA DE LUJO ÚNICA EN EL PALACIO ARRILUCE
                        HOTEL EN GETXO</span>
                </p>
                <div v-if="state.visitsCount > 7 && state.visitsCount < 15" class="text-validate--remaining">
                    <p v-if="state.visitsCount !== 14">
                        TIENE HASTA EL 25 DE NOVIEMBRE PARA VER LOS
                        {{ 15 - state.visitsCount }} ÁRBOLES DE NAVIDAD QUE LE
                        FALTAN PARA COMPLETAR LA RUTA
                    </p>
                    <p v-else>
                        TIENE HASTA EL 25 DE NOVIEMBRE PARA VER EL ÚLTIMO ÁRBOL
                        DE NAVIDAD QUE LE FALTA PARA COMPLETAR LA RUTA
                    </p>
                </div>
                <p v-if="state.visitsCount === 15" class="text-validate--congratulations">
                    ¡GRACIAS POR COMPLETAR LA RUTA SOLIDARITY XMAS TREE!
                </p>
            </div>
            <div v-show="!state.isMapLoading" class="info-map">
                <div v-if="state.visitsCount < 15" class="map-text">
                    <p v-if="state.visitsCount < 7">
                        ¡VISITE, VALIDE <br />
                        y GANE!
                    </p>
                    <p v-if="state.visitsCount >= 7 && state.visitsCount < 15">
                        ¡COMPLETE LA RUTA SOLIDARITY XMAS TREE!
                    </p>
                </div>
                <div class="map">
                    <Map :brands="state.brands" :map-loaded="handleMapLoad()"></Map>
                </div>
            </div>
        </div>
    </div>
    <ContestInformation v-if="!state.isLoading" :raffle-winner="state.visitsCount > 6" :visits-count="state.visitsCount"
        :qr-pages="true"></ContestInformation>
    <Donations v-if="!state.isLoading"></Donations>
    <YellowTree v-if="!state.isLoading" class="yellow-tree"></YellowTree>
    <BrandCarousel v-if="!state.isLoading"></BrandCarousel>
    <div v-if="state.isLoading" class="loader-container">
        <div class="loading-dual-ring"></div>
    </div>
    <RegistrationFooter v-if="!state.isLoading" class="sxt-container-scan--footer" />
</template>

<script setup>
import RegistrationFooter from "../../../components/RegistrationFooter.vue";
import Donations from "../../../components/generic/Donations.vue";
import YellowTree from "../../../components/generic/YellowTree";
import BrandCarousel from "../../../components/generic/BrandCarousel.vue";
import ContestInformation from "../../../components/ContestInformation.vue";
import Map from "../../../components/svg/Map.vue";
import { reactive, onBeforeMount } from "vue";
import API from "../../../utils/axios";

definePageMeta({
    layout: "scan",
    middleware: "scan",
});

const route = useRoute();

// State
const state = reactive({
    brand: {},
    brands: [],
    brandName: "Scan",
    brandLogo: "",
    visitsCount: 0,
    isMapLoading: false,
    isLoading: true,
});

// Functions
async function visitTree() {
    const tree_id = route.params.tree_id;
    try {
        const res = await API.get(`/back/api/brands/visit/${tree_id}/`);
        if (res.status === 200) {
            state.brand = res.data;
            state.brandName = res.data.name;
            state.brandLogo = `/img/brands/${state.brand.slug}.svg`;
        }
    } catch (error) {
        navigateTo("/");
    }
}

async function getVisitsCount() {
    try {
        const res = await API.get(`/back/api/user/me/`);
        if (res.status === 200) {
            state.visitsCount = res.data.visits_count;
        }
    } catch (error) {
        console.log(error);
    }
}

async function getBrands() {
    try {
        const res = await API.get("/back/api/brands/");
        if (res.status === 200) {
            state.brands = res.data;
        }
    } catch (error) {
        console.log(error);
    }
}

function handleMapLoad() {
    state.isMapLoading = false;
}

state.isMapLoading = true;

// Getters
const getters = {
    getName: () => {
        return state.brandName;
    },
};

onBeforeMount(async () => {
    await visitTree();
    await getVisitsCount();
    await getBrands();
    state.isLoading = false;
});

useHead({
    titleTemplate: () => {
        return `${getters.getName()} - Solidarity XMas Tree`;
    },
});
</script>

<style lang="scss" scoped>
@import "assets/css/variables";

.visits-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 32px;
    margin-top: 40px;

    .brand-logo {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 48px;

        img {
            width: 100%;
            height: auto;
        }
    }

    .visit-info {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 90px;

        .info-banner {
            display: flex;
            width: 100%;
            padding: 16px 20px;
            justify-content: center;
            align-items: center;
            gap: 10px;
            background-color: $primary;

            p {
                color: $font-secondary;
                text-align: center;

                font-size: 22px;
                font-style: normal;
                font-weight: 300;
                line-height: 30px;
                /* 136.364% */
                letter-spacing: 1.76px;
            }
        }

        .info-tree--validate {
            display: flex;
            justify-content: center;
            align-items: flex-end;
            gap: 23px;

            img {
                width: 100%;
                height: auto;
                max-width: 50px;
            }

            .tree-validate--text {
                display: flex;
                flex-direction: column;
                align-items: center;
                gap: 11px;

                .text-counter {
                    color: $primary;
                    font-size: 22px;
                    font-style: normal;
                    font-weight: 300;
                    line-height: 30px;
                    letter-spacing: 1.76px;
                    margin: 0;

                    span {
                        text-align: center;
                        font-size: 52px;
                        letter-spacing: 4.16px;
                    }
                }

                .text-trees {
                    color: $primary;
                    text-align: center;
                    font-size: 14px;
                    font-style: normal;
                    font-weight: 300;
                    line-height: normal;
                    letter-spacing: 1.12px;
                    margin: 0;
                }
            }
        }

        .info-text--validate {
            display: flex;
            width: 100%;
            padding: 0px 25px;
            flex-direction: column;
            justify-content: center;
            align-items: flex-start;
            gap: 32px;

            .text-validate--progress {
                color: $text-color-primary;
                text-align: center;
                font-size: 22px;
                font-style: normal;
                font-weight: 300;
                line-height: 30px;
                /* 136.364% */
                letter-spacing: 1.76px;

                span {
                    font-weight: 500;
                }
            }

            .text-validate--congratulations {
                color: $text-color-primary;
                text-align: center;
                font-size: 32px;
                font-style: normal;
                font-weight: 400;
                line-height: 36px;
                /* 112.5% */
            }

            .text-validate--remaining {
                display: flex;
                align-items: center;
                gap: 10px;
                align-self: stretch;

                p {
                    color: $text-color-primary;
                    text-align: center;

                    font-size: 22px;
                    font-style: normal;
                    font-weight: 300;
                    line-height: 30px;
                    /* 136.364% */
                    letter-spacing: 1.76px;

                    span {
                        font-weight: 500;
                    }
                }
            }
        }

        .info-map { //cambio temporal
            display: flex;
            width: 100%;
            flex-direction: column;
            justify-content: center;
            align-items: center;

            .map-text {
                display: flex;
                padding: 40px 0px 40px 0px;
                justify-content: center;
                align-items: center;
                gap: 10px;
                align-self: stretch;
                background: $primary;

                p {
                    color: #fff;
                    text-align: center;
                    font-size: 32px;
                    font-style: normal;
                    font-weight: 300;
                    line-height: 30px;
                    /* 93.75% */
                    letter-spacing: 2.56px;
                    margin: 0;
                }
            }

            .map {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                width: 100%;
                gap: 15px;
                padding: 35px 30px 30px 30px;
                background: linear-gradient(rgba(232, 100, 100, 1) 3%,
                        rgba(159, 8, 29, 1) 100%);
            }
        }
    }
}

.loader-container {
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 100vh;

    .loading-dual-ring::after {
        border: 6px solid $primary;
        border-color: $primary transparent $primary transparent;
    }
}

.yellow-tree {
    padding-left: 25px;
    padding-right: 25px;
}
</style>
