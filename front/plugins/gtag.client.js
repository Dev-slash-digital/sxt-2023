export default defineNuxtPlugin((nuxtApp) => {
    function gtag() {
        window.dataLayer.push(arguments);
    }

    window.dataLayer = window.dataLayer || [];

    gtag("js", new Date());
    gtag("config", "G-HMTFCST1GY");

    useHead({
        script: [
            {
                src: "https://www.googletagmanager.com/gtag/js?id=G-HMTFCST1GY",
                async: true,
            },
        ],
    });
});
