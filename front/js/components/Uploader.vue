<template>
    <form class="box" action="/upload" enctype="multipart/form-data" @submit.prevent="sendFile">
        <div class="field">
            <div class="control">
                <div class="file">
                    <label class="file-label">
                        <input class="file-input" name="resume" type="file" @change="handleFile" :disabled="isSending">
                        <span class="file-cta">
                            <span class="file-icon">
                              <i class="fas fa-upload"></i>
                            </span>
                            <span class="file-label">
                              {{ fileName }}
                            </span>
                        </span>
                    </label>
                </div>
                <p class="help" v-show="helpText" :class="helpTextType">
                    {{ helpText }}
                </p>
            </div>
        </div>
        <div class="field">
            <div class="control">
                <button type="submit" class="button is-link" :class="{ 'is-loading': isSending }">Submit</button>
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
                helpText: false,
                helpTextType: "",
                fileName: "Choose a file…",
                formData: new FormData()
            }
        },
        methods: {
            handleFile(event) {
                this.helpText = false;
                if (event.target.files[0]) {
                    this.fileName = event.target.files[0].name;
                    this.formData.append('file', event.target.files[0]);
                    this.isReady = true;
                }
            },
            sendFile(event) {
                if (this.isReady) {
                    this.helpText = false;
                    this.isSending = true;

                    axios.post('/upload', this.formData)
                        .then((resp) => {
                            if (resp.data.form.success) {
                                this.helpTextType = "is-success";
                                this.helpText = resp.data.form.message
                            } else {
                                this.helpTextType = "is-warning";
                                this.helpText = resp.data.form.message
                            }
                        })
                        .catch((error) => {
                            this.helpTextType = "is-danger";
                            this.helpText = error.response.data.form.errors.join('\n');
                        })
                        .finally(() => {
                            this.isSending = false;
                            event.target.reset();
                        });
                }
            }
        }
    }
</script>

<style scoped>

</style>
