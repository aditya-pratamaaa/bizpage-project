<template>
	<MainLayout :role="currentUser.role" :user="currentUser">
		<header class="flex items-center justify-between">
			<h1 class="text-2xl font-semibold text-slate-800">Daftar Produk</h1>

			<div class="flex items-center gap-3">
				<div class="relative w-80">
					<span
						class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none text-slate-400"
					>
						<i class="mdi mdi-magnify text-base"></i>
					</span>

					<input
						type="text"
						placeholder="Cari produk..."
						class="w-full pl-10 pr-4 py-2 bg-slate-100 rounded-lg text-sm text-slate-700 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-[var(--color-focus-ring)]"
					/>
				</div>

				<button
					class="px-4 py-2 rounded-lg bg-[var(--color-primary)] text-white text-sm font-medium hover:opacity-90 transition"
				>
					<i class="mdi mdi-plus mr-1"></i>
					Tambah Produk
				</button>
			</div>
		</header>
		<!-- <div v-for="product in productList" :key="product.name"></div> -->
	</MainLayout>
</template>

<script setup>
import { createResource } from "frappe-ui";
import { ref } from "vue";
import MainLayout from "../../../../../components/main-layout.vue";

// const productList = createResource({
// 	url: bizpage.api.product_api.get_product_list,
// });

// Nantinya ini idealnya datang dari auth store / composable (mis. useAuth()),
// bukan hardcode seperti ini. Untuk sekarang dipakai sebagai contoh saja.
const currentUser = {
	role: "owner", // atau "admin" — ini yang mengontrol menu apa saja yang tampil
	name: "Tom Cook",
	avatar: "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80",
};
</script>
