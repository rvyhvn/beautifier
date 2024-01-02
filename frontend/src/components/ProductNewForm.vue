<template>
<form @submit.prevent="form.post('/products/new')">
	<!-- email -->
	<input type="text" v-model="form.email">
	<div v-if="form.errors.email">{{ form.errors.email }}</div>
	<!-- password -->
	<input type="password" v-model="form.password">
	<div v-if="form.errors.password">{{ form.errors.password }}</div>
	<!-- remember me -->
	<input type="checkbox" v-model="form.remember"> Remember Me
	<!-- submit -->
	<button type="submit" :disabled="form.processing">Login</button>
</form>
</template>

<script setup>	
import { useForm } from '@inertiajs/vue3'

const form = useForm({
  email: null,
  password: null,
  remember: false,
})

</script>