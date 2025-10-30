<template>
    <div class="main-brand-container">
        <div class="brand-message-container">
            <p v-if="props.brandSlug !== 'sxt'">
                EL <span style="font-weight: 400; text-transform: uppercase">ÁRBOL DE NAVIDAD SOLIDARIO DE {{ brandName
                }}</span>, <span style="font-style: italic">estará</span> EXPUESTO <template
                    v-if="props.brandSlug === 'foundations'">en<br>
                    <span>{{ postalAddress }}</span><br>
                </template>
                <template v-else>EN SU BOUTIQUE DE<br>
                    <span>{{ postalAddress }}</span><br>
                </template>
                <span style="font-style: italic">del</span>
                <span style="font-weight: 400"> 18 <span style="font-style: italic">al</span> 24 DE NOVIEMBRE</span>
            </p>
            <div class="registration-process">
                <p class="registration-process-text">
                    ¡VISITE, VALIDE <span style="font-style: italic">y</span> GANE!
                </p>
            </div>
        </div>
    </div>
</template>

<script setup>
// props
const props = defineProps({
    postalAddress: {
        type: String,
        required: true,
    },
    brandName: {
        type: String,
        required: true,
    },
    brandSlug: {
        type: String,
        required: true,
    },
});
</script>

<style scoped lang="scss">
@import "assets/css/variables";

.main-brand-container {
    padding: 88px 0;
    background: $primary;
    color: white;
    width: 100%;
    display: flex;
    align-items: center;
    text-align: center;

    @media (max-width: $default-breakpoint) {
        padding: 70px 24px 70px 24px;
    }

    .brand-message-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        width: 100%;
        gap: 32px;

        p {
            font-size: $font-size-large-mobile;
            font-style: normal;
            font-weight: 250;
            line-height: 44px;
            margin: 0;
            max-width: 930px;
        }

        .registration-process {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;

            .registration-process-text {
                color: white;
                text-align: center;
                font-size: $font-size-large;
                font-weight: 500;
                line-height: 30px;
                letter-spacing: 1.8px;
                width: 100%;
                margin: 0;

                @media (max-width: $default-breakpoint) {
                    width: 100%;
                    font-size: $font-size-large-mobile;
                    line-height: 36px;
                }
            }
        }
    }
}
</style>
