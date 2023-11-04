import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from '../components/LandingPage.vue'
import HomePage from '../components/HomePage.vue'

const routes = [
  {
    path: '/',
    name: 'LandingPage',
    component: LandingPage
  },
  {
    path: '/home',
    name: 'HomePage',
    component: HomePage
  }
  // ... other routes
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
