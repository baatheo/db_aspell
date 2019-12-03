<template>
  <div>
    <h2 class="title">Upload origin file</h2>
    <form action="/upload" enctype="multipart/form-data" @submit.prevent="sendFile">
      <div class="field">
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
        <p class="help is-danger" v-show="errorText">
        {{ errorText }}
        </p>
      </div>
      <div class="field">
        <div class="control">
          <button type="submit" class="button is-link">Submit</button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
    export default {
        name: "Upload",
        data() {
            return {
                isSending: false,
                isReady: false,
                errorText: false,
                file: null
            }
        },
        methods: {
            handleFile(event) {
                this.errorText = false;
                if (event.target.files[0]) {
                    this.file = event.target.files[0];
                    this.isReady = true;
                }
            },
            sendFile() {
                if (this.isReady) {
                    this.errorText = false;
                    this.isSending = true;
                    axios.post('/upload', this.file, {
                        headers: {
                            'Content-Type': 'text/plain'
                        }
                    })
                        .then((resp) => {
                            setTimeout(() => {
                            }, 1000);
                            console.log(resp);
                        })
                        .catch((error) => {
                            console.error(error);
                            this.errorText = "Something went wrong";
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
