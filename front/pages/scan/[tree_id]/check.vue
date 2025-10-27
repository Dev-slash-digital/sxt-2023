<template>
    <div v-if="!state.isLoading" class="check-logo">
        <img :src="state.brandLogo" class="brand-logo" />
    </div>
    <div v-if="state.isLoading" class="loader-container">
        <div class="loading-dual-ring"></div>
    </div>
    <div class="check-content">
        <div class="content-text">
            <p>
                REGÍSTRESE PARA VALIDAR SU VISITA, TENER ACCESO A LA RUTA
                SOLIDARITY XMAS TREE Y ENTRAR EN EL SORTEO DE UNA EXPERIENCIA DE
                LUJO ÚNICA EN EL PALACIO ARRILUCE HOTEL EN GETXO
            </p>
        </div>
        <div class="content-form">
            <div v-if="state.noAccount" class="no-account">
                <p>
                    <span style="font-style: italic; font-weight: 500">No hay una cuenta registrada con este email
                    </span>
                    <br />
                    Si ya se ha registrado y no se le ha abierto el Mapa de la
                    Ruta Solidarity Xmas Tree compruebe que ha introducido
                    correctamente el email con el que se registró.
                </p>
                <p>
                    <span style="font-style: italic; font-weight: 500">Si aún no se ha registrado en la ruta <br />
                        Solidarity Xmas Tree,
                    </span>
                    <br />

                    pida el QR de acceso al personal de la boutique.
                </p>
            </div>
            <div class="form">
                <Input type="email" v-model="state.email" :placeholder="'Dirección de email'" :error="state.error" />
                <Button @handle-click="login">ACCEDER A LA RUTA</Button>
                <p class="server-error" v-if="state.serverError">
                    Se ha producido un error. Inténtelo de nuevo más tarde
                    gracias.
                </p>
            </div>
        </div>
        <YellowTree></YellowTree>
    </div>
</template>

<script setup>
import Input from "../../../components/generic/Input";
import Button from "../../../components/generic/Button";
import YellowTree from "../../../components/generic/YellowTree";

import { reactive, onBeforeMount } from "vue";
import API from "../../../utils/axios";

definePageMeta({
    layout: "check",
    middleware: "check",
});

const route = useRoute();

// State
const state = reactive({
    brandLogo: "",
    brandName: "Scan",
    noAccount: false,
    email: "",
    error: "",
    brandInfo: null,
    serverError: false,
    isLoading: true,
});

// Functions
async function getTreeInfo() {
    const tree_id = route.params.tree_id;
    try {
        const res = await API.get(`/back/api/brands/tree/${tree_id}/`);
        state.brandLogo = `/img/brands/${res.data.slug}.svg`;
        state.brandName = res.data.name;
    } catch (error) {
        navigateTo("/");
    }
}

async function login() {
    state.serverError = false;
    state.error = "";
    if (state.email === "") {
        state.error = "Debe ingresar su dirección de email";
    } else if (
        !/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(state.email)
    ) {
        state.error = "Debe ingrear una dirección de email válida";
    } else {
        try {
            const data = {
                email: state.email,
                password: "",
            };
            const res = await API.post("/back/api/user/me/", data);
            if (res.status === 200) {
                const emailCookie = useCookie("email", {
                    maxAge: 60 * 24 * 60 * 60,
                });
                emailCookie.value = res.data.email;
                const tree_id = route.params.tree_id;
                navigateTo(`/scan/${tree_id}/`);
            }
        } catch (error) {
            if (
                error.response &&
                error.response.status === 404 &&
                error.response.data?.detail === "Not found."
            ) {
                state.noAccount = true;
            } else {
                state.serverError = true;
            }
        }
    }
}

// Getters
const getters = {
    getName: () => {
        return state.brandName;
    },
};

onBeforeMount(async () => {
    await getTreeInfo();
    state.isLoading = false;
});

useHead({
    titleTemplate: () => {
        return `${getters.getName()} - Solidarity XMas Tree`;
    },
});
</script>

<style lang="scss" scoped>
@import "assets/css/variables";

.check-logo {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 32px;

    .brand-logo {
        width: 100%;
        height: auto;
    }
}

.check-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 90px;

    .content-text {
        display: flex;
        padding: 0px 25px;
        align-items: center;
        gap: 10px;
        align-self: stretch;

        p {
            text-align: center;
            font-size: 22px;
            font-style: normal;
            font-weight: 300;
            line-height: 30px;
            /* 136.364% */
            letter-spacing: 1.76px;
        }
    }

    .content-form {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 30px;
        align-self: stretch;

        .no-account {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 20px;
            text-align: center;

            p {
                font-size: 16px;
                line-height: 22px;
                letter-spacing: 0.32px;
            }
        }

        .form {
            display: flex;
            padding: 0px 25px;
            flex-direction: column;
            align-items: center;
            gap: 48px;
            align-self: stretch;
            max-width: 507px;
            width: 100%;

            .server-error {
                color: $error;
                text-align: center;
                font-size: $font-size-small-mobile;
                font-style: italic;
                font-weight: 300;
                line-height: 22px;
                /* 137.5% */
                letter-spacing: 0.32px;
            }
        }
    }
}

.loader-container {
    display: flex;
    align-items: center;
    justify-content: center;

    .loading-dual-ring::after {
        border: 6px solid $primary;
        border-color: $primary transparent $primary transparent;
    }
}
</style>
