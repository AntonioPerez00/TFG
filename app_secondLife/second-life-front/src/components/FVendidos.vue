<template>
  <div class="flex flex-wrap gap-[4rem]">
    <Item
      v-for="producto in productos"
      :key="producto.id"
      :producto="producto"
      class="cursor-pointer relative"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '../services/api'
import Item from '../components/Item.vue'
import { useRoute, useRouter } from 'vue-router'

const productos = ref([])
const loading = ref(true)
const router = useRouter()
const route = useRoute()
const mail = route.params.mail

// Por si usas filtros u otros parámetros:
const params = {disponibility: 'vendido'}

async function filtrarProductos(){
  try {
    const [response] = await Promise.all([
      api.get(`/users/${mail}/products/`, {
        params: { disponibility: 'vendido' }
      }),
      new Promise(resolve => setTimeout(resolve, 200))
    ])
    productos.value = response.data
  } catch (error) {
    console.error('Error al cargar productos:', error)
  } finally {
    loading.value = false
  }
}
onMounted(async () => {
  filtrarProductos();
});

</script>
