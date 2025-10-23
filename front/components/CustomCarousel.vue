<template>
    <div class="carousel-wrapper">
        <div class="prev" :class="[props.lightButtons ? 'light-buttons' : 'dark-buttons']" @click="prev">
            <svg width="60" height="40" viewBox="0 0 60 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path
                    d="M59.0496 20C59.0496 30.7732 50.3839 39.5 39.7023 39.5C29.0207 39.5 20.355 30.7732 20.355 20C20.355 9.22683 29.0207 0.5 39.7023 0.5C50.3839 0.5 59.0496 9.22683 59.0496 20Z"
                    stroke="#09454F" />
                <path
                    d="M0.64637 19.6464C0.451107 19.8417 0.451107 20.1583 0.64637 20.3535L3.82835 23.5355C4.02361 23.7308 4.34019 23.7308 4.53546 23.5355C4.73072 23.3403 4.73072 23.0237 4.53546 22.8284L1.70703 20L4.53546 17.1716C4.73072 16.9763 4.73072 16.6597 4.53546 16.4645C4.3402 16.2692 4.02361 16.2692 3.82835 16.4645L0.64637 19.6464ZM40.6946 19.5L0.999924 19.5L0.999924 20.5L40.6946 20.5L40.6946 19.5Z"
                    fill="#09454F" />
            </svg>
        </div>

        <Carousel ref="myCarousel" :wrap-around="true" :items-to-show="1" :breakpoints="state.breakpoints"
            :autoplay="5000" :transition="1000">
            <Slide :class="{ 'trees-slide': props.treesCarousel }" v-for="(value, index) in props.pictures"
                :key="index">
                <div class="slider-img">
                    <img class="picture-logos" :class="{ 'picture-trees': props.treesCarousel }" :src="value[0]" />
                    <p v-if="value[1]">{{ value[1] }}</p>
                </div>
            </Slide>
        </Carousel>

        <div class="next" :class="[props.lightButtons ? 'light-buttons' : 'dark-buttons']" @click="next">
            <svg width="60" height="40" viewBox="0 0 60 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path
                    d="M0.950363 20C0.950363 30.7732 9.61606 39.5 20.2977 39.5C30.9793 39.5 39.645 30.7732 39.645 20C39.645 9.22683 30.9793 0.5 20.2977 0.5C9.61606 0.5 0.950363 9.22683 0.950363 20Z"
                    stroke="#09454F" />
                <path
                    d="M59.3535 19.6464C59.5488 19.8417 59.5488 20.1583 59.3535 20.3535L56.1715 23.5355C55.9763 23.7308 55.6597 23.7308 55.4644 23.5355C55.2692 23.3403 55.2692 23.0237 55.4644 22.8284L58.2928 20L55.4644 17.1716C55.2692 16.9763 55.2692 16.6597 55.4644 16.4645C55.6597 16.2692 55.9763 16.2692 56.1715 16.4645L59.3535 19.6464ZM19.3053 19.5L59 19.5L59 20.5L19.3053 20.5L19.3053 19.5Z"
                    fill="#09454F" />
            </svg>
        </div>
    </div>
    <div class="mobile-buttons">
        <div class="prev" :class="[props.lightButtons ? 'light-buttons' : 'dark-buttons']" @click="prev">
            <svg width="60" height="40" viewBox="0 0 60 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path
                    d="M59.0496 20C59.0496 30.7732 50.3839 39.5 39.7023 39.5C29.0207 39.5 20.355 30.7732 20.355 20C20.355 9.22683 29.0207 0.5 39.7023 0.5C50.3839 0.5 59.0496 9.22683 59.0496 20Z"
                    stroke="#09454F" />
                <path
                    d="M0.64637 19.6464C0.451107 19.8417 0.451107 20.1583 0.64637 20.3535L3.82835 23.5355C4.02361 23.7308 4.34019 23.7308 4.53546 23.5355C4.73072 23.3403 4.73072 23.0237 4.53546 22.8284L1.70703 20L4.53546 17.1716C4.73072 16.9763 4.73072 16.6597 4.53546 16.4645C4.3402 16.2692 4.02361 16.2692 3.82835 16.4645L0.64637 19.6464ZM40.6946 19.5L0.999924 19.5L0.999924 20.5L40.6946 20.5L40.6946 19.5Z"
                    fill="#09454F" />
            </svg>
        </div>
        <div class="next" :class="[props.lightButtons ? 'light-buttons' : 'dark-buttons']" @click="next">
            <svg width="60" height="40" viewBox="0 0 60 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path
                    d="M0.950363 20C0.950363 30.7732 9.61606 39.5 20.2977 39.5C30.9793 39.5 39.645 30.7732 39.645 20C39.645 9.22683 30.9793 0.5 20.2977 0.5C9.61606 0.5 0.950363 9.22683 0.950363 20Z"
                    stroke="#09454F" />
                <path
                    d="M59.3535 19.6464C59.5488 19.8417 59.5488 20.1583 59.3535 20.3535L56.1715 23.5355C55.9763 23.7308 55.6597 23.7308 55.4644 23.5355C55.2692 23.3403 55.2692 23.0237 55.4644 22.8284L58.2928 20L55.4644 17.1716C55.2692 16.9763 55.2692 16.6597 55.4644 16.4645C55.6597 16.2692 55.9763 16.2692 56.1715 16.4645L59.3535 19.6464ZM19.3053 19.5L59 19.5L59 20.5L19.3053 20.5L19.3053 19.5Z"
                    fill="#09454F" />
            </svg>
        </div>
    </div>
