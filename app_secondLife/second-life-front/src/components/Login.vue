<template>
  <form @submit.prevent="$emit('authenticated')" class="space-y-4">
    <input type="email" placeholder="E-mail" class="w-full p-2 border rounded" required />
    <input type="password" placeholder="Contraseña" class="w-full p-2 border rounded" required />
    <button type="submit" class="w-full bg-teal-500 hover:bg-teal-600 text-white p-2 rounded">
      Continuar
    </button>
  </form>
</template>
