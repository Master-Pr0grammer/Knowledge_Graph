<template>

  <div class="node-container">
    <div class="node" @click="toggle">
      {{ data.name }} - Score: {{ data.score }}
      <progress max="100" :value="data.score"></progress>
      <!-- <progress-bar :value="40"></progress-bar> -->
    </div>
    <div v-if="isOpen">
      <ChildNodes
        v-for="(child, index) in data.nodes"
        :key="index"
        :data="child"
      />
    </div>
  </div>
</template>

<script>
// import  ProgressBar from './ProgressBar.vue';

export default {
  name: 'ChildNodes', // The component's name is used for recursive reference
  props: ['data'],
  data() {
    return {
      isOpen: false
    };
  },
  methods: {
    toggle() {
      this.isOpen = !this.isOpen;
    }
  },
  // This is necessary to inform Vue that the component will be used recursively.
  components: {
    ChildNodes: () => import('./ChildNodes.vue'),
    // ProgressBar
  }
};
</script>

<style>
.node {
  margin: 100px, 0, 100px, 20px;
  cursor: pointer;
}

.node-container {

  margin-left: 30px;
  animation: fade-in 1s ease-in forwards;
}

.node-container .node:hover {
  background-color: lightgray;
}

progress {
  color: green;
}


@keyframes fade-in {
  from { opacity: 0; }
  to { opacity: 1;}
}

</style>
