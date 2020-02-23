<template>
  <div>
    <h2 class="title">Tu będzie input do korzystania normalnego 😜</h2>
    <form :action="action" @submit.prevent="sendRequest">
      <div class="field">
        <label for="spellcheck" class="label">Message</label>
        <div class="control">
          <textarea id="spellcheck" class="textarea" placeholder="Textarea" v-model="text"></textarea>
        </div>
      </div>
      <div class="field">
        <button type="submit" class="button is-link">Submit</button>
      </div>
    </form>
  </div>

</template>

<script>
    export default {
        name: "Home",
        data() {
            return {
                text: "",
                action: "/verify"
            }
        },
        methods: {
            sendRequest() {
                axios.post(this.action, this.text.split(' '))
                    .then((resp) => {
                        if (resp.data.length > 0) {
                            for (let i = 0; i < resp.data.length; i++) {
                                console.log(resp.data.results[i].word, resp.data.results[i].reply);
                            }
                        } else {
                            console.log(resp);
                        }
                    })
                    .catch((error) => {
                        console.error(error);
                    })
                    .finally(() => {
                        let i = 0;
                    });
            }
        }
    }
</script>

<style scoped>

</style>
