<template>
    <div id="partners" class="footer-container">
        <div class="footer-partners">
            <p class="text-uppercase">NUESTROS COLABORADORES</p>
            <img src="/img/partners/Abanca.svg" width="186" height="67" style="display:none;" />
            <div class="footer-carousel">
                <CustomCarousel :light-buttons="true" :pictures="partnersPictures"></CustomCarousel>
            </div>
        </div>
        <div class="footer-info">
            <img class="footer-tree" src="~/assets/img/footer/tree.png" width="92" height="92" />
            <div class="footer-follow">
                <div class="follow-text">
                    <p class="footer-follow-text">¡SÍGANOS EN INSTAGRAM!</p>
                    <a href="https://www.instagram.com/solidarityxmastree/" target="_blank">
                        <Instagram></Instagram>
                    </a>
                </div>
                <hr class="footer-line" />
                <p class="info-together">info@togetherplus.es</p>
            </div>
            <div class="footer-rights">
                <span><span style="font-weight: 500; font-size: 14px">SOLIDARITY XMAX TREE</span>
                    is a registered idea and brand owned by TogetherPlus, S.L
                    All rights Reserved</span>
                <div class="footer-rights--partner">
                    <span>Partner tecnológico:
                        <a href="https://www.with-madrid.com" target="_blank">
                            www.with-madrid.com
                        </a></span>
                    <img class="partner-with" src="~/assets/img/footer/with.svg" width="36" height="14" />
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import CustomCarousel from "./CustomCarousel.vue";
import Instagram from "./svg/Instagram.vue";

const partnersPictures = [
    ["/img/partners/Abanca.svg", ""],
    ["/img/partners/BMW.svg", ""],
    ["/img/partners/Naturgy.svg", ""],
    ["/img/partners/Galeriascanalejas.svg", ""],
    ["/img/partners/Christies.svg", ""],
];

const randomPartnersPictures = [
    ["/img/partners/Nuevo.svg", ""],
    ["/img/partners/BANG-OLUFSEN.svg", ""],
];

shuffle(randomPartnersPictures);

partnersPictures.push(...randomPartnersPictures);

function shuffle(array) {
    let currentIndex = array.length;

    // While there remain elements to shuffle...
    while (currentIndex != 0) {
        // Pick a remaining element...
        let randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex--;

        // And swap it with the current element.
        [array[currentIndex], array[randomIndex]] = [
            array[randomIndex],
            array[currentIndex],
        ];
    }
}
</script>

<style lang="scss" scoped>
@import "assets/css/variables";

.footer-container {
    display: flex;
    flex-direction: column;
    align-items: center;

    background-color: $secondary;
    padding-top: 58px;
    gap: 40px;

    .footer-partners {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
        gap: 20px;
        color: $font-four;
        max-width: $max-width-lg;

        p {
            font-size: $font-size-medium;
            font-style: normal;
            font-weight: 300;
            line-height: 30px;
            /* 136.364% */
            letter-spacing: 1.76px;
            color: #094752;

            @media (max-width: $default-breakpoint) {
                font-size: $font-size-medium;
                line-height: 24px;
                /* 133.333% */
                letter-spacing: 1.44px;
            }
        }

        img {
            width: 100%;
            height: auto;
            max-width: 186px;
        }

        .footer-carousel {
            width: 80%;
            padding-top: 1em;
            padding-bottom: 2em;
            gap: 1em;
        }
    }

    .footer-info {
        background-color: $primary;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        width: 100%;
        gap: 8px;
        color: white;

        .footer-tree {
            width: 100%;
            max-width: 92px;
            height: auto;

            padding: 48px 0px;
        }

        .footer-follow {
            display: flex;
            padding: 24px 115px;
            flex-direction: column;
            align-items: center;
            gap: 23px;
            width: 100%;

            max-width: $max-width-lg;

            @media (max-width: $default-breakpoint) {
                padding: 24px 25px;
            }

            .follow-text {
                display: flex;
                flex-direction: column;
                gap: 8px;

                .footer-follow-text {
                    width: 100%;
                    font-weight: 300;
                    font-style: normal;
                    font-size: $font-size-medium;
                    line-height: 30px;
                    /* 136.364% */
                    letter-spacing: 1.76px;

                    @media (max-width: $default-breakpoint) {
                        font-size: $font-size-medium-mobile;
                        line-height: 24px;
                        /* 133.333% */
                        letter-spacing: 1.44px;
                    }
                }
            }
        }

        .footer-instagram {
            width: 100%;
            height: auto;
            max-width: 30px;
        }

        .footer-line {
            width: 100%;
        }

        .info-together {
            font-style: italic;
            font-size: 16px;
            font-weight: 300;
            line-height: 22px;
            /* 137.5% */
            letter-spacing: 0.32px;
        }

        .footer-rights {
            width: 100%;
            display: flex;
            align-items: center;
            padding: 26px 115px 24px 115px;
            justify-content: space-between;
            gap: 373px;

            font-size: 10px;
            line-height: 14px;
            gap: 1em;

            max-width: $max-width-lg;

            @media (max-width: $default-breakpoint) {
                flex-direction: column;
                align-items: center;
                gap: 16px;
                align-self: stretch;

                padding: 26px 25px 24px 25px;
            }

            .footer-rights--partner {
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 10px;
                line-height: 14px;
                font-weight: 300;

                span a {
                    color: white;
                }

                .partner-with {
                    width: 100%;
                    max-width: 35.76px;
                    height: auto;
                    margin-left: 8px;
                }
            }
        }
    }
}
</style>
