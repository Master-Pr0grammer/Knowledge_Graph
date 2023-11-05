<template>
    <div>
      <!-- The clickable area for opening the file dialog -->
      <div class="upload-area" @click="triggerFileInput">
        <p>Click here to select text files</p>
        <ul v-if="files.length > 0">
          <li v-for="(file, index) in files" :key="index">{{ file.name }}</li>
        </ul>
        <input type="file" ref="fileInput" @change="handleFileUpload" accept=".txt" multiple style="display: none;" />
      </div>

      <button @click="submitFiles" :disabled="files.length === 0">Upload Files</button>
      <div v-if="uploadProgress !== null">
        <progress max="100" :value="uploadProgress"> {{ uploadProgress }}% </progress>
        <span>{{ uploadProgress }}%</span>
      </div>
      <div v-if="errorMessage">{{ errorMessage }}</div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'FileReciever',
    data() {
      return {
        files: [],
        uploadProgress: null,
        errorMessage: '',
      };
    },
    methods: {
      triggerFileInput() {
        this.$refs.fileInput.click();
      },
      handleFileUpload(event) {
        this.files = Array.from(event.target.files);
        this.uploadProgress = null; // reset progress bar
        this.errorMessage = ''; // reset error message
      },
      async submitFiles() {
      const formData = new FormData();
      this.files.forEach((file) => {
      formData.append('file', file); // 'file' as the key
  });
  
        try {
          const response = await axios.post('http://localhost:5000/upload-text-files', formData, {
            onUploadProgress: (progressEvent) => {
              this.uploadProgress = parseInt(
                Math.round((progressEvent.loaded * 100) / progressEvent.total)
              );
            },
          });
          console.log('Files uploaded successfully:', response);
          this.files = []; // Reset the selected files
        } catch (error) {
          this.errorMessage = 'Error uploading files: ' + error.message;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .upload-area {
    padding: 20px;
    border: 2px dashed #007bff;
    border-radius: 5px;
    text-align: center;
    cursor: pointer;
    height: 200px;

    transition: border-color 0.3s;
  }
  
  .upload-area:hover {
    background-color: lightblue;
    border-color: #0056b3;
    animation: fade-in 1s ease-in-out;
  }
  
  @keyframes fade-in {
  from { background-color: white; }
  to { background-color: lightblue;}
}

  </style>
  