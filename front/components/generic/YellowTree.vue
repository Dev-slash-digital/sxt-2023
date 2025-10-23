<template>
    <div class="yellow-tree-container">
        <hr />
        <img class="yellow-tree" src="~/assets/img/scan/red-tree.svg" width="16" height="18" />
        <hr />
    </div>
</template>

<style lang="scss" scoped>
@import "assets/css/variables";

.yellow-tree-container {
    display: flex;
    width: 100%;
    align-items: center;
    gap: 24px;

    hr {
        border: 0;
        border-top: 1px solid $yellow-tree-lines;
        width: 100%;
        height: 1px;
    }

    .yellow-tree {
        width: 100%;
        height: auto;
        max-width: 15.68px;
    }
}
</style>
