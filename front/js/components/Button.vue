<template>
    <button class="misspell has-text-danger"></button>
</template>

<script>
    export default {
        name: "Button"
    }
</script>

<style scoped>
    button.misspell {
        text-decoration: underline !important;
        background: none;
        margin: 0;
        padding: 0;
        border: none;
        font-size: 1em;
    }

    button.misspell:hover {
        cursor: pointer;
    }
</style>
