<template>
  <div class="progress-bar-container">
    <div class="progress-bar" :style="{ width: score + '%' }"></div>
    
  </div>
</template>

<script>
export default {
  name: 'ProgressBar',
  props: {
    score: {
      type: Number,
      required: true
    }
  },
}
</script>

<style scoped>
.progress-bar-container {
  width: 100%;
  background-color: #e0e0e0;
  border-radius: 25px; /* This gives the container rounded corners */
  overflow: hidden; /* Ensures the inner .progress-bar respects the border radius */
}

.progress-bar {
  height: 20px;
  background-color: green;
  border-radius: 25px; /* Make sure this is equal to or greater than the container's border-radius */
}


</style>
