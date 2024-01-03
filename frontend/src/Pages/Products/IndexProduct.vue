<template>
  <Layout />
  <div class="products-index">
    <h2>Halo {{ user }}</h2>
    <h1 class="text-3xl underline">Product List</h1>
    <ul>
      <li v-for="product in products" :key="product.id">
        <h2 class="text-2xl">
          <a :href="`/products/show/${product.id}`">{{ product.name }}</a>
        </h2>
        <p>{{ product.description }}</p>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { usePage } from '@inertiajs/vue3';
import Layout from '@/components/Layout/Layout.vue';
const { props } = usePage();
const products = props.products;
const user = props.user_info;
console.log(products);
</script>

<style>
.products-index {
  text-align: center;
  margin-top: 20px;
}
</style>
