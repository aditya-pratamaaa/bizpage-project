<template>
	<MainLayout :role="currentUser.role" :user="currentUser">
		<div>Ini Prodcut Namanya</div>
	</MainLayout>
</template>

<script setup>
import MainLayout from "../../../../../components/main-layout.vue";

// Nantinya ini idealnya datang dari auth store / composable (mis. useAuth()),
// bukan hardcode seperti ini. Untuk sekarang dipakai sebagai contoh saja.
const currentUser = {
	role: "owner", // atau "admin" — ini yang mengontrol menu apa saja yang tampil
	name: "Tom Cook",
	avatar: "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80",
};
</script>
