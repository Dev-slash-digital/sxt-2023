<template>
    <RegistrationForm></RegistrationForm>
</template>

<script setup>
import RegistrationForm from "@/components/RegistrationForm.vue";

// head
useHead({
    title: "Formulario de registro",
});

// page meta
definePageMeta({
    layout: "registration-form",
    middleware: "registration",
});
</script>
