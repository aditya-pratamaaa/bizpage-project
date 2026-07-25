<template>
	<MainLayout :role="currentUser.role" :user="currentUser">
		<!-- Isinya bebas kamu racik di sini, otomatis masuk ke area konten kanan -->
		<div class="mb-6">
			<h1 class="text-2xl font-bold text-slate-900">Dashboard</h1>
			<p class="mt-1 text-sm text-slate-500">Ringkasan performa bisnis kamu hari ini.</p>
		</div>

		<div
			class="border-2 border-dashed border-slate-300 rounded-2xl h-[calc(100vh-14rem)] flex items-center justify-center bg-white"
		>
			<div class="text-center">
				<h2 class="text-xl font-semibold text-slate-400">Konten Dashboard Utama</h2>
				<p class="text-sm text-slate-400 mt-1">
					Tinggal isi statistik, tabel produk, atau grafik di sini.
				</p>
			</div>
		</div>
	</MainLayout>
</template>

<script setup>
import MainLayout from "../../../components/main-layout.vue";

// Nantinya ini idealnya datang dari auth store / composable (mis. useAuth()),
// bukan hardcode seperti ini. Untuk sekarang dipakai sebagai contoh saja.
const currentUser = {
	role: "owner", // atau "admin" — ini yang mengontrol menu apa saja yang tampil
	name: "Tom Cook",
	avatar: "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80",
};
</script>
