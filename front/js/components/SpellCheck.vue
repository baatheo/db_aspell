<template>
    <div>
        <form class="box" :action="action" enctype="multipart/form-data" @submit.prevent="check">
            <div class="field">
                <label for="textInput" class="label">A</label>
                <textarea name="textInput" id="textInput" cols="30" rows="6" class="textarea">{{ test }}</textarea>

            </div>
            <div class="field">
                <div class="control">
                    <button type="submit" class="button is-link" :class="{ 'is-loading': isSending }">Submit</button>
                </div>
            </div>
        </form>
        <div v-show="isReady" class="box">
            <div v-html="result"></div>
        </div>
    </div>

</template>

<script>
    export default {
        name: "SpellCheck",
        data() {
            return {
                action: '/verify2',
                isSending: false,
                isReady: false,
                helpText: false,
                helpTextType: "",
                formData: new FormData(),
                test: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
                result: ''
            }
        },
        methods: {
            check: function(event) {
                this.isSending = true;
                this.formData = new FormData(event.target);
                axios.post(this.action, this.formData)
                    .then((resp) => {
                        console.log(resp);
                        let list = {
                            'ipsum' : ['ipsum', 'ipsumem', 'ippsum'],
                            'adipiscing': ['foo', 'foo2']
                        };
                        this.result = (' ' + this.test).slice(1);
                        // button need to be separated component
                        list.forEach((el, i) => {
                            this.result =  this.result.replace(el, `<button class="misspell has-text-danger">${el}</button>`);
                        });
                        this.isReady = true;
                    })
                    .catch((error) => {
                        console.error(error, error.response || '');
                    })
                    .finally(() => {
                        this.isSending = false;
                    });


            }
        }
    }
</script>

<style>
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
