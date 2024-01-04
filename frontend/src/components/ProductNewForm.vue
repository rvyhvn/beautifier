<template>
	<form @submit.prevent="form.post('/products/new')">
		<!-- email -->
		<input type="text" v-model="form.name" />
		<div v-if="form.errors.name">{{ form.errors.name }}</div>
		<!-- password -->
		<input type="text" v-model="form.description" />
		<div v-if="form.errors.description">{{ form.errors.description }}</div>
		<!-- remember me -->
		<input type="text" v-model="form.price" />
		<div v-if="form.errors.price">{{ form.errors.price }}</div>
		<input type="text" v-model="form.stock" />
		<div v-if="form.errors.stock">{{ form.errors.stock }}</div>
		<!-- submit -->
		<button type="submit" :disabled="form.processing">Submit</button>
	</form>
</template>

<script setup>
import { useForm } from '@inertiajs/vue3';

const form = useForm({
	name: null,
	description: null,
	price: null,
	stock: null
});
</script>
