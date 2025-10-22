<template>
    <div class="sxt-container-check">
        <main class="sxt-container-check--main">
            <slot></slot>
        </main>
        <RegistrationFooter class="sxt-container-check--footer" />
    </div>
</template>

<script setup>
import RegistrationFooter from "../components/RegistrationFooter.vue";
</script>

<style lang="scss">
@import "assets/css/variables";

.sxt-container-check {
    min-height: 100vh;
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 90px;

    .sxt-container-check--main {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 32px;
        margin-top: 40px;
        margin-left: 25px;
        margin-right: 25px;
    }
}
</style>
