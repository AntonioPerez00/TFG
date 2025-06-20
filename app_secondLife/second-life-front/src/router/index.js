// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../pages/HomePage.vue'
import UploadProduct from '../pages/UploadProduct.vue'
import AuthView from '../pages/auth/AuthView.vue'
import ProductDetails from '../pages/ProductDetails.vue'
import ProductCheckout from '../pages/ProductCheckout.vue'
import MyProductDetails from '../pages/MyProductDetails.vue'
import User from '../pages/User.vue'
import FUser from '../pages/FUser.vue'
import EditUser from '../pages/EditUser.vue'
import EditProduct from '../pages/EditMyProduct.vue'
import Mysoldproduct from '../pages/MySoldProduct.vue'

const routes = [
  { path: '/', redirect: '/auth' },
  { path: '/auth', component: AuthView },
  { path: '/home', component: HomePage },
  { path: '/product/:id', component: ProductDetails },
  { path: '/my-product/:id', component: MyProductDetails },
  { path: '/checkout/:id', component: ProductCheckout },
  { path: '/user/:mail', component: User },
  { path: '/fuser/:mail', component: FUser },
  { path: '/upload-product', component: UploadProduct },
  { path: '/edit', component: EditUser },
  { path: '/editProduct/:id', component: EditProduct },
  { path: '/my-soldproduct/:id', component: Mysoldproduct },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
