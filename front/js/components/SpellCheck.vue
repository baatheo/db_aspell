<template>
    <div>
        <form class="box" :action="action" enctype="multipart/form-data" @submit.prevent="check">
            <div class="field">
                <label for="textInput" class="label sr-only">A</label>
                <textarea
                    v-model="textInput"
                    name="textInput"
                    id="textInput"
                    cols="30"
                    rows="6"
                    class="textarea"
                ></textarea>
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
                action: "/verify",
                isSending: false,
                isReady: false,
                helpText: false,
                helpTextType: "",
                formData: new FormData(),
                textInput:
                    "",
                tempText: [],
                elements: []
            };
        },
        methods: {
            sortMisspells: function(m) {
                return [...Object.keys(m)].sort((a, b) => {
                    return a.length < b.length ? 1 : -1;
                });
            },
            findErrorsInInput: function (misspells) {
                let t = [copyString(this.textInput)];
                const sortedMisspells = this.sortMisspells(misspells);
                for (const index in sortedMisspells) {
                    if (sortedMisspells.hasOwnProperty(index)) {
                        const misspell = sortedMisspells[index].trim();
                        let temp = [];
                        let arr = [];
                        t.forEach(token => {
                            if ("string" === typeof token) {
                                temp = token.split(misspell);
                                arr.push(...temp);
                            }
                        });
                        t = arr;
                    }
                }
                return t;
            },
            prepareErrors: function (misspells) {
                let offset = 1;
                let pp = [];
                const sortedMisspells = this.sortMisspells(misspells);
                for (let index in sortedMisspells) {
                    if (sortedMisspells.hasOwnProperty(index)) {
                        const m = sortedMisspells[index];
                        let positions = misspells[m]["pos"];
                        let list = misspells[m]["list"];
                        if ("string" === typeof list) {
                            list = [list];
                        }
                        for (let pos in positions) {
                            pp[positions[pos]] = new ButtonClass({propsData: {text: m, proms: list}});
                        }
                    }
                }
                return pp;
            },
            concatTextAndErrors: function (text, components) {
                let x = [];
                let c = Math.max(text.length, components.length);
                for (let i = 0; i < c; i++) {
                    let a = text.shift();
                    a = a.replace(/ /g, '\u00a0');
                    let b = components.shift();
                    if (undefined !== a) {
                        x.push(document.createTextNode(a));
                    }
                    if (undefined !== b) {
                        x.push(b);
                    }

                }
                return x;
            },
            check: function (event) {
                this.isSending = true;
                this.isReady = false;
                this.formData = new FormData(event.target);
                this.$refs.result.textContent = "";
                axios
                    .post(this.action, this.formData)
                    .then(resp => {
                        this.elements = this.findErrorsInInput(resp.data);
                        return resp.data;
                    })
                    .then((list) => {
                        return this.concatTextAndErrors(this.elements, this.prepareErrors(list));
                    })
                    .then(nodes => {
                        [...nodes].forEach(node => {
                            if (3 === node.nodeType) {
                                this.$refs.result.appendChild(node);
                            } else {
                                node.$mount();
                                this.$refs.result.appendChild(node.$el);
                            }
                        });
                        this.isReady = true;
                    })
                    .catch(error => {
                        console.error(error, error.response || "");
                    })
                    .finally(() => {
                        this.isSending = false;
                    });
            }
        }
    };
</script>

<style>
</style>
