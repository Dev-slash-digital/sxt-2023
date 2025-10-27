<template>
    <div class="landing-container">
        <BigSXTLogo></BigSXTLogo>
        <p class="landing-comment">
            REGÍSTRESE Y ACCEDA A LA RUTA <br />
            SOLIDARITY XMAS TREE
        </p>
        <!-- create a registration form asking for an email and a checkbox -->
        <div class="landing-container--form">
            <form class="form">
                <div class="landing-container--form--elements">
                    <div class="landing-container--form--input">
                        <div v-if="errors.email" class="landing-container--form--error">
                            <p>{{ errors.email }}</p>
                        </div>
                        <input type="email" id="email" placeholder="Direción de email" name="email"
                            v-model="formData.email" />
                    </div>
                    <div class="landing-container--form--checkbox">
                        <div v-if="errors.checked" class="landing-container--form--error">
                            <p>{{ errors.checked }}</p>
                        </div>
                        <div class="landing-container--form--checkbox-items">
                            <input type="checkbox" id="checkbox" v-model="formData.checked" name="checkbox" />
                            <label for="checkbox">
                                He leído y acepto los
                                <a href="/conditions/">términos y condiciones</a>. Sus datos personales no serán
                                utilizados para
                                uso comercial.
                            </label>
                        </div>
                    </div>
                </div>
                <div class="landing-container--form--submit">
                    <Button v-if="!state.sendingInfo" @handle-click="submitForm">Registrar</Button>
                    <div v-else class="loader-container">
                        <div class="loading-dual-ring"></div>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script setup>
import Button from "~/components/generic/Button.vue";
import { reactive } from "vue";
import API from "~/utils/axios";
import BigSXTLogo from "~/components/generic/BigSXTLogo.vue";

// route
const route = useRoute();

// state
const state = reactive({
    sendingInfo: false,
});

// formData
const formData = reactive({
    email: "",
    checked: false,
});

// errors
const errors = reactive({
    email: "",
    checked: "",
});

// isValidEmail
const isValidEmail = (email) => {
    // validate email
    const re = /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i;
    return re.test(email);
};

// validator
const validateForm = () => {
    // validate the form
    let valid = true;
    // check if the checkbox and email are valid
    if (!formData.checked) {
        // if the checkbox is not checked show an error
        errors.checked = "Debes aceptar los términos y condiciones";
        valid = false;
    } else {
        // if the checkbox is checked remove the error
        errors.checked = "";
    }

    // check if the email is valid
    if (!formData.email) {
        // if the email is empty show an error
        errors.email = "El email es obligatorio";
        valid = false;
    } else if (!isValidEmail(formData.email)) {
        // if the email is not valid show an error
        errors.email = "Debe ingrear una dirección de email válida";
        valid = false;
    } else {
        // if the email is valid remove the error
        errors.email = "";
    }

    return valid;
};

// register user
async function submitForm() {
    state.sendingInfo = true;
    if (validateForm()) {
        // Form is valid, submit the data or perform other actions
        const brand_id = route.params.brand_id;
        // register the user
        try {
            // user and brand data
            const data = {
                email: formData.email,
                registration_brand: brand_id,
            };
            // send the data to the backend
            const res = await API.post("/back/api/user/registration/", data);
            // if the user was registered successfully
            if (res.status === 201) {
                // store the email using cookies
                const emailCookie = useCookie("email", {
                    maxAge: 60 * 24 * 60 * 60,
                });
                emailCookie.value = res.data.email;
                // navigate to the confirmation page
                return navigateTo(`/registration/${brand_id}/confirmation/`);
            }
        } catch (error) {
            // if the user was not registered successfully
            if (error.response && error.response.status === 400) {
                // show an error
                errors.email = "El email ya está registrado";
            } else {
                // show an error
                errors.email = "Ha ocurrido un error";
            }
        } finally {
            state.sendingInfo = false;
        }
    } else {
        state.sendingInfo = false;
    }
}
</script>

<style lang="scss">
@import "assets/css/variables";

.landing-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 100px;
    width: 100%;
    padding: 100px 0 0 0;

    @media (max-width: $default-breakpoint) {
        padding: 66px 0 0 0;
        gap: 66px;
    }

    .landing-comment {
        max-width: 600px;
        width: 100%;
        height: auto;
        font-weight: 300;
        font-size: $font-size-medium;
        font-style: normal;
        line-height: 30px;
        letter-spacing: 1.76px;
        text-transform: uppercase;
        text-align: center;
        margin: 0;

        @media (max-width: $default-breakpoint) {
            max-width: 375px;
            width: 100%;
            font-size: 18px;
            line-height: 24px;
            height: auto;
        }
    }

    .landing-container--form {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 48px;
        align-self: stretch;

        .loader-container {
            .loading-dual-ring::after {
                border: 6px solid $primary;
                border-color: $primary transparent $primary transparent;
            }
        }

        .form {
            display: flex;
            max-width: 507px;
            width: 100%;
            height: auto;
            flex-direction: column;
            align-items: center;
            gap: 56px;

            @media (max-width: $default-breakpoint) {
                gap: 48px;
                padding: 0 25px;
                max-width: 375px;
                width: 100%;
                height: auto;
            }

            .landing-container--form--elements {
                max-width: 507px;
                width: 100%;
                height: auto;
                display: flex;
                padding-bottom: 25px;
                flex-direction: column;
                align-items: flex-start;
                gap: 40px;

                @media (max-width: $default-breakpoint) {
                    gap: 30px;
                }

                .landing-container--form--input {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 8px;
                    align-self: stretch;

                    // change input placeholder attributes
                    input {
                        width: 100%;
                        height: 40px;
                        border: 0;
                        border-bottom: 1px solid $text-color-primary;
                        border-radius: 0;
                        padding: 0 16px;
                        font-size: $font-size-small;
                        font-style: normal;
                        font-weight: 300;
                        line-height: 22px;
                        letter-spacing: 0.32px;
                        color: $text-color-primary;
                        background-color: transparent;
                        transition: 0.3s border-color;
                        outline: none;

                        &:focus,
                        &:hover {
                            border-color: $secondary;
                        }
                    }
                }

                .landing-container--form--error {
                    color: $error;
                    text-align: center;
                    font-size: $font-size-small;
                    font-style: italic;
                    font-weight: 300;
                    line-height: 22px;
                    letter-spacing: 0.32px;
                    display: flex;

                    p {
                        padding: 0;
                        margin: 0;
                    }
                }

                .landing-container--form--checkbox {
                    display: flex;
                    flex-direction: column;

                    .landing-container--form--checkbox-items {
                        display: flex;
                        max-width: 507px;
                        width: 100%;
                        height: auto;
                        align-items: flex-start;
                        gap: 10px;

                        @media (max-width: $default-breakpoint) {
                            max-width: 325px;
                            width: 100%;
                            height: auto;
                        }

                        input {
                            width: 20px;
                            height: 20px;
                            border: 1px solid $text-color-primary;
                            border-radius: 0;
                            padding: 0;
                            margin: 0;
                            background-color: transparent;
                            transition: 0.3s border-color;
                            outline: none;

                            &:focus,
                            &:hover {
                                border-color: $secondary;
                            }
                        }
                    }

                    label {
                        font-size: $font-size-small;
                        font-style: normal;
                        font-weight: 300;
                        line-height: 22px;
                        letter-spacing: 0.32px;
                        color: $text-color-primary;

                        a {
                            color: $text-color-primary;
                        }
                    }
                }
            }
        }
    }
}
</style>
