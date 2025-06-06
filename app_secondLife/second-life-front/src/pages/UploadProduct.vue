<template>
  <NavBar />

  <!-- El contenedor padre ocupa todo el ancho y centra el contenido -->
  <div class="w-full bg-[#FFFDF8] flex justify-center">
    <!-- El contenido tiene ancho máximo fijo y se ajusta centrado -->
    <div id="centro" class="w-full max-w-[55rem] mt-[10rem] flex flex-col mr-[4rem] mb-[5rem]">
      <h1 class="text-2xl font-semibold mb-[1.5rem]">Subir producto</h1>

      <div class="w-full bg-[#FFFFFF] shadow-[0_2px_4px_rgba(0,0,0,0.1)] p-[1.7rem] rounded-[1rem] flex flex-col mb-[4rem] gap-[2rem]">
        <div class="flex flex-row items-center justify-center gap-[1rem]">
          <span class="mb-0">Título del anuncio</span>
          <input
            v-model="nombre"
            placeholder="Título"
            required
            class="flex-1 border-0 border-b border-b-[#9f9a8f] p-[3px] text-[#9f9a8f] text-[1rem] bg-transparent focus:outline-none placeholder-[#9f9a8f]"
          />
        </div>

        <div class="flex flex-row gap-[1rem]">
          <span class="mb-0 mt-[1rem]">Descripción del producto</span>
          <textarea
            v-model="nombre"
            placeholder="Le quiero dar una segunda vida por que..."
            required
            class="flex-1 h-[6rem] border border-[#9f9a8f] rounded-[1rem] p-[0.75rem] text-[#9f9a8f] text-[1rem] bg-transparent focus:outline-none placeholder-[#9f9a8f]"
          ></textarea>
        </div>
      </div>


      <div class="w-full bg-[#FFFFFF] shadow-[0_2px_4px_rgba(0,0,0,0.1)] p-[1.7rem] rounded-[1rem] flex flex-col mb-[4rem]">
        <span class="mb-[1rem]">Sube hasta 5 fotos</span>
        <div class="w-5rem bg-[#FFFFFF] shadow-[0_2px_4px_rgba(0,0,0,0.1)] p-[1.7rem] rounded-[1rem] flex flex-row gap-[4rem]">

          <div class="flex flex-row gap-[4rem]">
            <div
              v-for="(preview, index) in previews"
              :key="index"
              class="border rounded-[1rem] w-[7rem] h-[9rem] flex items-center justify-center cursor-pointer relative overflow-hidden"
              @click="fileInputs[index]?.click()"
            >
              <input
                type="file"
                accept="image/*"
                class="hidden"
                :ref="el => fileInputs[index] = el"
                @change="event => handleImageUpload(event, index)"
              />
              <img
                v-if="preview"
                :src="preview"
                alt="Imagen subida"
                class="w-full h-full object-cover"
              />
              <img
                v-else
                src="/galeria-de-imagenes.png"
                alt="placeholder"
                class="w-[2rem] h-[3rem] rounded-[0.75rem] p-[1rem]"
              />
            </div>
</div>


        </div>
        
      </div>

      <div class="w-full bg-[#FFFFFF] shadow-[0_2px_4px_rgba(0,0,0,0.1)] p-[1.7rem] rounded-[1rem] flex flex-col mb-[4rem] gap-[2rem]">
        <div class="flex flex-row items-center justify-center gap-[1rem]">
          <span class="mb-0">Categoría</span>
          <select class="select_category">
            <option v-for="cat in categorias" :key="cat.id" :value="cat.id">
              {{ cat.name }}
            </option>
          </select>
        </div>

      </div>

      <div class="w-full bg-[#FFFFFF] shadow-[0_2px_4px_rgba(0,0,0,0.1)] p-[1.7rem] rounded-[1rem] flex flex-col mb-[4rem] gap-[2rem]">
        <div class="flex flex-row items-center justify-center gap-[1rem]">
          <span class="mb-0">Estado</span>
          <select class="select_category">
            <option v-for="estado in estados">
              {{ estado.value }}
            </option>
          </select>
        </div>

      </div>

      <div class="w-full bg-[#FFFFFF] shadow-[0_2px_4px_rgba(0,0,0,0.1)] p-[1.7rem] rounded-[1rem] flex flex-col mb-[4rem] gap-[2rem]">
        <div class="flex flex-row items-center justify-center gap-[1rem]">
          <span class="mb-0">Precio</span>
          <input
            v-model="nombre"
            placeholder="Pon un precio razonable..."
            required
            class="flex-1 border-0 border-b border-b-[#9f9a8f] p-[3px] text-[#9f9a8f] text-[1rem] bg-transparent focus:outline-none placeholder-[#9f9a8f]"
          />
        </div>

      </div>

      <button
            @click="checkout(producto)"
            :disabled="comprando"
            class="bg-[#299CA9] border-none text-[#FFFFFF] rounded-[1.2rem] text-[15px] cursor-pointer pt-[0.5rem] pb-[0.5rem] w-fit pl-[3rem] pr-[3rem] disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {{ comprando ? 'Procesando...' : 'Subir' }}
          </button>

    </div>
  </div>

  <!-- Spinner overlay -->
    <div v-if="loading" class="spinner-overlay">
      <div class="spinner"></div>
    </div>
</template>


<script setup>
import { ref, onMounted } from 'vue'
import api from '../services/api'
import NavBar from '../components/NavBar.vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import { watch } from 'vue'

const router = useRouter()
const route = useRoute()

const categorias = ref([])
const estados = ref([])

const imagenes = ref([null, null, null, null, null]) // Para guardar archivos
const previews = ref([null, null, null, null, null]) // Para mostrar imágenes

function handleImageUpload(event, index) {
  const file = event.target.files[0]
  if (file) {
    imagenes.value[index] = file
    previews.value[index] = URL.createObjectURL(file)
  }
}

const fileInputs = [] // Guardamos refs de inputs


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

const loading = ref(false)

onMounted(() => {
  fetchFiltrosOptions()

  loading.value = true

  setTimeout(() => {
    loading.value = false
  }, 300) // puedes ajustar la duración
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

