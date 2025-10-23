<template>
    <div class="brands-carousel-container">
        <p>
            LAS GRANDES MARCAS QUE PARTICIPAN EN 2025 EN ESTA INICIATIVA
            SOLIDARIA ÚNICA SON
        </p>
        <div class="brands-carousel--carousel">
            <CustomCarousel :pictures="brands"></CustomCarousel>
        </div>
    </div>
</template>

<script setup>
const brands = [
    ["/img/brands/cartier.svg", ""],
    ["/img/brands/chaumet.svg", ""],
    ["/img/brands/chopard.svg", ""],
    ["/img/brands/giorgio-armani.svg", ""],
    ["/img/brands/hermes.svg", ""],
    ["/img/brands/iwc.svg", ""],
    ["/img/brands/JLC.svg", ""],
    ["/img/brands/loewe.svg", ""],
    ["/img/brands/Valmont.svg", ""],
    ["/img/brands/Ralph-Lauren.svg", ""],
    ["/img/brands/stefano.svg", ""],
    ["/img/brands/suarez.svg", ""],
    ["/img/brands/TOD.svg", ""],
    ["/img/brands/Zimmermann.svg", ""],
];

import CustomCarousel from "/components/CustomCarousel.vue";
</script>

<style lang="scss" scoped>
@import "assets/css/variables";

.brands-carousel-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: 72px;

    @media (max-width: $default-breakpoint) {
        gap: 48px;
    }

    .brands-carousel--carousel {
        width: 90%;
    }

    p {
        font-size: $font-size-medium;
        width: 59%;
        font-style: normal;
        font-weight: 300;
        line-height: 30px;
        /* 136.364% */
        letter-spacing: 1.76px;
        margin: 0;

        @media (max-width: $default-breakpoint) {
            width: 100%;
            font-size: $font-size-medium-mobile;
            line-height: 24px;
            /* 133.333% */
            letter-spacing: 1.44px;
            padding-left: 25px;
            padding-right: 25px;
        }
    }
}
</style>
