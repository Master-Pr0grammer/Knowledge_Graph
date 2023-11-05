<script>
import axios from 'axios';
import ChildNodes from './ChildNodes.vue';

export default {
  components: {
    ChildNodes
  },
  data() {
    return {
      files: [],
      activeData: null,
    };
  },
  methods: {
    fetchFiles() {
      axios.get('http://localhost:5000/results')
        .then(response => {
          this.files = response.data;
        })
        .catch(error => {
          console.error('There was an error!', error);
        });
    },
    fetchAndSetActive(filename) {
      axios.get(`http://localhost:5000/api/results/${filename}`)
        .then(response => {
          this.activeData = response.data;
        })
        .catch(error => {
          console.error('There was an error!', error);
        });
    }
  },
  created() {
    this.fetchFiles();
  }
};
</script>

<template>
  <div class="home">
    <div class="greetings">
      <h1>
        Nice to have you back!
      </h1>
      <p> 
        Check out some of your progress below: 
      </p>
    </div>
    <div class="content">
      <div v-for="file in files" :key="file">
        <div @click="fetchAndSetActive(file)">
          {{ file }}
        </div>
      </div>
      <ChildNodes :data="activeData" v-if="activeData"/>
    </div>
  </div>
</template>


<style scoped>

.home {
  display: flex;
  flex-direction: column;
  float: left;
  align-items: left;
  justify-content: center;
  height: 100%;
  width: 100%;
}

.greetings {
  font-size: 30px;
}

.content {
  margin-top: 30px;
  outline: 2px solid grey;
  outline-offset: 5px; 

}

</style> 