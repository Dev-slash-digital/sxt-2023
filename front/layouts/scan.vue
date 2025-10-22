<template>
    <div class="sxt-container-scan">
        <main class="sxt-container-scan--main">
            <slot></slot>
        </main>
    </div>
</template>

<style lang="scss">
@import "assets/css/variables";

.sxt-container-scan {
    min-height: 100vh;
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 90px;

    .sxt-container-scan--main {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 90px;
    }
}
</style>
