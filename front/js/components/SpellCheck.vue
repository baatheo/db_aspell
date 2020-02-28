<template>
  <div>
    <form class="box" :action="action" enctype="multipart/form-data" @submit.prevent="check">
      <div class="field">
        <label for="textInput" class="label">A</label>
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
  components: { Button },
  data() {
    return {
      action: "/verify2",
      isSending: false,
      isReady: false,
      helpText: false,
      helpTextType: "",
      formData: new FormData(),
      textInput:
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
      tempText: [],
      elements: []
    };
  },
  mounted() {
    this.copyText();
  },
  methods: {
    copyText: function() {
      this.tempText = [copyString(this.textInput)];
    },
    findErrorsInInput: function(input, misspells) {
      let t = [input];
      for (const misspell in misspells) {
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
      return t;
    },
    check: function(event) {
      this.copyText();
      this.isSending = true;
      this.formData = new FormData(event.target);
      axios
        .post(this.action, this.formData)
        .then(resp => {
          console.log(resp);
          const list = {
            ipsum: {
              list: ["ipsugum", "ipsumem", "ippsum"],
              pos: [0, 2]
            },
            adipiscing: {
              list: ["foo", "foo2"],
              pos: [1, 3]
            }
          };
          this.elements = this.findErrorsInInput(this.textInput, list);
          //this.isReady = true;
        })
        .catch(error => {
          console.error(error, error.response || "");
        })
        .finally(() => {
          this.isSending = false;
          console.log(this.elements);
        });
    }
  }
};
</script>

<style>
</style>
