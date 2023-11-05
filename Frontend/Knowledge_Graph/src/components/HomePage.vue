<script>
import axios from 'axios';
import ChildNodes from './ChildNodes.vue';
import FileReciever from './FileReciever.vue'

export default {
  components: {
    ChildNodes,
    FileReciever
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
    },
    fileName(file) {
      var strArray = file.split('.');
      return strArray[0];
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
        Check out some of your previous progress or upload your score on a new topic 
      </p>
    </div>
    
    <div class="get-file">
      <FileReciever/> 
    </div>

    <div class="content">
      
      <div v-for="file in files" :key="file" >
        <div @click="fetchAndSetActive(file)">
          {{ file }}
          <ChildNodes :data="activeData" v-if="activeData"/>
        </div>
      </div>
    </div>
  </div>
</template>


<style scoped>

.home {
  padding-top: 30px;
  height: 100%;
  width: 100%;
  animation: fade-in 1s ease-in forwards;

}


.greetings {
  font-size: 30px;
}

.get-file {
  text-align: center;

}


.content {
  font-size: 19px;
  margin: 30px 30px 30px 30px;
  outline: 2px solid grey;
  outline-offset: 5px; 
}


@keyframes fade-in {
  from { opacity: 0; }
  to { opacity: 1;}
}

</style> 