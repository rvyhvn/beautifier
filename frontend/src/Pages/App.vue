<template>
  <Layout>    
    <div class="container border mx-auto">
      <div class="grid-rows-8">
        <div class="size-24">Banner</div>
        <div class="size-24">Recommended</div>
        <div class="size-24">Show case</div>
        <div class="size-24">Best sellers</div>
        <div class="size-24">Advantages</div>
        <div class="size-24">Comments from buyers</div>
        <div class="size-24">As seen in</div>
        <div class="size-24">Latest (instagram contents)</div>
      </div>
    </div>
  </Layout>
</template>
<script setup>
import { usePage } from '@inertiajs/vue3';
import IndexProduct from './Products/IndexProduct.vue';
import Layout from '@/components/Layout/Layout.vue';

const { props } = usePage();
const products = props.products;
console.log(products);
</script>
