<template>
  <aside
    class="fixed left-4 top-1/2 transform -translate-y-[45%] bg-[#FFFFFF]"
    id="filterBar"
  >
    <h2 class="text-xl font-semibold mb-4">Filtros</h2>

  <hr>

  <!-- Ordenar por precio -->
    <details class="filtros">
      <summary class="cursor-pointer text-base font-medium">Ordenar por precio</summary>
      <div class="mt-2">
        <select class="select_category">
          <option>Ascendente</option>
          <option>Descendente</option>
        </select>
      </div>
    </details>
    <hr />

    <!-- Filtro por categoría -->
    <details class="filtros">
      <summary class="cursor-pointer text-base font-medium">Categoría</summary>
       <div class="mt-2">
      <select class="select_category">
        <option>Electrónica</option>
        <option>Ropa</option>
        <option>Muebles</option>
      </select>
      </div>
    </details>
    <hr>

    <!-- Filtro por precio -->
    <details class="filtros">
      <summary class="cursor-pointer text-base font-medium">Precio</summary>
      <div class="pt-[1rem]">
        <span>Desde</span>
        <input type="number" class="mt-[rem] ml-[1rem] mr-[0.5rem] w-[4em]">
        <span>€</span>
      </div>
        <!-- haz esto porfa: El desde debe ser mas alto que el hasta -->
      <div class="mt-[1rem]">
        <span>Hasta</span>
        <input type="number" class="mt-[rem] ml-[1rem] mr-[0.5rem] w-[4em]">
        <span>€</span>
      </div>
    </details>

    <hr>

    <!-- Filtro por estado -->
    <details class="mt-[2rem]">
      <summary class="cursor-pointer text-base font-medium">Estado</summary>
      <select class="select_category">
        <option>Como nuevo</option>
        <option>Bueno</option>
        <option>regular</option>
      </select>
    </details>

    <div class="mt-[2rem] p-0 flex">
      <button type="submit" class="bg-[#299CA9] border-none text-[#FFFFFF] rounded-[1.2rem] pt-[10px] pb-[10px] pl-[25px] pr-[25px] text-[15px]">
        Filtrar
      </button>

      <button type="submit" class="bg-[#EC7753] border-none text-[#FFFFFF] rounded-full text-[15px] w-[2.5rem] h-[2.5rem] ml-[1rem]">
        <img src="../assets/papelera.png" alt="papelera" class="w-[1.5rem] h-[1.5rem]">
      </button>
    </div>
  </aside>
</template>

<script setup>
// import papelera from '../assets/papelera.png'
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