<template>
  <aside
    class="fixed left-4 top-1/2 transform -translate-y-[50%] bg-[#FFFFFF]"
    id="filterBar"
  >
    <h2 class="text-xl font-semibold mb-4">Filtros</h2>

  <hr>

    <!-- Filtro por categoría -->
    <div class="filtros">
      <label class="label_category">Categoría</label>
      <select class="select_category">
        <option>Electrónica</option>
        <option>Ropa</option>
        <option>Muebles</option>
      </select>
    </div>
    <hr>

    <!-- Filtro por precio -->
    <div class="filtros">
      <label>Precio máximo</label>
      <input type="range" min="0" max="100000" class="w-full" />
      <span>10.000</span>
    </div>

    <hr>

    <!-- Filtro por estado -->
    <div class="filtros">
      <label class="label_category">Estado</label>
      <select class="select_category">
        <option>Como nuevo</option>
        <option>Bueno</option>
        <option>regular</option>
      </select>
    </div>

    
  </aside>
</template>

<script setup>
// Todo estático por ahora
</script>

<style>

#filterBar{
  padding: 40px;
  padding-top: 10px;
  margin-left: 30px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  border-radius: 20px;
  width: 10rem;
}

.filtros{
  margin-top: 20px;
  margin-bottom: 30px;
}

.label_category{
  font-size: 17px;
}

.select_category{
  width: 100%;
  margin-top: 0.75rem;
  border-radius: 10px;
  padding: 5px;
}

</style>