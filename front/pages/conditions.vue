<template>
    <div class="conditions-header">
        <NuxtLink to="/">
            <img
                width="72"
                height="87.4"
                src="~/assets/img/logo-conditions.svg"
            />
        </NuxtLink>
    </div>
    <div class="conditions-text">
        <p style="margin-bottom: 20px">
            Los datos personales proporcionados por usted con el fin de
            participar en La Ruta Solidarity Xmas Tree se conservarán hasta la
            realización del sorteo para la adjudicación del premio el 26 de
            noviembre de 2024 o hasta que usted ejerza su derecho de cancelación
            enviando su solicitud de cancelación a info@togetherplus.es. Los
            datos se destruirán pasados 15 días laborables posteriores al sorteo
            y, en ningún caso, se cederán a terceros.
        </p>
        <p>Mecánica Sorteo Ruta SXT:</p>
        <p>
            Premio: <br />
            Una estancia de tres noches con pensión completa en la suite
            Arriluce del Palacio Arriluce Hotel en Getxo, con:
        </p>
        <ul>
            <li>
                Salida en barco de vela desde el hotel por la ría al Museo
                Guggenheim y visita al Museo con guía privado
            </li>
            <li>
                Tratamiento Spa dos días para dos personas: masaje corporal y
                circuito de aguas
            </li>
            <li>Cata en la bodega del hotel</li>
            <li>Desayuno, comida y cena incluidos</li>
            <li>
                Otras actividades del hotel incluidas como clases de croquet
            </li>
        </ul>
        <p>
            Las participaciones validadas (visita y validación de siete árboles
            de Navidad que conforman la Ruta Solidartiy Xmas Tree) a través de
            la WebApp de la Ruta Solidarity Xmas Tree, serán presentadas en un
            listado asociadas cada una a un número.
        </p>
        <p>
            Tras su séptima visita y validación las personas registradas en la
            Ruta Solidarity Xmas Tree recibirán un email con la confirmación de
            su participación en el sorteo que incluirá su número de
            participación.
        </p>
        <p>
            El 26 de noviembre del 2024 en el Gran Teatro Real de Madrid, se
            escogerá aleatoriamente un número al azar comprendido entre el
            primero y el último número del listado de participantes que hayan
            visitado y validado mínimo 7 árboles de la Ruta SXT.
        </p>
        <p>
            El vídeo de la extracción de los números se publicará en la cuenta
            de IG de Solidarity Xmas Tree (@solidarityxmastree)
        </p>
        <p>
            El número seleccionado será localizado en el listado resultando así
            un ganador. La organización contactará con el ganador, vía email, en
            la cuenta de correo que facilitó para el registro en la Ruta
            Solidartiy Xmas Tree, antes del 3 de diciembre. Si transcurridas dos
            semanas del envío del email, el ganador no ha reconocido su premio,
            dicho premio quedará desierto.
        </p>
        <p>
            Una vez finalizado el sorteo la base de datos creada única y
            exclusivamente para la Ruta Solidarity Xmas Tree, será destruida.
        </p>
    </div>
</template>

<script setup>
definePageMeta({
    layout: "conditions",
});

useHead({
    title: "Conditions",
});
</script>

<style lang="scss">
@import "assets/css/variables";

.conditions-header {
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: $primary;
    width: 100%;

    img {
        width: 100%;
        height: auto;
        max-width: 72px;
        margin-top: 39px;
        margin-bottom: 39px;
    }
}

.conditions-text {
    display: flex;
    flex-direction: column;
    margin-left: 61px;
    margin-right: 61px;
    max-width: $max-width-lg;
    p {
        color: #000;
        font-size: 16px;
        font-style: normal;
        font-weight: 300;
        line-height: 16px; /* 160% */
        letter-spacing: 0.25px;
    }
}

ul {
    li {
        color: #000;
        font-size: 16px;
        font-style: normal;
        font-weight: 300;
        line-height: 16px; /* 160% */
        letter-spacing: 0.25px;
    }
}
</style>
