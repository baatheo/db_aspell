<template>
  <div>
    <form action="/upload">
      <div class="file">
        <label class="file-label">
          <input class="file-input" name="resume" type="file">
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
    </form>
  </div>
</template>

<script>
    export default {
        name: "Upload"
    }
</script>

<style scoped>

</style>
