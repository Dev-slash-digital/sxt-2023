<template>
    <div class="landing-contest">
        <div class="landing-contest-logo">
            <img alt="Solidarity Xmas Tree" class="landing-contest-logo-img" src="~/assets/img/generic/contest-logo.svg"
                width="47" height="72" />
        </div>
        <div class="landing-contest-process">
            <p v-if="!props.raffleWinner && props.visitsCount < 7" class="landing-contest-process-text">
                HAGA LA RUTA
                <span style="font-style: italic">y entre en el</span> SORTEO
                <span style="font-style: italic">de una</span> EXPERIENCIA DE
                LUJO ÚNICA
                <span style="font-style: italic">en <br />
                    el</span>
                PALACIO ARRILUCE HOTEL
                <span style="font-style: italic">en</span> GETXO
            </p>
            <p v-if="props.raffleWinner && props.visitsCount === 7" class="landing-contest-process-text-scan">
                HA ENTRADO
                <span style="font-style: italic">en el</span> SORTEO
                <span style="font-style: italic">de <br />
                    una</span>
                EXPERIENCIA DE LUJO ÚNICA <br />
                <span style="font-style: italic">en el </span>PALACIO ARRILUCE
                HOTEL <span style="font-style: italic"> en </span> GETXO
            </p>
            <p v-if="props.raffleWinner && props.visitsCount > 7" class="landing-contest-process-text-scan">
                USTED YA PARTICIPA
                <span style="font-style: italic">en el</span> SORTEO
                <span style="font-style: italic">de <br />
                    una</span>
                EXPERIENCIA DE LUJO ÚNICA <br />
                <span style="font-style: italic">en el </span>PALACIO ARRILUCE
                HOTEL <span style="font-style: italic"> en </span> GETXO
            </p>
        </div>
        <div v-if="!props.qrPages" class="landing-contest-qr">
            <p class="landing-contest-qr-text">
                VALIDE SU VISITA
                <span style="font-weight: 500">ESCANEANDO EL CÓDIGO QR </span>
                QUE ENCONTRARÁ <br />
                EN LAS BOUTIQUES JUNTO A CADA ÁRBOL.
            </p>
        </div>
        <div v-if="!props.qrPages" class="landing-contest-validation">
            <p class="landing-contest-validation-text">
                Con la validación de
                <span style="font-weight: 500">7 árboles</span> participará en
                <span style="font-weight: 500">el exclusivo sorteo de UNA EXPERIENCIA DE LUJO EN EL
                    PALACIO ARRILUCE HOTEL EN GETXO</span>
            </p>
        </div>
        <div v-if="props.qrPages && props.raffleWinner && props.visitsCount < 15" class="landing-contest-validation">
            <p v-if="props.visitsCount === 7" class="landing-contest-validation-text-scan">
                ¡LE HEMOS ENVIADO UN EMAIL CON LA CONFIRMACIÓN DE SU
                PARTICIPACIÓN EN EL SORTEO!
            </p>
            <p v-if="props.visitsCount > 7" class="landing-contest-validation-text-scan">
                RECUERDE QUE LE HEMOS ENVIADO UN EMAIL CON LA CONFIRMACIÓN DE SU
                PARTICIPACIÓN EN EL SORTEO
            </p>
        </div>
        <div class="landing-contest-grant">
            <div class="landing-contest-grant-img"></div>
            <div class="landing-contest-grant-detail">
                <div :class="{
                    'landing-contest-grant-info': true,
                    open: state.showAdditionalInformation,
                }">
                    <p class="landing-contest-grant-info-text">
                        Disfrute del lujo sereno a orillas del mar Cantábrico.
                        Una estancia de tres noches en la suite Arriluce del
                        Palacio Arriluce Hotel en Getxo, con salida en barco de
                        vela por la Ría hasta el Museo Guggenheim y otras
                        actividades únicas para vivir la elegancia, la
                        exclusividad, la belleza y el arte de un concepto único.
                        <br /><br />
                        El premio incluye la cesión de un BMW XM con el que
                        disfrutar del viaje, en esta experiencia única.
                    </p>
                    <div class="more-info-text">
                        <p>
                            Un enclave único en Getxo, Bilbao donde la historia
                            se fusiona con la vanguardia.
                        </p>
                        <p>
                            Lo que fue en 1912 el primer palacete de la zona de
                            Neguri y símbolo de una aristocracia rupturista con
                            querencia británica, es hoy un alojamiento de lujo
                            en Getxo (Bilbao) que abraza el prestigio, el alma y
                            el estilo vanguardista cien años después de su
                            edificación.
                        </p>
                        <p>
                            Su belleza exterior, encabezada por una arquitectura
                            semejante a un castillo medieval, y su histórica
                            Pérgola, en pleno jardín, se combinan con la riqueza
                            que esconde cada estancia interior entre piezas
                            confeccionadas para Palacio Arriluce Hotel de la
                            mano de artistas como Sonia Delunay, Alberdi, Diego
                            Canogar o Jon Cacenave, influencias del interiorismo
                            de William Morris, del Art Déco y el color más
                            representativo del pasado familiar.
                        </p>
                        <p>
                            Para hacer esta experiencia más única, exclusiva e
                            inolvidable podrá disfrutar, por gentileza del
                            hotel, de:
                        </p>

                        <p>
                            &bull; Salida en barco de vela desde el hotel por la
                            ría al Museo Guggenheim y visita al Museo con guía
                            privado.
                        </p>
                        <p>
                            &bull; Tratamiento Spa dos días para dos personas:
                            masaje corporal y circuito de aguas.
                        </p>
                        <p>&bull; Cata en la bodega del hotel.</p>
                        <p>&bull; Desayuno, comida y cena incluidos.</p>
                        <p>
                            &bull; Otras actividades del hotel incluidas como
                            clases de croquet.
                        </p>

                        <p>
                            Palacio Arriluce Hotel es miembro de The Leading
                            Hotels of the World <br />
                            <a class="palace-link" href="https://www.palacioarrilucehotel.com/es/"
                                target="_blank">www.palacioarrilucehotel.com/es/</a>
                        </p>
                        <div class="follow-logo">
                            <a class="follow-link" href="https://www.instagram.com/solidarityxmastree/" target="_blank">
                                <Instagram></Instagram>
                            </a>
                        </div>
                    </div>
                    <Button @handle-click="handleShowAdditionalInformation">Más información</Button>
                    <a class="landing-contest-grant-info-terms-link" href="/conditions/">Términos y condiciones del
                        sorteo</a>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import Button from "~/components/generic/Button.vue";