</template>

<script setup>
import "vue3-carousel/dist/carousel.css";
import { Carousel, Slide, Pagination, Navigation } from "vue3-carousel";
import { ref, onMounted, reactive } from "vue";
const myCarousel = ref(null);

// Props
const props = defineProps({
    pictures: {
        type: Array,
        default: [],
    },
    treesCarousel: {
        type: Boolean,
        default: false,
    },
    lightButtons: {
        type: Boolean,
        default: false,
    },
});

const state = reactive({
    breakpoints: {
        767: {
            itemsToShow: props.treesCarousel ? 3 : 1,
            snapAlign: "center",
            autoplay: props.treesCarousel ? 0 : 5000,
        },
    },
    carouselLoading: true,
});

function prev() {
    myCarousel.value.prev();
}
function next() {
    myCarousel.value.next();
}

onMounted(() => { });
</script>

<style scoped lang="scss">
@import "assets/css/variables";

.carousel-wrapper {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1em;

    .carousel {
        width: 100%;
    }

    .slider-img {
        max-width: 98%;
    }

    .trees-slide {
        padding-bottom: 4em;

        .slider-img {
            display: flex;
            flex-direction: column;
            align-items: center;
            position: relative;

            p {
                position: absolute;
                top: 100%;
                font-size: 10px;
                font-weight: 300;
                line-height: 14px;
                font-style: normal;
                margin-top: 5px;
            }

            .picture-trees {
                width: 85%;
                max-width: 800px;

                @media (max-width: $default-breakpoint) {
                    width: 80%;
                }
            }
        }

        &.carousel__slide--active .slider-img {
            img {
                width: 100%;
                max-width: 850px;

                @media (max-width: $default-breakpoint) {
                    width: 80%;
                }
            }

            p {
                font-size: 16px;
                line-height: 22px;
                letter-spacing: 0.32px;
            }
        }
    }

    .prev,
    .next {
        svg {
            width: 60px;
            cursor: pointer;

            @media (max-width: $default-breakpoint) {
                width: 40px;
            }

            path {
                transition: 0.3s fill;
            }
        }
    }
}

.mobile-buttons {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 32px;
    width: 100%;
    display: none;
    margin-top: 32px;

    .prev,
    .next {
        svg {
            width: 80px;
            cursor: pointer;

            path {
                transition: 0.3s fill;
            }
        }
    }
}

@media screen and (max-width: $default-breakpoint) {
    .mobile-buttons {
        display: flex;
    }

    .carousel-wrapper .prev,
    .carousel-wrapper .next {
        display: none;
    }
}

.dark-buttons {
    svg path {
        stroke: $text-color-flechas;
    }

    &:hover svg path {
        stroke: $text-color-flechas;
    }
}

.light-buttons {
    svg path {
        stroke: $text-color-flechas;
    }

    &:hover svg path {
        stroke: $text-color-flechas;
    }
}
</style>
