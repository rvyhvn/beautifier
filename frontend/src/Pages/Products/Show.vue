<template>
  <div class="product-details">
    <h1 class="text-3xl underline">Product Detail</h1>
    <div v-if="product">
      <h2 class="text-2xl">{{ product.name }}</h2>
      <p>{{product.description}}</p>
      <h3 class="text-xl">Price: {{product.price}}</h3>
      <h3 class="text-xl">Stock: {{product.stock}}</h3>
    </div>
    <p v-else>Loading...</p>
  </div>
</template>

<script setup>
import { usePage } from "@inertiajs/vue3";
const { props } = usePage();
const product = props.product_detail;
console.log(product);
</script>

<style>
.product-details {
  text-align: center;
  margin-top: 20px;
}
</style>
