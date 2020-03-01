<template>
    <div ref="word" class="word no-size" @close-toasts="close">
        <button class="misspell has-text-danger" v-text="text" @click="open"></button>
        <div ref="balloon" class="balloon box buttons has-addons" v-show="isOpen">
            <button v-for="p in proms" :key="p" class="button" @click="choose" :disabled="disabled">{{ p }}</button>
        </div>
    </div>
</template>

<script>
    import eventBus from "../eventBus";

    export default {
        name: "Button",
        props: [ 'text', 'proms', 'disabled' ],
        data() {
            return {
                isOpen: false
            }
        },
        created() {
            eventBus.$on('close-balloon', this.close);
        },
        methods: {
            open: function(event){
                eventBus.$emit('close-balloon');
                this.isOpen = true;
                this.$refs["balloon"].style.left = (event.clientX-50) + 'px';
            },
            close: function () {
                this.isOpen = false;
            },
            choose: function(event) {
                this.isOpen = false;
                this.$refs.word.textContent = event.target.textContent;
                this.$refs.word.classList.remove('no-size');

            }
        }
    }
</script>

<style scoped>
    .word {
        display: inline;
    }

    .word.no-size {
        font-size: 0;
    }

    button.misspell {
        text-decoration: underline !important;
        background: none;
        margin: 0;
        padding: 0;
        border: none;
        font-size: 1rem;
    }

    button.misspell:hover {
        cursor: pointer;
    }

    div.box.balloon {
        position: absolute;
        font-size: 1rem;
    }
    .balloon.buttons .button {
        margin-bottom: 0;
    }

</style>
