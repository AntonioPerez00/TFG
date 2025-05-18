// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../pages/HomePage.vue'
import AuthView from '../pages/auth/AuthView.vue'

const routes = [
  { path: '/', redirect: '/auth' },
  { path: '/auth', component: AuthView },
  { path: '/home', component: HomePage },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
