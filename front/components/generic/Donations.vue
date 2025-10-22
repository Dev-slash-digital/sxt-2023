<template>
    <div class="donations-container">
        <div class="donations-videos">
            <SmallTree
                id="foundations"
                class="donations-smalltree"
                style="margin: 0 auto"
            ></SmallTree>
            <p style="margin-top: 40px">
                EL 26 DE NOVIEMBRE
                <span style="font-style: italic">los</span> ARBOLES SERÁN
                SUBASTADOS A BENEFICIO
                <span style="font-style: italic">de:</span>
            </p>
            <div class="videos">
                <Videos></Videos>
            </div>
        </div>
        <div class="donations-info">
            <div class="donations-header">
                <p>
                    SI LO DESEA PUEDE HACER UNA DONACIÓN MEDIANTE TRANSFERENCIA
                    BANCARIA
                </p>
            </div>
            <div class="foundations">
                <div class="friends">
                    <div class="friends-image">
                        <img
                            src="~/assets/img/foundations/friends.png"
                            width="121"
                            height="51"
                        />
                    </div>
                    <div class="friends-text">
                        <h4>GRANDES AMIGOS</h4>
                        <div class="friends-info">
                            <p>
                                <span style="font-weight: 500">IBAN</span> ES06
                                2080 1600 0530 4001 3111
                            </p>
                            <p>
                                <span style="font-weight: 500">CONCEPTO</span>
                                DONACIÓN SOLIDARITY XMAS TREE GRANDES AMIGOS
                            </p>
                        </div>
                        <p class="friends-description">
                            Grandes Amigos se basa en el voluntariado. Desde
                            2003, previene y aborda la soledad de las personas
                            mayores mediante diferentes programas de
                            acompañamiento y socialización, creando vínculos de
                            vecindad, apoyo mutuo y amistad
                        </p>
                        <Link
                            :href="'https://www.instagram.com/grandes_amigos/'"
                            class="friends-text-link"
                            >MÁS INFORMACIÓN GRANDES AMIGOS</Link
                        >
                    </div>
                </div>
                <div class="mothers">
                    <div class="mothers-image">
                        <img
                            src="~/assets/img/foundations/mothers.png"
                            width="174"
                            height="16"
                        />
                    </div>
                    <div class="mothers-text">
                        <h4>MAMÁS EN ACCIÓN</h4>
                        <div>
                            <p>
                                <span style="font-weight: 500">IBAN</span> ES69
                                2080 1600 0530 4001 3335
                            </p>
                            <p>
                                <span style="font-weight: 500">CONCEPTO</span>
                                DONACIÓN SOLIDARITY XMAS TREE PROYECTO MAMÁS EN
                                ACCIÓN
                            </p>
                        </div>
                        <p
                            class="mothers-description"
                            style="margin-top: 0.5em"
                        >
                            En 2013 Majo Gimeno, fundadora de Mamás en Acción,
                            vio en un hospital a un niño pequeño enfermo
                            ingresado y solo y descubrió que esa era una
                            realidad que afecta a miles de niños en España. Majo
                            pensó que podía hacer algo por esos niños y así
                            nació Mamás en Acción. Mamás en Acción está formada
                            por más de 2.500 voluntarios, hombres y mujeres, que
                            acompañan y dan “amor maternal” a los niños
                            hospitalizados que están solos.
                        </p>
                        <Link
                            :href="'https://www.instagram.com/mamasenacciones/'"
                            class="mothers-text-link"
                            >MÁS INFORMACIÓN FUNDACIÓN MAMÁS EN ACCIÓN</Link
                        >
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import SmallTree from "./SmallTree.vue";
import Link from "./Link.vue";
import Videos from "./Videos.vue";
</script>
<style lang="scss" scoped>
@import "assets/css/variables";
.donations-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    .donations-videos {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;

        width: 100%;
        p {
            margin: 0;
            font-weight: 250;
            font-size: $font-size-large;
            font-style: normal;
            line-height: 44px;
            width: 840px;

            @media (max-width: $default-breakpoint) {
                width: 100%;
                font-size: $font-size-large;
                text-align: center;
                padding-right: 25px;
                padding-left: 25px;
            }
        }

        .videos {
            width: 840px;
            margin-bottom: 100px;
            margin-top: 40px;
            @media (max-width: $default-breakpoint) {
                width: 100%;
                margin-bottom: 66px;
                margin-top: 32px;
            }
        }
    }

    .donations-info {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;

        @media (max-width: $default-breakpoint) {
            text-align: center;
            padding-left: 25px;
            padding-right: 25px;
            width: 100%;
        }

        .donations-header {
            width: 100%;

            @media (max-width: $default-breakpoint) {
                width: 100%;
            }

            p {
                font-size: $font-size-medium;
                font-weight: 300;
                line-height: 30px; /* 136.364% */
                letter-spacing: 1.76px;
                width: 80%;
                margin-bottom: 70px;

                @media (max-width: $default-breakpoint) {
                    width: 90%;
                    font-size: $font-size-medium-mobile;
                    font-style: normal;
                    font-weight: 300;
                    line-height: 24px; /* 133.333% */
                    letter-spacing: 1.44px;

                    margin-left: auto;
                    margin-right: auto;
                }
            }
        }

        .foundations {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            margin-left: 30%;
            margin-right: 10%;
            gap: 3em;
            width: 748px;

            @media (max-width: $default-breakpoint) {
                margin: 0;
                width: 100%;
            }

            .friends {
                display: flex;
                justify-content: center;
                width: 100%;
                gap: 24px;
                padding-left: 53px;

                @media (max-width: $default-breakpoint) {
                    flex-direction: column;
                    padding: 0;
                    align-items: center;
                }

                .friends-image {
                    img {
                        width: 100%;
                        height: auto;
                        max-width: 144px;
                    }
                }

                .friends-text {
                    display: flex;
                    flex-direction: column;
                    flex: 1;
                    gap: 8px;
                    margin-top: 5px;

                    @media (max-width: $default-breakpoint) {
                        text-align: center;
                        display: flex;
                        flex-direction: column;
                        align-items: center;
                        gap: 15px;

                        margin-top: 0;
                    }

                    p {
                        margin: 0;

                        font-size: $font-size-small;
                        font-style: normal;
                        font-weight: 300;
                        line-height: 22px;
                        letter-spacing: 0.32px;
                    }

                    h4 {
                        margin: 0;
                        font-weight: 300;
                        font-size: $font-size-medium;
                        font-style: normal;
                        font-weight: 300;
                        line-height: 30px; /* 136.364% */
                        letter-spacing: 1.76px;
                    }
                    .friends-description {
                        width: 100%;
                    }
                    .friends-text-link {
                        margin-top: 7px;
                        @media (max-width: $default-breakpoint) {
                            margin-top: 0px;
                        }
                    }
                }
            }

            .mothers {
                display: flex;
                justify-content: center;
                gap: 24px;
                width: 100%;

                @media (max-width: $default-breakpoint) {
                    flex-direction: column;
                    align-items: center;
                }

                .mothers-image {
                    img {
                        width: 100%;
                        height: auto;
                        max-width: 174px;
                    }
                }

                .mothers-text {
                    display: flex;
                    flex-direction: column;
                    gap: 8px;
                    flex: 1;

                    @media (max-width: $default-breakpoint) {
                        text-align: center;
                        display: flex;
                        flex-direction: column;
                        align-items: center;
                        gap: 15px;
                    }

                    p {
                        margin: 0;
                        font-size: $font-size-small;
                        font-style: normal;
                        font-weight: 300;
                        line-height: 22px;
                        letter-spacing: 0.32px;
                    }

                    h4 {
                        margin: 0;
                        font-weight: 300;
                        font-size: $font-size-medium;
                        font-style: normal;
                        font-weight: 300;
                        line-height: 30px; /* 136.364% */
                        letter-spacing: 1.76px;
                    }
                    .mothers-description {
                        width: 100%;

                        @media (max-width: $default-breakpoint) {
                            width: 100%;
                        }
                    }
                    .mothers-text-link {
                        margin-top: 7px;
                        @media (max-width: $default-breakpoint) {
                            margin-top: 0px;
                        }
                    }
                }
            }
        }
    }
}
</style>
