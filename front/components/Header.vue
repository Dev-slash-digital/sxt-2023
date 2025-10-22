<template>
    <div class="above-the-fold">
        <img
            class="logo"
            src="~/assets/img/logo-above-the-fold.svg"
            width="192"
            height="180"
            alt="Solidarity Xmas Tree"
        />
        <div class="line"></div>
        <div class="scroll" @click="scrollToMain">SCROLL</div>
    </div>

    <div
        ref="header"
        class="header-container"
        :class="state.sticky && 'sticky'"
    >
        <div class="navbar">
            <img
                @click="scrollToStart"
                class="header-img"
                width="80"
                height="80"
                src="~/assets/img/logo-header.svg"
            />

            <div
                class="header-links"
                :class="state.showMobileMenu ? 'open-menu' : 'closed-menu'"
            >
                <a @click="scrollIntoElement('weare', 50)">¿QUIÉNES SOMOS?</a>
                <a @click="scrollIntoElement('foundations', 100)"
                    >FUNDACIONES BENEFICIARIAS</a
                >
                <a @click="scrollIntoElement('partners', 100)">PARTNERS</a>
            </div>
            <img
                @click="showMobileMenu"
                src="~/assets/img/hamburger-menu.svg"
                width="32"
                height="16"
                class="hamburger-menu"
            />
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, onBeforeMount, onBeforeUnmount, reactive } from "vue";

const header = ref(null);

let onScroll = null;
let ticking = false;

const state = reactive({
    sticky: false,
    showMobileMenu: false,
    limitPosition: 0,
    logosAligned: false,
});

if (process.client) {
    // eslint-disable-next-line nuxt/no-globals-in-created
    const win = window;
    // eslint-disable-next-line nuxt/no-globals-in-created
    const doc = document;

    const raf =
        win.requestAnimationFrame ||
        win.mozRequestAnimationFrame ||
        win.webkitRequestAnimationFrame ||
        win.msRequestAnimationFrame;

    let lineEl;
    let scrollTextEl;
    let logoEl;
    let logoPlaceholderEl;

    onScroll = function () {
        if (!ticking) {
            raf(() => {
                if (!lineEl)
                    lineEl = doc.querySelector(".above-the-fold .line");
                if (!scrollTextEl)
                    scrollTextEl = doc.querySelector(".above-the-fold .scroll");
                if (!logoEl)
                    logoEl = doc.querySelector(".above-the-fold .logo");
                if (!logoPlaceholderEl)
                    logoPlaceholderEl = doc.querySelector("#weare");

                const y = win.scrollY;
                const avail = win.screen.availHeight;
                const { offsetTop } = logoPlaceholderEl;
                const minScale = 0.55;
                const screenWidth = win.screen.availWidth;
                lineEl.style.opacity = y < 10 ? 1 : 0;
                scrollTextEl.style.opacity = y < 10 ? 1 : 0;

                const rectLogoEl = logoEl.getBoundingClientRect();
                const rectlogoPlaceholedEl =
                    logoPlaceholderEl.getBoundingClientRect();

                const threshold = screenWidth < 767 ? -51 : 3;

                const condition =
                    rectlogoPlaceholedEl.top +
                        rectlogoPlaceholedEl.height / 2 -
                        (rectLogoEl.top + rectLogoEl.height / 2) >
                    threshold;

                logoEl.style.top = y * 0.8 + "px";
                if (condition) {
                    if (state.logosAligned) state.logosAligned = false;
                    if (logoEl.style.opacity == 0) {
                        logoEl.style.opacity = 1;
                    }
                    const advancement = y / avail;
                    let scaleLevel = 1 - advancement / 1.7;
                    if (scaleLevel < minScale) scaleLevel = 0.55;
                    logoEl.style.transform = `scale(${Math.min(
                        scaleLevel,
                        1
                    )})`;

                    if (logoPlaceholderEl.style.opacity == 1) {
                        logoPlaceholderEl.style.opacity = 0;
                    }
                } else {
                    if (!state.logosAligned) state.logosAligned = true;
                    if (logoPlaceholderEl.style.opacity == 0) {
                        logoPlaceholderEl.style.opacity = 1;
                    }
                    if (logoEl.style.opacity == 1) {
                        logoEl.style.opacity = 0;
                    }
                }

                ticking = false;
            });
        }
        ticking = true;
    };
    win.addEventListener("scroll", onScroll, false);
    setTimeout(() => onScroll());
}

