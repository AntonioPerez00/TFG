<template>
  <aside
    class="fixed left-4 top-1/2 transform -translate-y-[45%] bg-[#FFFFFF]"
    id="filterBar"
  >
    <h2 class="text-xl font-semibold mb-4">Filtros</h2>
    <hr />

    <!-- Ordenar por precio -->
    <details class="filtros">
      <summary class="cursor-pointer text-base font-medium">Ordenar</summary>
      <div class="mt-2">
        <select class="select_category" v-model="filtros.orden">
          <option value="price">Precio ascendente</option>
          <option value="-price">Precio descendente</option>
          <option value="created_at">Más reciente</option>
          <option value="-created_at">Más antiguo</option>
        </select>
      </div>
    </details>
    <hr />

    <!-- Filtro por categoría -->
    <details class="filtros">
      <summary class="cursor-pointer text-base font-medium">Categoría</summary>
      <div class="mt-2">
        <select class="select_category" v-model="filtros.categoria">
          <option value="">Todos</option>
          <option v-for="cat in categorias" :key="cat.id" :value="cat.id">
            {{ cat.name }}
          </option>
        </select>
      </div>
    </details>
    <hr />

    <!-- Filtro por precio -->
    <details class="filtros">
      <summary class="cursor-pointer text-base font-medium">Precio</summary>
      <div class="pt-[1rem]">
        <span>Desde</span>
        <input type="number" class="mt-[rem] ml-[1rem] mr-[0.5rem] w-[4em]" v-model.number="filtros.precioDesde">
        <span>€</span>
      </div>
      <div class="mt-[1rem]">
        <span>Hasta</span>
        <input type="number" class="mt-[rem] ml-[1rem] mr-[0.5rem] w-[4em]" v-model.number="filtros.precioHasta">
        <span>€</span>
      </div>
    </details>
    <hr />

    <!-- Filtro por estado -->
    <details class="filtros">
      <summary class="cursor-pointer text-base font-medium">Estado</summary>
      <select class="select_category" v-model="filtros.estado">
        <option value="">Cualquiera</option>
        <option v-for="estado in estados">
          {{ estado.value }}
        </option>
      </select>
    </details>

    <div class="mt-[2rem] p-0 flex">
      <button @click="aplicarFiltros" class="bg-[#299CA9] border-none text-[#FFFFFF] rounded-[1.2rem] pt-[10px] pb-[10px] pl-[25px] pr-[25px] text-[15px] cursor-pointer">
        Filtrar
      </button>

      <button @click="resetFiltros" class="bg-[#EC7753] border-none text-[#FFFFFF] rounded-full text-[15px] w-[2.5rem] h-[2.5rem] ml-[1rem] cursor-pointer">
        <img src="../assets/papelera.png" alt="papelera" class="w-[1.5rem] h-[1.5rem]">
      </button>
    </div>
  </aside>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '../services/api'

const filtros = ref({
  orden: 'created_at',
  categoria: '',
  precioDesde: '',
  precioHasta: '',
  estado: '',
})

const emit = defineEmits(['filtrar-productos'])
const categorias = ref([])
const estados = ref([])

async function fetchFiltrosOptions() {
  try {
    const [resCategorias, resEstados] = await Promise.all([
      api.get('/categories/'),
      api.get('products/states/')
    ])
    categorias.value = resCategorias.data
    estados.value = resEstados.data
  } catch (error) {
    console.error('Error al cargar filtros:', error)
  }
}

function aplicarFiltros() {
  emit('filtrar-productos', filtros.value)
}

function resetFiltros() {
  filtros.value = {
    orden: 'created_at',
    categoria: '',
    precioDesde: '',
    precioHasta: '',
    estado: '',
  }
  // Emitimos los filtros reseteados
  // emit('filtrar-productos', filtros.value)
  // Comentado por si se quiere activar
  // Ahora mismo no me interesa que se apliquen los filtros al borrar
}

onMounted(() => {
  fetchFiltrosOptions()
})
</script>

<style>
#filterBar {
  padding: 40px;
  padding-top: 10px;
  margin-left: 30px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  border-radius: 20px;
  width: 10rem;
}

.filtros {
  margin-top: 20px;
  margin-bottom: 30px;
}

.label_category {
  font-size: 17px;
}

.select_category {
  width: 100%;
  margin-top: 0.75rem;
  border-radius: 10px;
  padding: 5px;
}
</style>
