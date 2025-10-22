<template>
    <div class="sxt-container-registration-form">
        <div class="sxt-container-registration-form--header">
            <slot name="header"></slot>
            <StickyHeader :with-foundations-link="false" ref="header" />
            <main class="sxt-container-registration-form--main">
                <slot></slot>
            </main>
        </div>
        <RegistrationFooter class="sxt-container-registration--footer" />
    </div>
</template>

<script setup>
import RegistrationFooter from "../components/RegistrationFooter.vue";
import StickyHeader from "../components/StickyHeader.vue";
</script>

<style lang="scss">
@import "assets/css/variables";

.sxt-container-registration-form {
    min-height: 100vh;
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 100px;

    @media (max-width: $default-breakpoint) {
        gap: 112px;
    }

    .sxt-container-registration-form--header {
        .sxt-container-registration-form--main {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
    }
}
</style>
