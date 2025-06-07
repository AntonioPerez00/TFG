<template>
  <div class="w-full h-full bg-[#FFFDF8] flex flex-col items-center">
    <NavBar />

    <div class="mt-[7rem] w-full max-w-[40rem] px-[2rem]">

      <!-- Imagen de perfil y botón -->
      <div class="flex flex-col items-center mb-[2rem]">
        <img
          :src="profile_pic || '/usuario.png'"
          alt="usuario"
          class="w-[10rem] h-[10rem] rounded-full object-cover mb-[1rem]"
        />
        <label class="cursor-pointer bg-[#E5E7EB] px-[1rem] py-[0.5rem] rounded-[1rem] text-[0.9rem] hover:bg-[#d1d5db] transition-colors">
          Cambiar foto
          <input type="file" class="hidden" @change="onProfilePicChange" />
        </label>
      </div>

      <!-- Formulario -->
      <form class="flex flex-col gap-[1.5rem]">
        <!-- Nombre -->
        <div class="flex flex-col">
          <label class="text-[1rem] mb-[0.5rem]">Nombre</label>
          <input
            type="text"
            v-model="nombreUsuario"
            class="border border-[#D1D5DB] rounded-[1rem] p-[0.8rem] text-[1rem] focus:outline-none focus:ring-2 focus:ring-[#A0AEC0]"
          />
        </div>

        <!-- Localización -->
        <div class="flex flex-col">
          <label class="text-[1rem] mb-[0.5rem]">Localización</label>
          <input
            type="text"
            v-model="localizacion"
            class="border border-[#D1D5DB] rounded-[1rem] p-[0.8rem] text-[1rem] focus:outline-none focus:ring-2 focus:ring-[#A0AEC0]"
          />
        </div>

        <!-- Descripción -->
        <div class="flex flex-col">
          <label class="text-[1rem] mb-[0.5rem]">Descripción</label>
          <textarea
            v-model="descripcion"
            rows="4"
            class="border border-[#D1D5DB] rounded-[1rem] p-[0.8rem] text-[1rem] resize-none focus:outline-none focus:ring-2 focus:ring-[#A0AEC0]"
          ></textarea>
        </div>

        <!-- Botón Guardar -->
        <button
          type="button"
          class="bg-[#299CA9] text-[#FFFFFF] border-none cursor-pointer py-[0.8rem] rounded-[1rem] text-[1rem] hover:bg-[#217d86] transition-colors"
        >
          Guardar cambios
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import NavBar from '../components/NavBar.vue'

// Método para que no devuelva un string "null"
function safeGet(key) {
  const value = localStorage.getItem(key)
  return value === null || value === 'null' ? '' : value
}

const nombreUsuario = ref(safeGet('name'))
const profile_pic = ref(safeGet('profile_pic'))
const localizacion = ref(safeGet('location'))
const descripcion = ref(safeGet('profile_desc'))

function onProfilePicChange(event) {
  const file = event.target.files[0]
  if (file) {
    const reader = new FileReader()
    reader.onload = () => {
      profile_pic.value = reader.result
    }
    reader.readAsDataURL(file)
  }
}
</script>
