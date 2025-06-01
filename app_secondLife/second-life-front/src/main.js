import { createApp } from 'vue'
import { createPinia } from 'pinia'     // <-- Importa Pinia aquí
import App from './App.vue'
import router from './router'
import './assets/tailwind.css'

const app = createApp(App)
const pinia = createPinia()             // <-- Crea la instancia de Pinia

app.use(pinia)                         // <-- Usa Pinia
app.use(router)
app.mount('#app')
