<template>
	<MainLayout>
		<header class="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
			<div>
				<h1 class="text-2xl font-semibold text-slate-800">Daftar Produk</h1>
				<p class="mt-1 text-sm text-slate-500">
					{{ productList.data?.total ?? 0 }} produk terdaftar
				</p>
			</div>

			<div class="flex items-center gap-3">
				<div class="relative w-full sm:w-80">
					<span
						class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none text-slate-400"
					>
						<i class="mdi mdi-magnify text-base"></i>
					</span>

					<input
						v-model="searchQuery"
						@input="handleSearchInput"
						type="text"
						placeholder="Cari produk..."
						class="w-full pl-10 pr-4 py-2 bg-slate-100 rounded-lg text-sm text-slate-700 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-[var(--color-focus-ring)]"
					/>
				</div>

				<button
					type="button"
					class="shrink-0 px-4 py-2 rounded-lg bg-[var(--color-primary)] text-white text-sm font-medium hover:opacity-90 transition"
				>
					<i class="mdi mdi-plus mr-1"></i>
					Tambah Produk
				</button>
			</div>
		</header>

		<!-- Loading -->
		<div v-if="productList.loading && !productList.data" class="mt-6 space-y-2">
			<div v-for="i in 6" :key="i" class="h-14 animate-pulse rounded-xl bg-slate-100"></div>
		</div>

		<!-- Error -->
		<div
			v-else-if="productList.error"
			class="mt-6 flex flex-col items-center justify-center gap-3 rounded-xl border border-slate-200 bg-slate-50 py-16 text-center"
		>
			<p class="text-sm font-medium text-[var(--color-danger)]">
				{{ productList.error.messages?.[0] || "Gagal memuat daftar produk." }}
			</p>
			<button
				type="button"
				@click="productList.reload()"
				class="rounded-lg bg-[var(--color-primary)] px-4 py-2 text-sm font-medium text-white hover:opacity-90"
			>
				Coba lagi
			</button>
		</div>

		<!-- Empty -->
		<div
			v-else-if="!products.length"
			class="mt-6 flex flex-col items-center justify-center gap-2 rounded-xl border border-dashed border-slate-300 py-16 text-center"
		>
			<i class="mdi mdi-package-variant text-3xl text-slate-300"></i>
			<p class="text-sm font-medium text-slate-700">Belum ada produk yang cocok</p>
			<p class="text-sm text-slate-500">Coba ubah kata kunci pencarian.</p>
		</div>

		<template v-else>
			<!-- Desktop: table -->
			<div class="mt-6 hidden overflow-x-auto rounded-xl border border-slate-200 md:block">
				<table class="min-w-full divide-y divide-slate-200">
					<thead class="bg-slate-50">
						<tr>
							<th
								class="px-4 py-3 text-left text-xs font-semibold uppercase tracking-wide text-slate-500"
							>
								Produk
							</th>
							<th
								class="px-4 py-3 text-left text-xs font-semibold uppercase tracking-wide text-slate-500"
							>
								SKU
							</th>
							<th
								class="px-4 py-3 text-left text-xs font-semibold uppercase tracking-wide text-slate-500"
							>
								Kategori
							</th>
							<th
								class="px-4 py-3 text-right text-xs font-semibold uppercase tracking-wide text-slate-500"
							>
								Harga
							</th>
							<th
								class="px-4 py-3 text-right text-xs font-semibold uppercase tracking-wide text-slate-500"
							>
								Stok
							</th>
							<th
								class="px-4 py-3 text-left text-xs font-semibold uppercase tracking-wide text-slate-500"
							>
								Status
							</th>
							<th
								class="px-4 py-3 text-right text-xs font-semibold uppercase tracking-wide text-slate-500"
							>
								Aksi
							</th>
						</tr>
					</thead>
					<tbody class="divide-y divide-slate-200 bg-white">
						<tr v-for="p in products" :key="p.name" class="hover:bg-slate-50">
							<td class="px-4 py-3">
								<div class="flex items-center gap-3">
									<img
										:src="p.image || placeholderImage"
										:alt="p.product_name"
										class="h-9 w-9 flex-shrink-0 rounded-lg object-cover ring-1 ring-slate-200"
									/>
									<div class="min-w-0">
										<p class="truncate text-sm font-medium text-slate-800">
											{{ p.product_name }}
										</p>
										<p class="truncate text-xs text-slate-400">{{ p.name }}</p>
									</div>
								</div>
							</td>
							<td class="px-4 py-3 text-sm text-slate-600">{{ p.sku || "—" }}</td>
							<td class="px-4 py-3 text-sm text-slate-600">
								{{ p.category || "—" }}
							</td>
							<td class="px-4 py-3 text-right text-sm font-medium text-slate-800">
								{{ formatCurrency(p.price) }}
							</td>
							<td class="px-4 py-3 text-right text-sm text-slate-600">
								{{ p.stock_qty ?? 0 }}
							</td>
							<td class="px-4 py-3">
								<span
									:class="statusBadgeClass(p.status)"
									class="inline-flex items-center rounded-full px-2.5 py-1 text-xs font-medium"
								>
									{{ statusLabel(p.status) }}
								</span>
							</td>
							<td class="px-4 py-3">
								<div class="flex items-center justify-end gap-1">
									<button
										type="button"
										title="Lihat"
										@click="viewProduct(p)"
										class="flex h-8 w-8 items-center justify-center rounded-lg text-slate-500 hover:bg-slate-100 hover:text-slate-700"
									>
										<i class="mdi mdi-eye-outline text-base"></i>
									</button>
									<button
										type="button"
										title="Edit"
										@click="editProduct(p)"
										class="flex h-8 w-8 items-center justify-center rounded-lg text-slate-500 hover:bg-[var(--color-primary-light)] hover:text-[var(--color-primary)]"
									>
										<i class="mdi mdi-pencil-outline text-base"></i>
									</button>
									<button
										type="button"
										title="Hapus"
										@click="askDelete(p)"
										class="flex h-8 w-8 items-center justify-center rounded-lg text-slate-500 hover:bg-red-50 hover:text-[var(--color-danger)]"
									>
										<i class="mdi mdi-trash-can-outline text-base"></i>
									</button>
								</div>
							</td>
						</tr>
					</tbody>
				</table>
			</div>

			<!-- Mobile: cards -->
			<div class="mt-6 space-y-3 md:hidden">
				<div
					v-for="p in products"
					:key="p.name"
					class="rounded-xl border border-slate-200 bg-white p-4"
				>
					<div class="flex items-start gap-3">
						<img
							:src="p.image || placeholderImage"
							:alt="p.product_name"
							class="h-11 w-11 flex-shrink-0 rounded-lg object-cover ring-1 ring-slate-200"
						/>
						<div class="min-w-0 flex-1">
							<div class="flex items-start justify-between gap-2">
								<p class="truncate text-sm font-medium text-slate-800">
									{{ p.product_name }}
								</p>
								<span
									:class="statusBadgeClass(p.status)"
									class="inline-flex flex-shrink-0 items-center rounded-full px-2 py-0.5 text-xs font-medium"
								>
									{{ statusLabel(p.status) }}
								</span>
							</div>
							<p class="mt-0.5 text-xs text-slate-400">
								{{ p.sku || p.name }} &middot; {{ p.category || "Tanpa kategori" }}
							</p>
							<div class="mt-2 flex items-center justify-between">
								<div class="text-sm">
									<span class="font-medium text-slate-800">{{
										formatCurrency(p.price)
									}}</span>
									<span class="text-slate-500">
										&middot; stok {{ p.stock_qty ?? 0 }}</span
									>
								</div>
								<div class="flex items-center gap-1">
									<button
										type="button"
										title="Lihat"
										@click="viewProduct(p)"
										class="flex h-8 w-8 items-center justify-center rounded-lg text-slate-500 hover:bg-slate-100"
									>
										<i class="mdi mdi-eye-outline text-base"></i>
									</button>
									<button
										type="button"
										title="Edit"
										@click="editProduct(p)"
										class="flex h-8 w-8 items-center justify-center rounded-lg text-slate-500 hover:bg-[var(--color-primary-light)] hover:text-[var(--color-primary)]"
									>
										<i class="mdi mdi-pencil-outline text-base"></i>
									</button>
									<button
										type="button"
										title="Hapus"
										@click="askDelete(p)"
										class="flex h-8 w-8 items-center justify-center rounded-lg text-slate-500 hover:bg-red-50 hover:text-[var(--color-danger)]"
									>
										<i class="mdi mdi-trash-can-outline text-base"></i>
									</button>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>

			<!-- Pagination -->
			<div class="mt-4 flex flex-col items-center justify-between gap-3 sm:flex-row">
				<p class="text-xs text-slate-500">
					Menampilkan {{ rangeStart }}–{{ rangeEnd }} dari {{ totalCount }} produk
				</p>
				<div class="flex items-center gap-2">
					<button
						type="button"
						:disabled="page === 1"
						@click="prevPage"
						class="rounded-lg border border-slate-200 px-3 py-1.5 text-sm text-slate-700 disabled:cursor-not-allowed disabled:opacity-40 enabled:hover:bg-slate-50"
					>
						Sebelumnya
					</button>
					<span class="text-sm text-slate-600">Hal. {{ page }} / {{ totalPages }}</span>
					<button
						type="button"
						:disabled="page >= totalPages"
						@click="nextPage"
						class="rounded-lg border border-slate-200 px-3 py-1.5 text-sm text-slate-700 disabled:cursor-not-allowed disabled:opacity-40 enabled:hover:bg-slate-50"
					>
						Berikutnya
					</button>
				</div>
			</div>
		</template>

		<!-- Modal konfirmasi hapus -->
		<div
			v-if="deleteTarget"
			class="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/40 p-4"
			@click.self="deleteTarget = null"
		>
			<div class="w-full max-w-sm rounded-xl bg-white p-5">
				<h3 class="text-base font-semibold text-slate-800">Hapus produk?</h3>
				<p class="mt-1.5 text-sm text-slate-500">
					"{{ deleteTarget.product_name }}" akan dihapus permanen. Tindakan ini tidak
					bisa dibatalkan.
				</p>
				<div class="mt-5 flex justify-end gap-2">
					<button
						type="button"
						@click="deleteTarget = null"
						class="rounded-lg px-4 py-2 text-sm font-medium text-slate-700 hover:bg-slate-100"
					>
						Batal
					</button>
					<button
						type="button"
						@click="confirmDelete"
						:disabled="deleteResource.loading"
						class="rounded-lg bg-[var(--color-danger)] px-4 py-2 text-sm font-medium text-white hover:bg-[var(--color-danger-hover)] disabled:opacity-60"
					>
						{{ deleteResource.loading ? "Menghapus..." : "Ya, hapus" }}
					</button>
				</div>
			</div>
		</div>
	</MainLayout>
