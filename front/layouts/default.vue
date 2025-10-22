<template>
    <div class="sxt-container">
        <Header />
        <main class="sxt-container--main">
            <slot></slot>
        </main>
        <Footer class="sxt-container--footer" />
    </div>
</template>

<script setup>
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
</script>

<style lang="scss">
@import "assets/css/variables";

.sxt-container {
    min-height: 100vh;
    width: 100%;
    display: flex;
    flex-direction: column;

    .sxt-container--main {
        flex: 1;
        display: flex;
        flex-direction: column;
        align-items: center;
        z-index: 1;
        margin-top: 100px;

        @media (max-width: $default-breakpoint) {
            margin-top: 66px;
        }
    }
}
</style>
