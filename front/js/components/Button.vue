<template>
    <div ref="word" class="word" @close-toasts="close">
        <button class="misspell has-text-danger" v-text="text" @click="open"></button>
        <div class="box toast" v-show="isOpen">
            <button class="button is-small is-success" @click="choose">Foo</button>
            <button class="button is-small is-success" @click="choose">Foo2</button>
            <button class="button is-small is-success" @click="choose">Foo3</button>
        </div>
    </div>
</template>

<script>
    import eventBus from "../eventBus";

    export default {
        name: "Button",
        props: [ 'text' ],
        data() {
            return {
                isOpen: false
            }
        },
        created() {
            eventBus.$on('close-toasts', this.close);
        },
        methods: {
            open: function(){
                eventBus.$emit('close-toasts');
                this.isOpen = true;
            },
            close: function () {
                console.log('close');
                this.isOpen = false;
            },
            choose: function(event) {
                this.isOpen = false;
                this.$refs.word.textContent = event.target.textContent;
            }
        }
    }
</script>

<style scoped>
    .word {
        display: inline;
    }

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

    div.box.toast {
        position: absolute;

    }

</style>