</template>

<script setup>
import { createResource } from "frappe-ui";
import { computed, ref } from "vue";
import MainLayout from "../../../../../components/main-layout.vue";

const PAGE_SIZE = 20;
const placeholderImage = "https://placehold.co/80x80/e6e9f2/2d3e70?text=%20";

const searchQuery = ref("");
const page = ref(1);
const deleteTarget = ref(null);

let searchDebounce = null;

// GANTI url di bawah dengan API kamu sendiri, contoh whitelisted method di Frappe:
//
//   @frappe.whitelist()
//   def get_product_list(search="", page=1, page_length=20):
//       filters = [["product_name", "like", f"%{search}%"]] if search else []
//       data = frappe.get_list(
//           "Product",
//           fields=["name","product_name","sku","category","price","stock_qty","status","image"],
//           filters=filters,
//           order_by="modified desc",
//           limit_start=(int(page) - 1) * int(page_length),
//           limit_page_length=page_length,
//       )
//       total = frappe.db.count("Product", filters=filters)
//       return {"data": data, "total": total}
//
const productList = createResource({
	url: "bizpage.api.product_api.get_product_list",
	params: {
		search: searchQuery.value,
		page: page.value,
		page_length: PAGE_SIZE,
	},
	auto: true,
});

const products = computed(() => productList.data?.data || []);
const totalCount = computed(() => productList.data?.total || 0);
const totalPages = computed(() => Math.max(1, Math.ceil(totalCount.value / PAGE_SIZE)));
const rangeStart = computed(() => (totalCount.value === 0 ? 0 : (page.value - 1) * PAGE_SIZE + 1));
const rangeEnd = computed(() => Math.min(page.value * PAGE_SIZE, totalCount.value));

