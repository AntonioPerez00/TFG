<template>
  <nav :class="['navbar', { 'navbar-hidden': !isVisible }]">
    <div class="logo-container cursor-pointer" @click="goToHome">
      <img src="/SecondLifeIcon.png" alt="Logo" class="logo-img" />
      <div class="logo">SecondLife</div>
    </div>

    <div class="search-container">
      <input
        type="text"
        v-model="searchQuery"
        placeholder="Buscar..."
        class="search-input"
        @keyup.enter="handleSearch"
      />
      <button class="search-button" @click="handleSearch">Buscar</button>
    </div>

    <div class="relative menu menu" @click="toggleDropdown">
      <span class="nombre-usuario">
        {{ nombreUsuario || 'Iniciar sesión' }}
      </span>
      <img
        :src="profile_pic || '/usuario.png'"
        alt="usuario"
        class="w-[2.5rem] h-[2.5rem] rounded-full"
      />
      <div
        v-if="dropdownVisible"
        class="absolute mt-[8rem] w-40 bg-[#FFFFFF] shadow-lg z-50 pl-[1rem] pr-[1rem] rounded-[1rem] shadow-[0_2px_4px_rgba(0,0,0,0.1)] z-[9999]"
      >
        
          <p
            class="px-4 py-2 hover:bg-gray-100 cursor-pointer"
            @click.stop="goToProfile"
          >
            Mi perfil
          </p>
          <p
            class="px-4 py-2 hover:bg-gray-100 cursor-pointer"
            @click.stop="cerrarSesion"
          >
            Cerrar sesión
          </p>
        
      </div>
    </div>

      <!-- <div class="menu">
            <span class="nombre-usuario">
      {{ nombreUsuario || 'Iniciar sesión' }}
    </span>
            <img src="/usuario.png" alt="usurio" class="usuario-img" />
        </div> -->
  </nav>

  
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { useRoute } from 'vue-router'

const route = useRoute()
const isVisible = ref(true)
const searchQuery = ref(route.query.search || '')
const nombreUsuario = ref('')
const profile_pic = ref('')
let lastScrollY = window.scrollY // Guarda la posición previa del scroll
const router = useRouter()
const dropdownVisible = ref(false)

async function cerrarSesion() {
  dropdownVisible.value = false

  
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
      localStorage.removeItem('name')
      localStorage.removeItem('mail')
      localStorage.removeItem('profile_pic')

       // Actualiza los valores reactivos
  nombreUsuario.value = ''
  profile_pic.value = ''

  // Redirige al usuario si lo deseas (opcional)
  router.push('/home')  // o cualquier ruta pública, como '/login'

}


function toggleDropdown() {
  dropdownVisible.value = !dropdownVisible.value
}

function goToProfile() {
  dropdownVisible.value = false
  const url = router.resolve(`/user/${localStorage.getItem('mail')}`).href
  router.push(url)
}

function handleClickOutside(event) {
  const menuElement = document.querySelector('.menu')
  if (menuElement && !menuElement.contains(event.target)) {
    dropdownVisible.value = false
  }
}

function goToHome() {
  router.push('/home')
}

function userDetails() {
  const url = router.resolve(`/user/${localStorage.getItem('mail')}`).href
  router.push(url)
}

nombreUsuario.value = localStorage.getItem('name')
profile_pic.value = localStorage.getItem('profile_pic')

function handleScroll() {
  const currentY = window.scrollY // Posición actúal
  isVisible.value = currentY < lastScrollY || currentY < 10
  lastScrollY = currentY
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
    window.addEventListener('click', handleClickOutside)
})
onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
    window.removeEventListener('click', handleClickOutside)

})

const emit = defineEmits(['buscar'])

function handleSearch() {
  localStorage.setItem('lastSearch', searchQuery.value)
  router.push({ path: '/home', query: { search: searchQuery.value } }) // Envía búsqueda como query
  emit('buscar', searchQuery.value) // Por si estás en Home
}

</script>

<style>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  background-color: white;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  z-index: 50;
  padding: 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  transition: transform 0.3s ease;
  transform: translateY(0);
  height: 80px; /* Aumenta la altura para más espacio */
  box-sizing: border-box;
}

.navbar-hidden {
  transform: translateY(-100%);
}

.logo-container {
  display: flex;
  align-items: center;
  gap: 10px;
  z-index: 1;
}

.logo-img {
  width: 30px;
  margin: 0;
}

.logo {
  font-size: 2rem;
  font-weight: bold;
}

.search-container {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  align-items: center;
  gap: 10px;
}

.search-input {
  padding: 8px 10px;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 18px;
  width: 25rem;
  margin: 0;
}

.search-input:focus {
  border-color: #299CA9;
}

.search-button {
  padding: 8px 20px;
  background-color: #299CA9;
  border: none;
  color: white;
  border-radius: 18px;
  cursor: pointer;
  margin: 0;
}

.search-button:hover {
  background-color: #217d86;
}

.menu {
  display: flex;
  align-items: center;
  cursor: pointer;
  padding: 6px;
  margin-left: auto; /* empuja a la derecha */
}

.menu:hover{
  background-color: #eeeded;
  padding: 6px;
  border-radius: 20px;
}

.usuario-img{
    width: 30px;
    margin: 0;
}

.nombre-usuario{
    margin-top: 4px;
    font-size: 18px;
    margin-right: 10px;
}

.content {
  margin-top: 80px; /* espacio para que el navbar fijo no tape el contenido */
  padding: 20px;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
  font-family: Arial, sans-serif;
  line-height: 1.6;
}
</style>