import Instagram from "~/components/svg/Instagram.vue";
import { reactive } from "vue";

// Props
const props = defineProps({
    qrPages: {
        type: Boolean,
        default: false,
    },
    raffleWinner: {
        type: Boolean,
        default: false,
    },
    visitsCount: {
        type: Number,
        default: 0,
    },
});

// state variables
let state = reactive({
    showAdditionalInformation: false,
});

// methods
const handleShowAdditionalInformation = () => {
    // toggle collapse state
    state.showAdditionalInformation = !state.showAdditionalInformation;
};
</script>

<style lang="scss" scoped>
@import "assets/css/variables";

.landing-contest {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    gap: 60px;
    max-width: $max-width-lg;

    @media (max-width: $default-breakpoint) {
        padding: 0px 25px;
    }

    .landing-contest-logo {
        display: flex;
        flex-direction: column;
        align-items: center;

        .landing-contest-logo-img {
            width: 47px;
            height: auto;
        }
    }

    .landing-contest-process {
        display: flex;
        flex-direction: column;
        align-items: center;

        .landing-contest-process-text {
            overflow: hidden;
            max-width: 870px;
            text-align: center;
            font-style: normal;
            font-weight: 250;
            font-size: $font-size-large;
            line-height: 44px;
            margin: 0;
            padding: 0;

            @media (max-width: $default-breakpoint) {
                padding: 15px;
                width: 100%;
                font-size: $font-size-large-medium;
                line-height: 1.2em;
            }
        }

        .landing-contest-process-text-scan {
            text-align: center;
            font-style: normal;
            font-weight: 250;
            font-size: $font-size-large;
            line-height: 44px;
            margin: 0;
            padding: 0;
        }
    }

    .landing-contest-qr {
        display: flex;
        flex-direction: column;
        align-items: center;

        .landing-contest-qr-text {
            text-align: center;
            font-style: normal;
            font-weight: 300;
            font-size: $font-size-medium;
            line-height: 30px;
            letter-spacing: 1.76px;
            text-transform: uppercase;
            margin: 0;
            padding: 0;

            @media (max-width: $default-breakpoint) {
                font-size: 18px;
                line-height: 24px;
                letter-spacing: 1.44px;
                width: 100%;
            }
        }
    }

    .landing-contest-validation {
        display: flex;
        flex-direction: column;
        align-items: center;

        .landing-contest-validation-text {
            max-width: 887px;
            text-align: center;
            font-style: normal;
            font-weight: 300;
            font-size: $font-size-medium;
            line-height: 30px;
            letter-spacing: 1.8px;
            text-transform: uppercase;
            margin: 0;
            padding: 0;

            @media (max-width: $default-breakpoint) {
                width: 100%;
                font-size: 18px;
                line-height: 24px;
                letter-spacing: 1.44px;
            }
        }

        .landing-contest-validation-text-scan {
            text-align: center;
            font-style: normal;
            font-weight: 300;
            font-size: $font-size-medium;
            line-height: 30px;
            letter-spacing: 1.76px;
            text-transform: uppercase;
            margin: 0;
            padding: 0;

            @media (max-width: $default-breakpoint) {
                width: 100%;
                font-size: 21px;
                line-height: 30px;
                letter-spacing: 1.76px;
            }
        }
    }

    .landing-contest-grant {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 30px;
        text-align: center;
        max-width: 888px;

        @media (max-width: $default-breakpoint) {
            width: 100%;
        }

        .landing-contest-grant-img {
            display: flex;
            width: 888px;
            height: 525px;
            background: url("~/assets/img/registration/contest-grant.png") lightgray 50% / cover no-repeat;

            @media (max-width: $default-breakpoint) {
                height: 225px;
                width: -webkit-fill-available;
            }
        }

        .landing-contest-grant-detail {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 10px;

            .landing-contest-grant-info.open .more-info-text {
                max-height: 100%;
            }

            .landing-contest-grant-info {
                display: flex;
                flex-direction: column;
                align-items: center;
                gap: 30px;
                align-self: stretch;

                .landing-contest-grant-info-text {
                    max-width: 887px;
                    text-align: center;
                    font-style: normal;
                    font-weight: 100;
                    font-size: $font-size-large-medium;
                    line-height: 1.2em;
                    letter-spacing: auto;
                    margin: 0;
                    padding: 0;

                    @media (max-width: $default-breakpoint) {
                        font-size: $font-size-medium;
                        line-height: 1.2em;
                    }
                }

                .more-info-text {
                    max-width: 887px;
                    max-height: 0;
                    overflow: hidden;
                    transition: max-height 0.3s ease-in-out;
                    text-align: center;
                    font-style: normal;
                    font-weight: 100;
                    font-size: $font-size-large-medium;
                    line-height: 1.2em;
                    margin: 0;
                    padding: 0;

                    @media (max-width: $default-breakpoint) {
                        font-size: $font-size-medium;
                    }

                    .palace-link {
                        text-decoration: none;
                        color: $text-color-primary;
                    }
                }

                .landing-contest-grant-info-terms-link {
                    color: $text-color-primary;
                }
            }
        }
    }
}
</style>
