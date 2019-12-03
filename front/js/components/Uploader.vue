<template>
  <form action="/upload" enctype="multipart/form-data" @submit.prevent="sendFile">
    <div class="field is-grouped">
      <div class="control">
        <div class="file">
          <label class="file-label">
            <input class="file-input" name="resume" type="file" @change="handleFile" :disabled="isSending">
            <span class="file-cta">
            <span class="file-icon">
              <i class="fas fa-upload"></i>
            </span>
            <span class="file-label">
              Choose a file…
            </span>
          </span>
          </label>
        </div>
        <p class="help" v-show="text" :class="textType">
          {{ text }}
        </p>
      </div>
      <div class="control">
        <button type="submit" class="button is-link">Submit</button>
      </div>
    </div>
  </form>
</template>

<script>
    export default {
        name: "Uploader",
        data() {
            return {
                isSending: false,
                isReady: false,
                textType: "",
                text: false,
                formData: new FormData()
            }
        },
        methods: {
            handleFile(event) {
                this.text = false;
                if (event.target.files[0]) {
                    this.formData.append('file', event.target.files[0]);
                    this.isReady = true;
                }
            },
            sendFile() {
                if (this.isReady) {
                    this.text = false;
                    this.isSending = true;

                    axios.post('/upload', this.formData)
                        .then((resp) => {
                            console.log(resp);
                            this.textType = "is-success";
                            this.text = "File uploaded";
                        })
                        .catch((error) => {
                            console.error(error);
                            this.textType = "is-danger";
                            this.text = "Something went wrong";
                        })
                        .finally(() => {
                            this.isSending = false;
                        });
                }
            }
        }
    }
</script>

<style scoped>

</style>
