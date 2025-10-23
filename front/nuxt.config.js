import { envManager, defineModelWConfig } from "@model-w/preset-nuxt3";

const modelWConfig = envManager((env) => {
    return defineModelWConfig(env, {
        siteName: "Solidarity XMas Tree",
        head: {
            meta: [
                { charset: "utf-8" },
                {
                    name: "viewport",
                    content: "width=device-width, initial-scale=1",
                },
                { name: "format-detection", content: "telephone=no" },
                {
                    name: "description",
                    content:
                        "Únete a la Ruta Solidarity Xmas Tree y vive una experiencia única recorriendo las boutiques de las marcas de lujo más prestigiosas, donde podrás admirar y pujar por árboles de Navidad exclusivos. Todo lo recaudado se destina a Grandes Amigos y Mamás en Acción.",
                },
                {
                    name: "keywords",
                    content:
                        "Ruta Árboles de Navidad, subasta benéfica, lujo y solidaridad, evento exclusivo, Grandes Amigos, Mamás en Acción, marcas de lujo",
                },
            ],
            link: [
                {
                    rel: "shortcut icon",
                    type: "image/png",
                    href: "/img/fav-1.png",
                },
                {
                    rel: "icon",
                    type: "image/png",
                    href: "/img/fav-2.png",
                },
                {
                    rel: "canonical",
                    href: "https://www.tusitio.com/ruta-arboles-navidad-lujo",
                },
            ],
        },
        cmsAlias: "",
        runtimeConfig: {
            public: {
                baseURL:
                    process.env.NUXT_PUBLIC_BASE_URL || "http://localhost:3000",
                gtagId: process.env.GANALYTICS_TAG_ID,
            },
        },
    });
});

export default {
    ...modelWConfig,
    css: ["~/assets/css/main.scss"],
    nitro: {
        compressPublicAssets: true,
        publicAssets: [
            {
                baseURL: '/img',
                dir: 'public/img',
                maxAge: 60 * 60 * 24 * 7 // 7 days
            }
        ]
    },
    router: {
        options: {
            strict: false
        }
    }
};
