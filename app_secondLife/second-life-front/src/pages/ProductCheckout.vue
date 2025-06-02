<template>
  <div class="bg-[#FFFDF8] min-h-screen" v-if="producto">
    <NavBar />

    <div class="mt-[8rem] ml-[8rem] mr-[8rem]">
      <h2 class="mb-[2rem]">Comprar artículo</h2>

      <div class=" flex flex-row gap-[3rem] flex-wrap">
        
        <div class="flex flex-col gap-[3rem]">
          <div class="w-[35rem] bg-[#FFFFFF] shadow-[0_2px_4px_rgba(0,0,0,0.1)] p-[1.5rem] pt-[0.5rem] rounded-[1rem] flex flex-col" >
            <p class="text-[0.9rem] text-[#C8C8C8]">Pedido</p>
            <div class="flex flex-row items-center">
              <div>
              <img 
                :src="producto.picture1"
                class="w-[5rem] rounded-[0.5rem]"
              >
              </div>
              <div class="pl-[1.2rem] flex flex-col gap-[0.5rem] w-full">
                <b class="text-[1rem]">{{ producto.name }}</b>
                <div class="flex flex-row justify-between w-full">
                  <span>{{ producto.state }}</span>
                  <span>{{ producto.price }} €</span>
                </div>
              </div>
            </div>
          </div>

          <div class="w-[35rem] bg-[#FFFFFF] shadow-[0_2px_4px_rgba(0,0,0,0.1)] p-[1.5rem] pt-[0.5rem] rounded-[1rem] flex flex-col">
            <p class="text-[0.9rem] text-[#C8C8C8]">Dirección</p>

            <div class="flex items-center w-full mb-[1rem]">
              <b class="mr-[1.5rem] text-[1rem] whitespace-nowrap">Nombre</b>
              <input
                v-model="nombre"
                placeholder="Nombre del comprador"
                required
                class="flex-1 border-0 border-b border-b-[#9f9a8f] p-[3px] text-[#9f9a8f] text-[1rem] bg-[#FFFDF8] focus:outline-none placeholder-[#9f9a8f]"
              />
            </div>

            <div class="flex items-center w-full mb-[1rem]">
              <b class="mr-[1.5rem] text-[1rem] whitespace-nowrap">Calle y código postal</b>
              <input
                v-model="direccion"
                placeholder="Dirección a la que llegará el producto"
                required
                class="flex-1 border-0 border-b border-b-[#9f9a8f] p-[3px] text-[#9f9a8f] text-[1rem] bg-[#FFFDF8] focus:outline-none placeholder-[#9f9a8f]"
              />
            </div>

            <div class="flex items-center w-full">
              <b class="mr-[1.5rem] text-[1rem] whitespace-nowrap">Nº puerta / piso</b>
              <input
                v-model="piso"
                placeholder="Nombre del comprador"
                required
                class="flex-1 border-0 border-b border-b-[#9f9a8f] p-[3px] text-[#9f9a8f] text-[1rem] bg-[#FFFDF8] focus:outline-none placeholder-[#9f9a8f]"
              />
            </div>
          </div>


        </div>

        
        
        <div class="w-[27rem] h-[15.5rem] bg-[#FFFFFF] shadow-[0_2px_4px_rgba(0,0,0,0.1)] p-[1.5rem] pt-[0.5rem] rounded-[1rem] flex flex-col gap-[1.5rem]" >
          <p class="text-[1.1rem] text-[#C8C8C8]">Desglose del pedido</p>
          <div class="flex flex-row justify-between items-center w-full mt-2">
            <span>Precio del producto:</span>
            <span>{{ producto.price }} €</span>
          </div>
          <div class="flex flex-row gap-[2rem] mt-4 items-center">
            <label class="flex items-center  cursor-pointer">
              <input
                type="radio"
                name="entrega"
                value="en_persona"
                v-model="tipoEntrega"
                class="accent-[#299CA9] align-middle"
                checked
              />
              <span class="ml-[0.5rem] align-middle text-[1rem]">En persona</span>
            </label>

            <label class="flex items-center  cursor-pointer">
              <input
                type="radio"
                name="entrega"
                value="direccion"
                v-model="tipoEntrega"
                class="accent-[#299CA9] align-middle"
              />
              <span class="ml-[0.5rem] align-middle text-[1rem]">Dirección establecida</span>
            </label>
          </div>

          <div class="flex flex-row justify-between items-center w-full mt-2">
            <span>Precio de envío:</span>
            <span>{{ precioEnvio }} €</span>
          </div>

          <div class="flex flex-row justify-between items-center w-full mt-2">
            <h3 class="mb-[2rem]">Total a pagar:</h3>
            <span>{{ total }} €</span>
          </div>

          <button @click="checkout(producto)" class="bg-[#299CA9] border-none text-[#FFFFFF] rounded-[1.2rem] text-[15px] cursor-pointer pt-[0.5rem] pb-[0.5rem] w-fit pl-[3rem] pr-[3rem]">
          Pagar
          </button>
        </div>
        

        
      </div>
    </div>
    
  </div>
</template>

<script setup>
import { ref, onMounted, computed, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import api from '../services/api'
import NavBar from '../components/NavBar.vue'
import { nextTick } from 'vue'
import router from '../router'

const route = useRoute()
const tipoEntrega = ref('en_persona')
const precioEnvio = ref(0)
const nombre = ref('')
const direccion = ref('')
const piso = ref('')
const backendURL = 'http://localhost:8000'

// Precio total dinámico
const total = computed(() => {
  return producto.value ? producto.value.price + precioEnvio.value : 0
})

// Validar campos dirección
const direccionCompleta = computed(() => {
  return nombre.value.trim() && direccion.value.trim() && piso.value.trim()
})

// Watch para actualizar precioEnvio
watch(tipoEntrega, async (nuevoValor, anteriorValor) => {
  if (nuevoValor === 'direccion') {
    if (direccionCompleta.value) {
      precioEnvio.value = 5
    } else {
      alert('Completa todos los campos de dirección antes de seleccionar esta opción.')
      await nextTick()
      // nextTick() espera a que Vue procese los cambios antes de re-asignar el valor de tipoEntrega, evitando inconsistencias o errores.
      tipoEntrega.value = 'en_persona'
    }
  } else {
    precioEnvio.value = 0
  }
})

const producto = ref(null)
const loading = ref(true)

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

const checkout = async (producto) => {
  // Compruebo de nuevo que si ha puesto la direccion habiendo elegido esa opcion
  if (tipoEntrega.value === 'direccion' && !direccionCompleta.value) {
    alert('Debes completar todos los campos de dirección.')
    return
  }

  try{
    const res = await api.post(`/products/${producto.id}/mark_sold/`)
    alert("Compra realizada con éxito")
    router.push('/home')
  } catch (error) {
    console.error('Error al marcar como vendido: ', error)
    alert('Hubo un error al procesar la compra. Intenta de nuevo.')
  }
}

</script>
