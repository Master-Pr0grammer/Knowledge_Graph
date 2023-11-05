<template>

  <div class="node-container">
    <div class="node" @click="toggle">
      {{ data.name }} - Score: {{ data.score }}
      <progress-bar :value="data.score"></progress-bar>
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
import  ProgressBar from './ProgressBar.vue';

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
    ProgressBar
  }
};
</script>

<style>
.node {
  margin-left: 20px;
  cursor: pointer;
}

.node-container {
  outline: 2px solid grey;
  outline-offset: 5px; 
}

</style>
