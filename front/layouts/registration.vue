<template>
    <div class="sxt-container-registration">
        <main class="sxt-container-registration--main">
            <slot></slot>
        </main>
    </div>
</template>

<style lang="scss">
@import "assets/css/variables";

.sxt-container-registration {
    min-height: 100vh;
    width: 100%;
    display: flex;
    flex-direction: column;

    .sxt-container-registration--main {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
}
</style>
