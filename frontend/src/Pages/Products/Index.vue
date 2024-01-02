<template>
  <div class="products-index">
    <h1 class="text-3xl underline">Product List</h1>
    <ul>
      <li v-for="product in products">
        <h2 class="text-2xl"><a :href="`/products/show/${product.id}`">{{product.name}}</a></h2>
        <p>{{product.description}}</p>
      </li>

    </ul>
  </div>
</template>

<script setup>
  import { usePage } from '@inertiajs/vue3';
  const { props } = usePage();
  const products = props.products;
  console.log(products)
</script>

<style>
.products-index {
  text-align: center;
  margin-top: 20px;
}
</style>