<template>
  <div class="landing">
    <h1 v-html="animatedHeading"></h1>
    <p v-html="animatedText"></p>
    
    <router-link to="/home" v-if="showButton">
      <button>Click to start</button>
    </router-link>

    
  </div>
</template>

<script>
export default {
  name: 'LandingPage',
  data() {
    return {
      heading: 'Welcome to Knowledge_Graphs!',
      text: 'A quick way to visualize understanding of multiple abstract topics.',
      animatedHeading: '',
      animatedText: '',
      showButton: false // Initial state of the button is not visible
    }
  },
  mounted() {
    this.typeText(
      this.heading,
      'animatedHeading',
      () => {
        // After the heading is completed, start typing the paragraph
        this.typeText(
          this.text,
          'animatedText',
          () => {
            // After the paragraph is completed, show the button
            this.showButton = true
          },
          30
        )
      },
      50
    )
  },
  methods: {
    typeText(text, stateKey, callback, speed) {
      let i = 0
      const interval = setInterval(() => {
        if (i < text.length) {
          this[stateKey] += text[i]
          i++
        } else {
          clearInterval(interval)
          // If there's a callback passed, execute it after typing is finished
          if (callback) callback()
        }
      }, speed) // The speed of typing, in milliseconds
    }
  }
}
</script>

<style scoped>
.landing {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  font-size: 30px;
}

h1,
p {
  margin: 0;
  white-space: nowrap;
  overflow: hidden;
}

/* Transition the button in smoothly after typing is finished */
button {
  margin-top: 40px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  border-radius: 25px;
  animation: fade-in 1s ease-in forwards;
}

@keyframes fade-in {
  from { opacity: 0; }
  to { opacity: 1;}
}

</style>
