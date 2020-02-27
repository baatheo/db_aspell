<template>
    <div>
        <form class="box" :action="action" enctype="multipart/form-data" @submit.prevent="test">
            <div class="field">
                <label for="textInput" class="label">A</label>
                <textarea v-model="textInput" name="textInput" id="textInput" cols="30" rows="6" class="textarea"></textarea>
            </div>
            <div class="field">
                <div class="control">
                    <button type="submit" class="button is-link" :class="{ 'is-loading': isSending }">Submit</button>
                </div>
            </div>
        </form>
        <div v-show="isReady" class="box">
            <div ref="result"></div>
        </div>
    </div>
</template>

<script>
    import Button from "./Button";
    const ButtonClass = Vue.extend(Button);

    export default {
        name: "SpellCheck",
        components: {Button},
        data() {
            return {
                action: '/verify2',
                isSending: false,
                isReady: false,
                helpText: false,
                helpTextType: "",
                formData: new FormData(),
                textInput: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                tempText: [],
                elements: []
            }
        },
        mounted() {
            this.copyText()
        },
        methods: {
            copyText: function () {
                this.tempText = [(' ' + this.textInput).slice(1)];
            },
            test() {
                this.copyText();
                let list = {
                    "ipsum": {
                        "list": ["ipsugum", "ipsumem", "ippsum"],
                        "pos": [0, 2],
                    },
                    "adipiscing": {
                        "list": ["foo", "foo2"],
                        "pos": [1, 3],
                    }
                };
                let t = this.tempText;

                for (let word in list) {
                    let temp = [];
                    let arr = [];
                    t.forEach((token) => {
                        if ("string" === typeof token) {
                            temp = token.split(word);
                            arr.push(...temp);
                            //arr = [...arr].map((e, i) => i < arr.length - 1 ? [e,  new ButtonClass()] : [e]).reduce((a, b) => a.concat(b))
                        }
                    });
                    t = arr;
                    console.log(t);

                    // [...arr].map((e, i) => i < arr.length - 1 ? [e,  new ButtonClass()] : [e]).reduce((a, b) => a.concat(b)).forEach((el) => {
                    //     this.elements.push(el);
                    // });

                    // this.elements.push(document.createTextNode(xd[0]));
                    // this.elements.push(new ButtonClass());
                    // this.tempText = xd[1];
                }

            },
            check: function (event) {
                this.copyText();
                this.isSending = true;
                this.formData = new FormData(event.target);
                axios.post(this.action, this.formData)
                    .then((resp) => {
                        console.log(resp);


                        this.isReady = true;
                    })
                    .catch((error) => {
                        console.error(error, error.response || '');
                    })
                    .finally(() => {
                        this.isSending = false;
                        console.log(this.elements)
                    });


            }
        }
    }
</script>

<style>

</style>
