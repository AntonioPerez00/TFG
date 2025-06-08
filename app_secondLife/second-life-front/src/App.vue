<template>
  <div>
    <router-view />
  </div>
</template>

<script setup>
import { ref } from 'vue'
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;700&display=swap');

  /* Fuente general para casi todo el texto */
  body, div, section, article, header, footer, main, aside,
  h1, h2, h3, h4, h5, h6,
  p, span, label, button, input, textarea, select,
  a, li, ul, ol, dt, dd, small, strong, em {
  font-family: 'Nunito', sans-serif;
    color: #000000;
  }

  button {
    cursor: pointer;
  }

  input, select, textarea {
    font-family: inherit;
  }
</style>
