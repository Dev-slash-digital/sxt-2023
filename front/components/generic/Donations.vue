<template>
    <div class="donations-container">
        <div class="donations-videos">
            
            <SmallTree id="foundations" class="donations-smalltree" style="margin: 0 auto"></SmallTree>
            <p style="margin-top: 40px">
                EL PODER TRANFORMADOR DE LA FORMACIÓN
            </p>
            <p style="margin-top: 40px" class="texto-oportunidades">
                Que la formación da oportunidades a todos, es un hecho, pero hay tres colectivos para los que tener acceso a una formación de calidad es más difícil que para el resto. Para esas personas, poder formarse es especialmente importante y hacerlo supone un cambio de 180° en sus vidas.
            </p>
            <div class="videos">
                <Videos></Videos>
            </div>
            <p style="margin-top: 40px">
                HAY MUCHAS FORMAS <span style="font-style: italic">de</span> CAMBIAR <span
                    style="font-style: italic">el</span> MUNDO. UNA DE ELLAS ES CREER EN EL POTENCIAL <span
                    style="font-style: italic">de</span> QUIENES SOLO NECESITAN UNA OPORTUNIDAD.
                <br><br>
                EL 25 DE NOVIEMBRE <span style="font-style: italic">los</span> ÁRBOLES SERÁN SUBASTADOS A BENEFICIO
                <span style="font-style: italic">de</span>:
            </p>

        </div>
        <div class="donations-info">
            <div class="donations-header" style="display:none;">
                <p>
                    SI LO DESEA PUEDE HACER UNA DONACIÓN MEDIANTE TRANSFERENCIA
                    BANCARIA
                </p>
            </div>
            <div class="foundations">
                <div class="friends">
                    <div class="friends-image">
                        <img src="~/assets/img/foundations/fundacion-tacumi.svg" width="121" height="51" />
                    </div>
                    <div class="friends-text">
                        <h4>Fundación Tacumi</h4>
                        <div class="friends-info">
                            <p>
                                <span style="font-weight: 500">IBAN</span> ES08 2080 1600 0130 4001 8218
                            </p>
                            <p>
                                <span style="font-weight: 500">CONCEPTO</span>
                                DONACIÓN SOLIDARITY XMAS TREE FUNDACIÓN TACUMI
                            </p>
                            <p style="text-transform: uppercase;">
                                Si lo desea puede hacer una donación mediante transferencia bancaria.
                            </p>
                        </div>
                        <p class="friends-description">
                            Promueve la integración plena de niños con discapacidad intelectual en centros educativos
                            ordinarios, trabajando con el alumnado, las familias y los colegios. Con el proyecto “Aulas
                            Itinerantes”, profesionales especializados trabajan dentro del aula ordinaria, al lado del
                            alumno con necesidades específicas y junto al resto de compañeros, para brindarle todo el
                            apoyo educativo necesario.
                        </p>
                        <Link :href="'https://fundaciontacumi.org/'" class="friends-text-link">más información Fundación
                        Tacumi</Link>
                    </div>
                </div>
                <div class="friends">
                    <div class="friends-image">
                        <img src="~/assets/img/foundations/fundacion-dadoris.svg" width="121" height="51" />
                    </div>
                    <div class="friends-text">
                        <h4>Fundación Dádoris</h4>
                        <div class="friends-info">
                            <p>
                                <span style="font-weight: 500">IBAN</span> ES13 2080 1600 0430 4001 8466
                            </p>
                            <p>
                                <span style="font-weight: 500">CONCEPTO</span>
                                DONACÓN SOLIDARITY XMAS TREE FUNDACIÓN DÁDORIS
                            </p>
                            <p style="text-transform: uppercase;">
                                Si lo desea puede hacer una donación mediante transferencia bancaria.
                            </p>
                        </div>
                        <p class="friends-description">
                            La Fundación Dadoris apoya a jóvenes que han obtenido excelentes resultados en bachillerato,
                            pero no tienen recursos económicos suficientes para acceder a estudios universitarios porque
                            pertenecen a familias que viven bajo el umbral de pobreza 1, el más bajo en nuestro país.
                            Mediante premios económicos, estos estudiantes pueden cubrir los gastos derivados de sus
                            estudios universitarios, y de cursos de idiomas y otras actividades complementarias para su
                            formación.
                        </p>
                        <Link :href="'https://fundaciondadoris.org/'" class="friends-text-link">más información
                        Fundación Dádoris</Link>
                    </div>
                </div>
                <div class="friends">
                    <div class="friends-image">
                        <img src="~/assets/img/foundations/fundacion-alas.svg" width="121" height="51" />
                    </div>
                    <div class="friends-text">
                        <h4>Fundación Alas</h4>
                        <div class="friends-info">
                            <p>
                                <span style="font-weight: 500">IBAN</span> ES37 2080 1600 0830 4001 8226
                            </p>
                            <p>
                                <span style="font-weight: 500">CONCEPTO</span>
                                DONACÓN SOLIDARITY XMAS TREE FUNDACIÓN ALAS
                            </p>
                            <p style="text-transform: uppercase;">
                                Si lo desea puede hacer una donación mediante transferencia bancaria.
                            </p>
                        </div>
                        <p class="friends-description">
                            A través de diversos proyectos y recursos: hogares y viviendas tuteladas, formación
                            académica y ocupacional y formación en actividades cotidianas del día a día, acompañan a
                            personas adultas con discapacidad intelectual para que puedan llegar a lo más autónomas
                            posibles dentro de sus posibilidades, ayudándoles a tener un vida digna, segura y feliz.
                        </p>
                        <Link :href="'https://alasmadrid.org/'" class="friends-text-link">más información Fundación Alas
                        </Link>
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
            width: 900px;

            @media (max-width: $default-breakpoint) {
                width: 100%;
                font-size: $font-size-large-medium;
                text-align: center;
                padding-right: 25px;
                padding-left: 25px;
            }
        }

        .texto-oportunidades {
            margin: 0;
            font-weight: 250;
            font-size: $font-size-medium;
            font-style: normal;
            line-height: 1.2em;
            width: 900px;
            text-transform: uppercase;
        }

        .videos {
            width: 900px;
            margin-bottom: 50px;
            margin-top: 50px;

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
        justify-content: space-between;
        width: 100%;
        margin-top: 100px;

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
                line-height: 30px;
                /* 136.364% */
                letter-spacing: 1.76px;
                width: 80%;
                margin-bottom: 70px;

                @media (max-width: $default-breakpoint) {
                    width: 90%;
                    font-size: $font-size-medium-mobile;
                    font-style: normal;
                    font-weight: 300;
                    line-height: 24px;
                    /* 133.333% */
                    letter-spacing: 1.44px;

                    margin-left: auto;
                    margin-right: auto;
                }
            }
        }

        .foundations {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: start;
            gap: 3em;
            width: 900px;

            @media (max-width: $default-breakpoint) {
                margin: 0;
                width: 100%;
            }

            .friends {
                display: flex;
                justify-content: space-between;
                align-items: center;
                width: 100%;
                gap: 24px;

                @media (max-width: $default-breakpoint) {
                    flex-direction: column;
                    padding: 0;
                    align-items: center;
                    justify-content: center;
                }

                .friends-image {
                    width: 100%;
                    height: 100%;
                    max-width: 250px;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: start;

                    @media (max-width: $default-breakpoint) {
                        align-items: center;
                        justify-content: center;
                    }
                }

                .friends-image {
                    img {
                        width: auto;
                        height: auto;
                        object-fit: contain;
                    }
                }

                .friends-info {
                    display: flex;
                    flex-direction: column;
                    flex: 1;
                    gap: 8px;
                }

                .friends-text {
                    display: flex;
                    flex-direction: column;
                    flex: 1;
                    gap: 8px;
                    max-width: 70%;

                    @media (max-width: $default-breakpoint) {
                        text-align: center;
                        display: flex;
                        flex-direction: column;
                        align-items: center;
                        gap: 15px;
                        margin-top: 0;
                        max-width: 100%;
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
                        line-height: 30px;
                        /* 136.364% */
                        letter-spacing: 1.76px;
                        text-transform: uppercase;
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
        }
    }
}
</style>
