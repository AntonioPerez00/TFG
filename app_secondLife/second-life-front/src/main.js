import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './index.css' // o tu main TailwindCSS aquí

createApp(App).use(router).mount('#app')
