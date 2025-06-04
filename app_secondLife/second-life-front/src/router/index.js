// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../pages/HomePage.vue'
import AuthView from '../pages/auth/AuthView.vue'
import ProductDetails from '../pages/ProductDetails.vue'
import ProductCheckout from '../pages/ProductCheckout.vue'
import User from '../pages/User.vue'

const routes = [
  { path: '/', redirect: '/auth' },
  { path: '/auth', component: AuthView },
  { path: '/home', component: HomePage },
  { path: '/product/:id', component: ProductDetails },
  { path: '/checkout/:id', component: ProductCheckout },
  { path: '/user/:mail', component: User },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
