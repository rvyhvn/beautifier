<template>
  <Layout>    
    <div class="container border mx-auto">
      <div class="grid-rows-8">
        <h3>{{property}}</h3>
      </div>
    </div>
  </Layout>
</template>
<script setup>
import { usePage } from '@inertiajs/vue3';
import IndexProduct from './Products/IndexProduct.vue';
import Layout from '@/components/Layout/Layout.vue';

const { props } = usePage();
const property = props.title;
console.log(property);
</script>
