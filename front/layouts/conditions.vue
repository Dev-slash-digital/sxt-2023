<template>
    <div class="sxt-container-conditions">
        <main class="sxt-container-conditions--main">
            <slot></slot>
        </main>
    </div>
</template>

<style lang="scss">
@import "assets/css/variables";

.sxt-container-conditions {
    min-height: 100vh;
    width: 100%;
    display: flex;
    flex-direction: column;

    .sxt-container-conditions--main {
        flex: 1;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 33px;
        margin-bottom: 37px;
    }
}
</style>