function handleScroll() {
    if (process.client) {
        let mainHeaderEl;
        if (!mainHeaderEl)
            mainHeaderEl = document.querySelector(".header-container");

        mainHeaderEl.classList.toggle("active", state.logosAligned);

        if (
            window.scrollY > header.value.offsetTop &&
            window.scrollY > state.limitPosition
        ) {
            state.sticky = true;
        } else {
            state.sticky = false;
        }
    }
}

function scrollIntoElement(id, offset) {
    if (state.showMobileMenu) state.showMobileMenu = false;
    const element = document.getElementById(id);
    const rect = element.getBoundingClientRect();
    window.scrollTo({
        top: rect.top + window.scrollY - offset,
        behavior: "smooth",
    });
}

function scrollToStart() {
    window.scrollTo({ top: 0, left: 0, behavior: "smooth" });
}

function showMobileMenu() {
    state.showMobileMenu = !state.showMobileMenu;
}
function scrollToMain() {
    scrollIntoElement("weare", 50);
}

onBeforeMount(() => {
    window.addEventListener("scroll", handleScroll);
});

onMounted(() => {
    state.limitPosition = header.value.offsetTop;
});

onBeforeUnmount(() => {
    window.removeEventListener("scroll", handleScroll);
    window.removeEventListener("scroll", onScroll);
});
</script>

<style lang="scss">
@import "assets/css/variables";
.above-the-fold {
    position: relative;
    background-color: $primary;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    background-image: url("~/assets/img/background-noise-above-the-fold.png");
    user-select: none;
    background-blend-mode: hard-light;

    img {
        width: 192px;
        position: relative;
        z-index: 3;
        @media (max-width: $mobile-width) {
            padding-bottom: 200px;
        }
    }

    .line {
        position: absolute;
        width: 1px;
        bottom: 118px;
        left: 50%;
        left: calc(50% - 1px);
        background-color: $above-the-fold-color;
        animation: scroll-line 1.5s infinite;
        @media (max-width: $mobile-width) {
            margin-bottom: 60px;
        }
    }

    .scroll {
        position: absolute;
        transform: rotate(-90deg);
        color: $above-the-fold-color;
        bottom: 48px;
        text-transform: uppercase;
        cursor: pointer;
        letter-spacing: 2px;
        z-index: 4;

        @media (max-width: $mobile-width) {
            padding-left: 120px;
        }
    }
}

.sticky {
    position: fixed;
    left: 0;
    top: 0;
    width: 100%;
    -webkit-backface-visibility: hidden;
}

.sticky + .sxt-container--main {
    padding-top: 100px;
}

.header-container {
    z-index: 2;
    transition: 0.7s all;
    opacity: 0;
    visibility: hidden;

    &.active {
        opacity: 1;
        visibility: visible;
        top: 0;
    }
}

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: $primary;
    width: 100%;
    padding: 16px 80px;

    .hamburger-menu {
        width: 100%;
        height: auto;
        max-width: 32px;
        cursor: pointer;
        color: $text-color-secondary;
        display: none;
    }

    .header-img {
        width: 100%;
        max-width: 80px;
        height: auto;
        cursor: pointer;
    }

    .header-links {
        display: flex;
        align-items: flex-start;
        gap: 32px;
        justify-content: center;
        background-color: $primary;

        a {
            margin: auto;
            padding: 10px 0px;
            font-size: $font-size-small;
            text-decoration: none;
            color: $text-color-secondary;
            transition: 0.3s color;
            cursor: pointer;

            &:hover,
            &:focus {
                color: $font-tertiary;
            }
        }
    }
}

@media screen and (max-width: $default-breakpoint) {
    .navbar {
        position: relative;
        padding: 30px 0px;
        gap: 10px;
    }
    .open-menu {
        opacity: 1;
        visibility: visible;
    }
    .closed-menu {
        opacity: 0;
        visibility: hidden;
    }

    .header-links {
        top: 98%;
        right: 0;
        gap: 16px !important;
        flex-direction: column;
        position: absolute;
        padding: 16px;

        transition: all 0.2s ease-out;
    }

    .hamburger-menu {
        display: block !important;
        margin-right: 37px;
    }

    .header-img {
        margin-left: 37px;
        max-width: 44px !important;
    }
}
</style>
