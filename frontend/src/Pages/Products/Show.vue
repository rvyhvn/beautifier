<template>
  <div class="product-details">
    <h1>Product Details</h1>
    <div v-if="product">
      <h2>{{ product }}</h2>
    </div>
    <p v-else>Loading...</p>
  </div>
</template>

<script setup>
import { usePage } from "@inertiajs/vue3";
const { props } = usePage();
const product = props.product_name
</script>

<style>
.product-details {
  text-align: center;
  margin-top: 20px;
}
</style>
