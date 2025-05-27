<template>
  <div class="bg-[#FFFDF8]">
    <NavBar />
    <div class="pt-20 px-8 flex gap-6">
      <Filtros />

     

        <!-- Contenido principal -->
        <main class="flex flex-col mt-[80px] p-[20px] ml-[20rem]">
          <h1 class="text-2xl font-bold">Bienvenido a SecondLife</h1>
          <div class="flex flex-wrap gap-[4rem]">
            <Item v-for="n in 40" :key="n" />
          </div>
        </main>
      
    </div>
  </div>
</template>

<script setup>
import NavBar from '../components/NavBar.vue'
import Filtros from '../components/FilterBar.vue'
import Item from '../components/Item.vue'
</script>
