<template>
    <div class="videos-container">
        <div class="main-video">
            <div v-if="!state.isPlaying" class="video-preview" @click="playVideo">
                <img src="https://img.youtube.com/vi/iiysyYpBHcI/maxresdefault.jpg" alt="Video preview">
                <div class="play-button">
                    <svg height="100%" version="1.1" viewBox="0 0 68 48" width="100%">
                        <path d="M66.52,7.74c-0.78-2.93-2.49-5.41-5.42-6.19C55.79,.13,34,0,34,0S12.21,.13,6.9,1.55 C3.97,2.33,2.27,4.81,1.48,7.74C0.06,13.05,0,24,0,24s0.06,10.95,1.48,16.26c0.78,2.93,2.49,5.41,5.42,6.19 C12.21,47.87,34,48,34,48s21.79-0.13,27.1-1.55c2.93-0.78,4.64-3.26,5.42-6.19C67.94,34.95,68,24,68,24S67.94,13.05,66.52,7.74z" fill="#f00"></path>
                        <path d="M 45,24 27,14 27,34" fill="#fff"></path>
                    </svg>
                </div>
            </div>
            <iframe v-else src="https://www.youtube.com/embed/iiysyYpBHcI?si=B6Icguc9EmOR7Hcr&autoplay=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
        </div>
    </div>
</template>

<script setup>
import { reactive } from "vue";

const state = reactive({
    isPlaying: false,
});

function playVideo() {
    state.isPlaying = true;
}
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
        position: relative;

        iframe {
            aspect-ratio: 16 / 9;
            width: 100%;
        }

        .video-preview {
            position: relative;
            width: 100%;
            aspect-ratio: 16 / 9;
            cursor: pointer;
            overflow: hidden;

            img {
                width: 100%;
                height: 100%;
                object-fit: cover;
            }

            .play-button {
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                width: 68px;
                height: 48px;
                transition: transform 0.2s;

                &:hover {
                    transform: translate(-50%, -50%) scale(1.1);
                }
            }
        }
    }
}
</style>
