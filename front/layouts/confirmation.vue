<template>
    <div class="sxt-container-registration-form">
        <main class="sxt-container-registration-form--main">
            <slot></slot>
        </main>
    </div>
</template>

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

    .sxt-container-registration-form--main {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
}
</style>
