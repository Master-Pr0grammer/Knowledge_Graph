<template>
  <div class="progress-bar-container">
    <div class="progress-bar" :style="{ width: filledWidth }"></div> 
  </div>
</template>

<script>
export default {
  name: 'ProgressBar',
  props: {
    value: {
      type: Number,
      required: true,
      default: 0,
      validator: (value) => value >= 0 && value <= 100,
    },
  },
  computed: {
    filledWidth() {
      return `${(this.value > 100 ? 100 : this.value)}%`;
    },
  },
};
</script>

<style scoped>
.progress-container {
  width: 200px;
  height: 20px;
  background-color: #eee;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: inset 0 0 5px rgba(0,0,0,0.2);
}

.progress-bar {
  height: 100%;
  background-color: #3b82f6; /* feel free to change the color */
  transition: width 0.25s ease-in-out;
}

</style>







