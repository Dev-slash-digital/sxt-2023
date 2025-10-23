<template>
    <svg
        width="30"
        height="30"
        viewBox="0 0 30 30"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
    >
        <path
            class="circle"
            d="M15 30C23.2843 30 30 23.2843 30 15C30 6.71573 23.2843 0 15 0C6.71573 0 0 6.71573 0 15C0 23.2843 6.71573 30 15 30Z"
            fill="#08AEA2"
        />
        <g clip-path="url(#clip0_6_13)">
            <mask
                id="mask0_6_13"
                style="mask-type: luminance"
                maskUnits="userSpaceOnUse"
                x="6"
                y="6"
                width="18"
                height="18"
            >
                <path
                    d="M23.6842 6.31579H6.3158V23.6842H23.6842V6.31579Z"
                    fill="white"
                />
            </mask>
            <g mask="url(#mask0_6_13)">
                <path
                    d="M18.9799 6.79825H11.0201C9.901 6.80006 8.8282 7.24544 8.03684 8.03681C7.24548 8.82817 6.80009 9.90097 6.79828 11.0201V18.9799C6.80009 20.0991 7.24548 21.1719 8.03684 21.9632C8.82829 22.7546 9.90123 23.2 11.0205 23.2018H18.9795C20.0988 23.2 21.1718 22.7546 21.9632 21.9632C22.7546 21.1718 23.2001 20.0988 23.2018 18.9795V11.0205C23.2001 9.9012 22.7546 8.82826 21.9632 8.03681C21.1719 7.24544 20.0991 6.80006 18.9799 6.79825Z"
                    stroke="white"
                />
                <path
                    d="M19.9625 11.2782C20.6476 11.2782 21.2031 10.7227 21.2031 10.0376C21.2031 9.35242 20.6476 8.79698 19.9625 8.79698C19.2773 8.79698 18.7219 9.35242 18.7219 10.0376C18.7219 10.7227 19.2773 11.2782 19.9625 11.2782Z"
                    fill="white"
                />
            </g>
            <circle cx="15" cy="15" r="4.23684" stroke="white" />
        </g>

        <defs>
            <clipPath id="clip0_6_13">
                <rect
                    width="17.3684"
                    height="17.3684"
                    fill="white"
                    transform="translate(6.3158 6.31579)"
                />
            </clipPath>
        </defs>
    </svg>
</template>

<style lang="scss" scoped>
@import "assets/css/variables";

svg {
    width: 100%;
    height: auto;
    max-width: 30px;

    .circle:hover {
        fill: $font-tertiary;
    }
}
</style>
