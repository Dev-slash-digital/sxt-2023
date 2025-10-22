<template>
    <a
        @click="handleClick"
        :class="
            props.invertDisplayBehavior
                ? 'button-container-inverted-behavior'
                : 'button-container'
        "
    >
        <div class="button-wrap">
            <div class="button">
                <p class="button-text"><slot></slot></p>
                <svg viewBox="0 0 15 15" xmlns="http://www.w3.org/2000/svg">
                    <g clip-path="url(#clip0_695_7510)">
                        <path
                            d="M9.72888 3.33337V3.5816L12.6694 7.1277H0V7.87238H12.6382L9.72888 11.4362V11.6667L15.0156 7.67735V7.305L9.72888 3.33337Z"
                        />
                    </g>
                    <defs>
                        <clipPath id="clip0_695_7510">
                            <rect
                                width="15"
                                height="8.33333"
                                fill="white"
                                transform="translate(0 3.33337)"
                            />
                        </clipPath>
                    </defs>
                </svg>
            </div>
        </div>
    </a>
</template>

<script setup>
const emit = defineEmits(["handleClick"]);

// props
const props = defineProps({
    invertDisplayBehavior: {
        type: Boolean,
        default: false,
    },
});

function handleClick() {
    emit("handleClick");
}
</script>

<style lang="scss" scoped>
@import "assets/css/variables";

.button-container {
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 8px;
    cursor: pointer;

    .button-wrap {
        display: flex;
        gap: 8px;
        color: $register-button-text;
        background: $register-button-bg;

        transition:
            0.3s color,
            0.3s fill,
            0.3s border-color;

        .button {
            display: flex;
            flex-direction: row;
            align-items: center;
            gap: 8px;
            padding: 10px 16px 8px 16px;
            background: $register-button-bg;
        }

        .button-text {
            text-transform: uppercase;
            font-style: italic;
            font-weight: 400;
            font-size: 14px;
            line-height: normal;
            letter-spacing: 1.4px;
            margin: 0;
            padding: 0;
            text-align: left;
        }

        svg {
            width: 100%;
            height: auto;
            max-width: 15px;
            fill: $register-button-text;
        }

        &:focus,
        &:hover {
            color: white;

            svg {
                fill: white;
            }
        }
    }
}

.button-container-inverted-behavior {
    display: none;
    flex-direction: row;
    align-items: center;
    gap: 8px;
    cursor: pointer;

    .button-wrap {
        display: flex;
        gap: 8px;
        color: $register-button-text;
        background: $register-button-bg;

        transition:
            0.3s color,
            0.3s fill,
            0.3s border-color;

        .button {
            display: flex;
            flex-direction: row;
            align-items: center;
            gap: 8px;
            padding: 10px 16px 8px 16px;
            background: $register-button-bg;
        }

        .button-text {
            text-transform: uppercase;
            font-style: italic;
            font-weight: 400;
            font-size: 14px;
            line-height: normal;
            letter-spacing: 1.4px;
            margin: 0;
            padding: 0;
            text-align: left;
        }

        svg {
            width: 100%;
            height: auto;
            max-width: 15px;
            fill: $register-button-text;
        }

        &:focus,
        &:hover {
            color: white;

            svg {
                fill: white;
            }
        }
    }
}

@media screen and (max-width: $default-breakpoint) {
    .button-container {
        display: none;
    }
    .button-container-inverted-behavior {
        display: flex;
        flex-direction: row;
        align-items: center;
        gap: 8px;
        cursor: pointer;
    }
}
</style>
