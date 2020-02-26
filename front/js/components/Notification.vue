<template>
    <div class="notification" :class="type">
        <button class="delete"></button>
        {{ text }}
    </div>
</template>

<script>
    export default {
        name: "Notification",
        props: {
            text: 'string',
            type: 'string'
        }
    }
</script>

<style scoped>

</style>
