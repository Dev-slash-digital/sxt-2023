<template>
    <div class="input-container">
        <p v-if="props.error" class="input-error">{{ props.error }}</p>
        <input :value="modelValue" :placeholder="props.placeholder"
            @input="$emit('update:modelValue', $event.target.value)" class="input"
            :class="props.error ? 'has-error' : ''" />
    </div>
</template>

<script setup>
const props = defineProps({
    error: {
        type: String,
        default: "",
    },
    placeholder: {
        type: String,
        default: "",
    },
    modelValue: String,
});

// We use the defineProps and defineEmits functions to make v-model work perfectly with this component.
defineEmits(["update:modelValue"]);
</script>

<style lang="scss">
@import "assets/css/variables";

.input-container {
    display: flex;
    flex-direction: column;
    width: 100%;

    .input-error {
        color: $error;
        font-size: $font-size-small-mobile;
        font-style: italic;
        font-weight: 300;
        line-height: 22px;
        /* 137.5% */
        letter-spacing: 0.32px;
        margin: 0;
    }

    .input {
        color: $text-color-primary;
        font-size: 16px;
        font-style: normal;
        font-weight: 300;
        line-height: 22px;
        /* 137.5% */
        letter-spacing: 0.32px;
        width: 100%;
        border: 0;
        border-bottom: 1px solid $text-color-primary;
        background: transparent;
        padding: 8px 0;
        transition: 0.3s all;

        &:focus {
            border-bottom-color: $secondary;
        }

        &:focus-visible {
            outline: -webkit-focus-ring-color auto 0;
        }

        /* &:hover, &:focus {
        outline: none;
        background: $t;
    } */

        &::-webkit-input-placeholder {
            color: $text-color-primary;
        }

        &::-moz-placeholder {
            color: $text-color-primary;
        }

        &::-ms-placeholder {
            color: $text-color-primary;
        }

        &::placeholder {
            color: $text-color-primary;
        }

        &.has-error {
            border-bottom-color: #de2006;
        }
    }
}
</style>
