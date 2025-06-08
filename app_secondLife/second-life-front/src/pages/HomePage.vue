<template>
  <div class="bg-[#FFFDF8] relative min-h-screen">
    <NavBar @buscar="actualizarBusqueda" />
    <div class="pt-20 px-8 flex gap-6">
      <Filtros @filtrar-productos="actualizarFiltros"/>

      <main class="flex flex-col mt-[80px] p-[20px] ml-[20rem] flex-grow">
        <div><p class="text-[#9f9a8f] text-[18px]">Dale una segunda vida a tus cosas</p></div>
        <div class="flex flex-wrap gap-[4rem]">
          <Item
            v-for="producto in productos"
            :key="producto.id"
            :producto="producto"
            class="cursor-pointer relative"
            @click="productDetails(producto)"
          />

        </div>
      </main>
    </div>

    <!-- Spinner overlay -->
    <div v-if="loading" class="spinner-overlay">
      <div class="spinner"></div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import api from '../services/api'
import NavBar from '../components/NavBar.vue'
import Filtros from '../components/FilterBar.vue'
import Item from '../components/Item.vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import { watch } from 'vue'

const authStore = useAuthStore()

const router = useRouter()
const route = useRoute()

const pagina = ref(1)
const finDeResultados = ref(false)

function productDetails(producto) {
  const url = router.resolve(`/product/${producto.id}`).href
  window.open(url, '_blank')
}

const productos = ref([])
const loading = ref(false)

const busquedaActual = ref('')
const filtrosActivos = ref({})

async function filtrarProductos(busqueda = '', filtros = {}, cargarMas = false) {
  if (loading.value || finDeResultados.value) return
  loading.value = true

  const params = {
    search: busqueda,
    category: filtros.categoria,
    state: filtros.estado,
    price__gte: filtros.precioDesde,
    price__lte: filtros.precioHasta,
    ordering: filtros.orden,
    page: pagina.value,
  }

  const queryParams = Object.fromEntries(
    Object.entries(params).filter(([_, v]) => v !== '' && v !== undefined)
  )

  if (!cargarMas) {
    productos.value = []
    pagina.value = 1
    finDeResultados.value = false
  }

  try {
    const response = await api.get('/products/', { params })

    const nuevosProductos = response.data.results || response.data  // por si no se devuelve en .results
    if (nuevosProductos.length === 0) {
      finDeResultados.value = true
    } else {
      if (cargarMas) {
        productos.value.push(...nuevosProductos)
      } else {
        productos.value = nuevosProductos
      }
      pagina.value += 1
    }
  } catch (error) {
    console.error('Error al cargar productos:', error)
  } finally {
    loading.value = false
  }
}


// Estas funciones se ejecutan al recibir los emits:
function actualizarBusqueda(nuevaBusqueda) {
  busquedaActual.value = nuevaBusqueda
  filtrarProductos(busquedaActual.value, filtrosActivos.value)
}

function actualizarFiltros(nuevosFiltros) {
  filtrosActivos.value = nuevosFiltros
  filtrarProductos(busquedaActual.value, nuevosFiltros)
}

onMounted(() => {
  authStore.checkAuth()
  const query = route.query

  filtrosActivos.value = {
    categoria: query.category || '',
    estado: query.state || '',
    precioDesde: query.price__gte || '',
    precioHasta: query.price__lte || '',
    orden: query.ordering || 'price'
  }

  busquedaActual.value = query.search || ''

  filtrarProductos(busquedaActual.value, filtrosActivos.value)
})


watch(() => route.query, (nuevaQuery) => {
  filtrosActivos.value = {
    categoria: nuevaQuery.category || '',
    estado: nuevaQuery.state || '',
    precioDesde: nuevaQuery.price__gte || '',
    precioHasta: nuevaQuery.price__lte || '',
    orden: nuevaQuery.ordering || 'price'
  }

  busquedaActual.value = nuevaQuery.search || ''
  filtrarProductos(busquedaActual.value, filtrosActivos.value)
})


</script>

<style>
.spinner-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;    /* cubrir toda la pantalla */
  height: 100vh;   /* cubrir toda la pantalla */
  background-color: rgba(0, 0, 0, 0.4); /* fondo negro semi-transparente */
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999; /* por encima de todo */
}

.spinner {
  border: 4px solid #f3f3f3;
  border-top: 4px solid #299CA9;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  animation: spin 1s linear infinite;
}

/* Animación giratoria */
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>
