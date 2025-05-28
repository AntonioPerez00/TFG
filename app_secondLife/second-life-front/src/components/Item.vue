<template>
  <div class="flex flex-col">
    <img
      :src="producto.picture || '/usuario.png'"
      alt="usuario"
      class="w-[9rem] h-[12rem] rounded-[0.75rem] mb-[0.5rem]"
    />
    <div class="flex flex-col pl-[0.4rem] gap-[0.2rem]">
      <span><b>{{ producto.name }}</b></span>
      <span>{{ producto.price }} €</span>
      <span>{{ producto.state }}</span>
    </div>
  </div>
</template>

<script setup>
defineProps({
  producto: Object
})
</script>
