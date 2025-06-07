<template>
  <div class="w-full h-full bg-[#FFFDF8] flex flex-col items-center">
    <NavBar />

    <div class="mt-[7rem] w-full max-w-[40rem] px-[2rem]">

      <!-- Imagen de perfil y botón -->
      <div class="flex flex-col items-center mb-[2rem]">
        <img
  :src="profilePreview || '/usuario.png'"
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
          @click="guardarCambios"
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
import axios from 'axios'
import api from '../services/api'

function safeGet(key) {
  const value = localStorage.getItem(key)
  return value === null || value === 'null' ? '' : value
}

const nombreUsuario = ref(safeGet('name'))
const profile_pic = ref(null) // Ahora será el File, no base64
const profilePreview = ref(safeGet('profile_pic')) // Para previsualizar la imagen
const localizacion = ref(safeGet('location'))
const descripcion = ref(safeGet('profile_desc'))

async function guardarCambios() {
  const token = localStorage.getItem('access_token')
  if (!token) {
    alert('No estás autenticado')
    return
  }

  if (!nombreUsuario.value.trim()) {
    alert('El nombre es obligatorio')
    return
  }

  const formData = new FormData()
  formData.append('name', nombreUsuario.value.trim())

  if (localizacion.value.trim() !== '') {
    formData.append('location', localizacion.value.trim())
  }
  if (descripcion.value.trim() !== '') {
    formData.append('profile_desc', descripcion.value.trim())
  }
  if (profile_pic.value) {
    formData.append('profile_pic', profile_pic.value)
  }

  try {
    const res = await api.put('/profile/', formData, {
      headers: {
        Authorization: `Bearer ${token}`,
        'Content-Type': 'multipart/form-data',
      },
    })

    alert('Perfil actualizado correctamente')
    localStorage.setItem('name', res.data.name || '')
    localStorage.setItem('location', res.data.location || '')
    localStorage.setItem('profile_desc', res.data.profile_desc || '')
    localStorage.setItem('profile_pic', 'http://localhost:8000' + res.data.profile_pic || '')

    window.location.reload()

  } catch (error) {
    const data = error.response?.data || {}
    const msg =
      typeof data === 'string'
        ? data
        : data.detail || data.message || JSON.stringify(data.errors || data)

    alert('Error al actualizar: ' + msg)
  }
}


function onProfilePicChange(event) {
  const file = event.target.files[0]
  if (file) {
    profile_pic.value = file

    const reader = new FileReader()
    reader.onload = () => {
      profilePreview.value = reader.result
    }
    reader.readAsDataURL(file)
  }
}

</script>
