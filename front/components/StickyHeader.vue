<template>
    <div
        ref="header"
        class="sticky-header-container"
        :class="state.sticky && 'sticky'"
    >
        <div class="navbar">
            <img
                @click="goToHome"
                class="header-img"
                width="80"
                height="80"
                src="~/assets/img/logo-header.svg"
            />
            <RegistrationButton
                v-if="withRegistrationButton"
                @handle-click="gotToForm"
                :invert-display-behavior="true"
                >Regístrese</RegistrationButton
            >
            <div
                class="header-links"
                :class="state.showMobileMenu ? 'open-menu' : 'closed-menu'"
            >
                <a
                    v-if="props.withFoundationsLink"
                    @click="scrollIntoElement('foundations', 100)"
                    >FUNDACIONES BENEFICIARIAS</a
                >
                <a @click="scrollIntoElement('partners', 100)">PARTNERS</a>
                <RegistrationButton
                    v-if="withRegistrationButton"
                    @handle-click="gotToForm"
                    >Regístrese</RegistrationButton
                >
            </div>
            <img
                @click="showMobileMenu"
                width="32"
                height="16"
                src="~/assets/img/hamburger-menu.svg"
                class="hamburger-menu"
            />
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, onBeforeMount, onBeforeUnmount, reactive } from "vue";
import RegistrationButton from "~/components/generic/RegistrationButton.vue";

const header = ref(null);

const state = reactive({
    sticky: false,
    showMobileMenu: false,
    limitPosition: 0,
});

// props
const props = defineProps({
    withRegistrationButton: {
        type: Boolean,
        default: false,
    },
    withFoundationsLink: {
        type: Boolean,
        default: true,
    },
});

function handleScroll() {
    if (
        window.scrollY > header.value.offsetTop &&
        window.scrollY > state.limitPosition
    ) {
        state.sticky = true;
    } else {
        state.sticky = false;
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

function goToHome() {
    window.location.href = "/";
}

function showMobileMenu() {
    state.showMobileMenu = !state.showMobileMenu;
}

onBeforeMount(() => {
    window.addEventListener("scroll", handleScroll);
});

onMounted(() => {
    state.limitPosition = header.value.offsetTop;
});

onBeforeUnmount(() => {
    window.removeEventListener("scroll", handleScroll);
});

// function to redirect to /form
function gotToForm() {
    // recover the current url and redirect to /form
    const currentUrl = window.location.href;
    // concatenate the /form to the current url considering the last slash
    const formUrl =
        currentUrl[currentUrl.length - 1] === "/" ? "form" : "/form";
    // redirect to /form
    window.location.href = `${currentUrl}${formUrl}`;
}
</script>

<style lang="scss">
@import "assets/css/variables";

.sticky {
    position: fixed;
    left: 0;
    top: 0;
    width: 100%;
    -webkit-backface-visibility: hidden;
}

.sticky + .landing-container-2 {
    padding-top: 100px;
}

.sticky + .landing-container-confirmation {
    padding-top: 100px;
}

.sticky + .sxt-container-registration-form--main {
    padding-top: 100px;
}

.sticky-header-container {
    z-index: 2;
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
        color: white;
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

            &:hover,
            &:focus {
                color: $font-tertiary;
            }
        }
    }
}

.handle-form-button {
    display: none;
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
        margin-right: 0;
        max-width: 44px !important;
    }

    .handle-form-button {
        display: flex;
        align-items: flex-start;
        gap: 32px;
        justify-content: center;
        background-color: $primary;
    }
}
</style>