function fetchProducts() {
	productList.fetch({
		search: searchQuery.value,
		page: page.value,
		page_length: PAGE_SIZE,
	});
}

function handleSearchInput() {
	clearTimeout(searchDebounce);
	searchDebounce = setTimeout(() => {
		page.value = 1;
		fetchProducts();
	}, 400);
}

function nextPage() {
	if (page.value < totalPages.value) {
		page.value += 1;
		fetchProducts();
	}
}

function prevPage() {
	if (page.value > 1) {
		page.value -= 1;
		fetchProducts();
	}
}

function formatCurrency(value) {
	const number = Number(value) || 0;
	return new Intl.NumberFormat("id-ID", {
		style: "currency",
		currency: "IDR",
		maximumFractionDigits: 0,
	}).format(number);
}

function statusLabel(status) {
	const map = { Active: "Aktif", Inactive: "Nonaktif", "Out of Stock": "Stok Habis" };
	return map[status] || status || "—";
}

function statusBadgeClass(status) {
	const map = {
		Active: "bg-[var(--color-success)]/10 text-[var(--color-success-hover)]",
		Inactive: "bg-slate-100 text-slate-600",
		"Out of Stock": "bg-[var(--color-danger)]/10 text-[var(--color-danger-hover)]",
	};
	return map[status] || "bg-slate-100 text-slate-600";
}

function viewProduct(p) {
	// TODO: arahkan ke halaman detail, mis. router.push({ name: "produk.detail", params: { id: p.name } })
	console.log("Lihat produk", p.name);
}

function editProduct(p) {
	// TODO: arahkan ke form edit, mis. router.push({ name: "produk.edit", params: { id: p.name } })
	console.log("Edit produk", p.name);
}

function askDelete(p) {
	deleteTarget.value = p;
}

// GANTI url di bawah dengan API hapus produk kamu sendiri, contoh:
//
//   @frappe.whitelist()
//   def delete_product(name):
//       frappe.delete_doc("Product", name)
//
const deleteResource = createResource({
	url: "bizpage.api.product_api.delete_product",
	onSuccess() {
		deleteTarget.value = null;
		fetchProducts();
	},
});

function confirmDelete() {
	if (!deleteTarget.value) return;
	deleteResource.submit({ name: deleteTarget.value.name });
}
</script>
