<template>
  <div class="bg-[#FFFDF8] min-h-screen" v-if="producto">
    <NavBar />

    º
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import api from '../services/api'
import NavBar from '../components/NavBar.vue'

const route = useRoute()
const producto = ref(null)
const loading = ref(true)
const backendURL = 'http://localhost:8000'

onMounted(async () => {
  try {
    const res = await api.get(`/products/${route.params.id}/`)
    producto.value = res.data
  } catch (error) {
    console.error('Error al cargar el producto:', error)
  } finally {
    loading.value = false
  }
})

</script>
