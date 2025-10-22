<template>
    <div class="videos-container">
        <div class="main-video">
            <iframe
                :src="state.videoSource"
                title="YouTube video player"
                frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                allowfullscreen
            ></iframe>
        </div>
        <div class="videos">
            <div class="friends">
                <img
                    @click="changeVideoSource(0)"
                    :class="state.index === 0 ? 'active' : ''"
                    src="~/assets/img/videos/Friends.png"
                />
                <p>GRANDES AMIGOS</p>
            </div>
            <div class="mothers">
                <img
                    @click="changeVideoSource(1)"
                    :class="state.index === 1 ? 'active' : ''"
                    src="~/assets/img/videos/Mothers.png"
                />
                <p>MAMÁS EN ACCIÓN</p>
            </div>
        </div>
    </div>
</template>

<script setup>
import { reactive, onMounted } from "vue";

const state = reactive({
    index: 0,
    videoSource:
        "https://www.youtube.com/embed/62z5NpOSJeU?si=8g_Ae3eqZUpnScfV&amp;controls=0&rel=0&autoplay=1",
});

function getVideoSource() {
    if (state.index === 0) {
        state.videoSource =
            "https://www.youtube.com/embed/62z5NpOSJeU?si=8g_Ae3eqZUpnScfV&amp;controls=0&rel=0&autoplay=1";
    } else {
        state.videoSource =
            "https://www.youtube.com/embed/8L2C95OoH3w?si=s1y-15NOjtK_pNJx&amp;controls=0&rel=0&autoplay=1";
    }
}

function getFirstVideo() {
    if (state.index === 0) {
        state.videoSource =
            "https://www.youtube.com/embed/62z5NpOSJeU?si=8g_Ae3eqZUpnScfV&amp;controls=0&rel=0";
    } else {
        state.videoSource =
            "https://www.youtube.com/embed/8L2C95OoH3w?si=s1y-15NOjtK_pNJx&amp;controls=0&rel=0";
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
