<template>
    <div class="videos-container">
        <div class="main-video">
            <iframe :src="state.videoSource" title="YouTube video player" frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                allowfullscreen></iframe>
        </div>
    </div>
</template>

<script setup>
import { reactive, onMounted } from "vue";

const state = reactive({
    index: 0,
    videoSource:
        "https://www.youtube.com/embed/iiysyYpBHcI?si=B6Icguc9EmOR7Hcr",
});

function getVideoSource() {
    if (state.index === 0) {
        state.videoSource =
            "https://www.youtube.com/embed/iiysyYpBHcI?si=B6Icguc9EmOR7Hcr";
    } else {
        state.videoSource =
            "https://www.youtube.com/embed/iiysyYpBHcI?si=B6Icguc9EmOR7Hcr";
    }
}

function getFirstVideo() {
    if (state.index === 0) {
        state.videoSource =
            "https://www.youtube.com/embed/iiysyYpBHcI?si=B6Icguc9EmOR7Hcr";
    } else {
        state.videoSource =
            "https://www.youtube.com/embed/iiysyYpBHcI?si=B6Icguc9EmOR7Hcr";
    }
}

function changeVideoSource(index) {
    state.index = index;
    getVideoSource();
}

onMounted(() => {
    state.index = Math.round(Math.random());
    getFirstVideo();
});
</script>

<style lang="scss" scoped>
@import "assets/css/variables";

.videos-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 25px;

    @media (max-width: $default-breakpoint) {
        gap: 15px;
    }

    .main-video {
        width: 100%;

        iframe {
            aspect-ratio: 16 / 9;
            width: 100%;
        }
    }

    .videos {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 25px;

        @media (max-width: $default-breakpoint) {
            gap: 15px;
        }

        .friends,
        .mothers {
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 50%;

            p {
                margin-top: 10px;
                font-size: 14px;
                font-style: normal;
                font-weight: 400;
                line-height: normal;
                letter-spacing: 1.4px;
                padding: 0;
            }
        }

        img {
            width: 100%;
            height: auto;
            max-width: 304px;
            cursor: pointer;

            @media (max-width: $default-breakpoint) {
                max-width: 150px;
            }
        }

        img:not(.active) {
            opacity: 0.5;
        }
    }
}
</style>
