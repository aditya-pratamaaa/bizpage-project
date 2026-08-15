<template>
	<div
		v-if="product.loading"
		class="flex items-center justify-center h-screen bizpage-text-muted"
	>
		Memuat produk...
	</div>
	<div
		v-else-if="!product.data"
		class="flex flex-col items-center justify-center h-screen gap-4"
	>
		<p class="bizpage-text-muted">Produk tidak ditemukan.</p>
		<button @click="router.back()" class="font-medium cursor-pointer bizpage-text-accent">
			← Kembali
		</button>
	</div>
	<div v-else class="m-6 sm:m-8 md:m-10">
		<button
			@click="router.back()"
			class="flex items-center gap-1 text-sm mb-6 cursor-pointer transition-colors bizpage-back-link"
		>
			<svg
				xmlns="http://www.w3.org/2000/svg"
				fill="none"
				viewBox="0 0 24 24"
				stroke-width="2"
				stroke="currentColor"
				class="w-4 h-4"
			>
				<path
					stroke-linecap="round"
					stroke-linejoin="round"
					d="M15.75 19.5L8.25 12l7.5-7.5"
				/>
			</svg>
			Kembali
		</button>

		<div class="flex flex-col md:flex-row md:items-stretch gap-8">
			<div class="w-full md:w-[620px] md:sticky md:top-6 md:self-start">
				<div
					@touchstart="handleTouchStart"
					@touchend="handleTouchEnd"
					class="relative w-full aspect-square rounded-[1rem] overflow-hidden group select-none bizpage-gallery-media"
				>
					<template v-if="images.length > 0">
						<transition :name="slideDirection">
							<img
								:key="currentIndex"
								:src="`${apiUrl}${images[currentIndex].image}`"
								:alt="images[currentIndex].title || product.data.item_name"
								class="absolute inset-0 w-full h-full object-cover pointer-events-none"
							/>
						</transition>
					</template>
					<div v-else class="w-full h-full flex items-center justify-center text-sm">
						No Image
					</div>

					<div
						v-if="images.length > 1"
						class="absolute top-3 right-3 z-10 px-2 py-0.5 rounded-full text-xs font-medium bizpage-image-counter"
					>
						{{ currentIndex + 1 }}/{{ images.length }}
					</div>

					<button
						v-if="images.length > 1"
						@click="slideLeft"
						class="absolute z-10 left-3 top-1/2 -translate-y-1/2 w-9 h-9 rounded-full flex items-center justify-center opacity-0 group-hover:opacity-100 transition-all cursor-pointer hidden md:flex bizpage-slider-btn"
					>
						<svg
							xmlns="http://www.w3.org/2000/svg"
							fill="none"
							viewBox="0 0 24 24"
							stroke-width="2"
							stroke="currentColor"
							class="w-4 h-4"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								d="M15.75 19.5L8.25 12l7.5-7.5"
							/>
						</svg>
					</button>

					<button
						v-if="images.length > 1"
						@click="slideRight"
						class="absolute z-10 right-3 top-1/2 -translate-y-1/2 w-9 h-9 rounded-full flex items-center justify-center opacity-0 group-hover:opacity-100 transition-all cursor-pointer hidden md:flex bizpage-slider-btn"
					>
						<svg
							xmlns="http://www.w3.org/2000/svg"
							fill="none"
							viewBox="0 0 24 24"
							stroke-width="2"
							stroke="currentColor"
							class="w-4 h-4"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								d="M8.25 4.5l7.5 7.5-7.5 7.5"
							/>
						</svg>
					</button>
				</div>
				<div v-if="images.length > 1" class="mt-3 flex gap-2 overflow-x-auto no-scrollbar">
					<button
						v-for="(img, idx) in images"
						:key="idx"
						@click="goToSlide(idx)"
						:class="[
							'shrink-0 w-12 h-12 sm:w-14 sm:h-14 rounded-[0.5rem] overflow-hidden border-2 transition-colors cursor-pointer bizpage-gallery-thumb',
							idx === currentIndex ? 'is-active' : '',
						]"
					>
						<img
							:src="`${apiUrl}${img.image}`"
							:alt="img.title || product.data.item_name"
							class="w-full h-full object-cover"
						/>
					</button>
				</div>

				<p
					v-if="images.length > 0 && images[currentIndex].title"
					class="mt-2 text-sm text-center bizpage-text-muted"
				>
					{{ images[currentIndex].title }}
				</p>
			</div>
			<div class="w-full md:flex-1 min-w-0 flex flex-col">
				<span
					v-if="product.data.item_group_name"
					class="inline-block w-fit text-sm font-medium px-2.5 py-0.5 rounded-full mb-2 bizpage-badge-accent"
				>
					{{ product.data.item_group_name }}
				</span>

				<h1 class="text-2xl sm:text-3xl font-bold bizpage-text-heading">
					{{ product.data.item_name }}
				</h1>

				<h2 class="mt-2 text-xl sm:text-2xl font-bold bizpage-price">
					Rp {{ activePrice ? activePrice.toLocaleString("id-ID") : "-" }}
				</h2>

				<div class="flex items-center gap-2 mt-3 mb-1">
					<div
						v-if="product.data.cod"
						class="flex items-center gap-1.5 px-2.5 py-1 rounded-[0.25rem] bg-orange-100 text-orange-600 border border-orange-200"
					>
						<img src="../../../assets/icon/cod.svg" alt="COD" class="w-4 h-4" />
						<span class="text-xs font-bold uppercase tracking-wide">Bisa COD</span>
					</div>

					<div
						v-if="product.data.delivery"
						class="flex items-center gap-1.5 px-2.5 py-1 rounded-[0.25rem] bg-blue-100 text-blue-600 border border-blue-200"
					>
						<img
							src="../../../assets/icon/delivery.svg"
							alt="Delivery"
							class="w-4 h-4"
						/>
						<span class="text-xs font-bold uppercase tracking-wide">Delivery</span>
					</div>
				</div>

				<p
					class="mt-4 text-sm sm:text-[15px] leading-relaxed whitespace-pre-line bizpage-text-muted"
				>
					{{ product.data.description || "Tidak ada deskripsi." }}
				</p>

				<div
					v-if="product.data.components && product.data.components.length > 0"
					class="mt-6 pt-6 border-t border-[var(--border-subtle)]"
				>
					<p class="text-base font-semibold mb-2 bizpage-text-heading">Isi Paket</p>
					<ul class="list-disc list-inside text-sm space-y-1 bizpage-text-muted">
						<li v-for="(c, idx) in product.data.components" :key="idx">
							{{ c.component_name || c.component }}
							<span v-if="c.qty"> x{{ c.qty }}</span>
						</li>
					</ul>
				</div>

				<div
					v-if="Object.keys(groupedVariants).length > 0"
					class="mt-6 pt-6 border-t border-[var(--border-subtle)] flex flex-col gap-4"
				>
					<div v-for="(variants, attrName) in groupedVariants" :key="attrName">
						<p class="text-base font-semibold mb-2 bizpage-text-heading">
							{{ attrName }}
						</p>
						<div class="flex flex-wrap gap-2">
							<button
								v-for="(v, idx) in variants"
								:key="idx"
								@click="selectedVariant = v"
								:class="[
									'px-4 py-2 text-sm rounded-[0.25rem] border transition-colors cursor-pointer bizpage-variant-chip',
									selectedVariant === v ? 'is-active font-semibold' : '',
								]"
							>
								{{ v.value_label }}
							</button>
						</div>
					</div>
				</div>

				<div
					v-if="product.data.business"
					@click="goToStore(product.data.business.slug)"
					class="mt-6 flex items-center gap-3 p-3 border rounded-[0.75rem] cursor-pointer transition-colors w-fit bizpage-info-card"
				>
					<img
						v-if="product.data.business.image"
						:src="`${apiUrl}${product.data.business.image}`"
						alt="Logo"
						class="h-10 w-10 rounded-full object-cover bg-[var(--bg-subtle)]"
					/>
					<div>
						<p class="text-sm bizpage-text-muted">Dijual oleh</p>
						<p class="text-base font-semibold bizpage-text-heading">
							{{ product.data.business.business_name }}
						</p>
					</div>
				</div>

				<div class="mt-8 pt-6 border-t border-[var(--border-subtle)] w-full sm:w-fit">
					<button
						@click="handleCheckout"
						class="w-full px-6 py-3 rounded-[0.25rem] font-medium transition-colors cursor-pointer flex items-center justify-center gap-2 shadow-sm bizpage-btn-whatsapp"
					>
						<svg
							xmlns="http://www.w3.org/2000/svg"
							viewBox="0 0 24 24"
							fill="currentColor"
							class="w-5 h-5"
						>
							<path
								d="M12 2C6.48 2 2 6.48 2 12c0 1.85.5 3.58 1.37 5.07L2 22l5.07-1.33A9.94 9.94 0 0012 22c5.52 0 10-4.48 10-10S17.52 2 12 2zm5.2 14.2c-.22.62-1.28 1.18-1.76 1.24-.45.06-1.02.08-1.65-.1-.38-.11-.87-.28-1.5-.55-2.64-1.14-4.36-3.8-4.5-3.98-.13-.18-1.08-1.44-1.08-2.74 0-1.3.68-1.94.92-2.2.24-.26.53-.32.7-.32.18 0 .35 0 .5.01.16.01.38-.06.6.46.22.53.75 1.83.82 1.96.07.13.11.29.02.47-.09.18-.13.29-.26.44-.13.15-.27.34-.39.46-.13.13-.26.27-.11.53.15.26.65 1.08 1.4 1.75.97.86 1.78 1.13 2.05 1.26.26.13.42.11.57-.07.15-.18.65-.76.82-1.02.17-.26.35-.22.58-.13.24.09 1.5.71 1.76.84.26.13.43.19.5.3.07.11.07.62-.15 1.24z"
							/>
						</svg>
						Pesan via WhatsApp
					</button>
				</div>
			</div>

			<div
				class="w-full md:w-80 shrink-0 flex flex-col border rounded-[0.75rem] bizpage-info-card overflow-hidden"
			>
				<div class="p-4">
					<p class="text-sm font-semibold bizpage-text-heading">Request Khusus</p>
					<p class="mt-1 text-xs leading-relaxed bizpage-text-muted">
						Ingin request khusus untuk pesanan Anda?
					</p>
				</div>

				<div
					class="px-4 py-3 border-t border-[var(--border-subtle)] flex items-center gap-3"
				>
					<img
						v-if="images.length > 0"
						:src="`${apiUrl}${images[0].image}`"
						:alt="product.data.item_name"
						class="h-10 w-10 rounded-[0.375rem] object-cover shrink-0 bg-[var(--bg-subtle)]"
					/>
					<p class="text-sm font-medium bizpage-text-heading truncate">
						{{ product.data.item_name }}
					</p>
				</div>

				<div
					class="flex-1 flex flex-col px-4 pb-4 pt-3 border-t border-[var(--border-subtle)]"
				>
					<label for="custom_name" class="text-xs font-medium bizpage-text-muted"
						>Nama</label
					>
					<input
						type="text"
						id="custom_name"
						v-model="customBuyerName"
						placeholder="Nama Anda"
						class="w-full mt-1 px-3 py-1.5 text-sm border rounded-[0.25rem] bizpage-input"
					/>

					<label
						for="custom_note"
						class="mt-3 block text-xs font-medium bizpage-text-muted"
						>Catatan</label
					>
					<textarea
						id="custom_note"
						v-model="customNote"
						placeholder="Contoh: mau warna kuning, request pita pink, dll"
						class="w-full mt-1 flex-1 px-3 py-1.5 text-sm border rounded-[0.25rem] bizpage-input bizpage-textarea resize-none"
					></textarea>

					<button
						@click="sendCustomWhatsApp"
						class="w-full mt-3 px-6 py-2.5 rounded-[0.25rem] text-sm font-medium transition-colors cursor-pointer flex items-center justify-center gap-2 bizpage-btn-whatsapp"
					>
						Kirim Request Custom
					</button>
				</div>
			</div>
		</div>
	</div>
	<div
		v-if="isCheckoutFormVisible"
		class="fixed inset-0 z-50 flex items-center justify-center p-4 backdrop-blur-sm transition-opacity bg-[var(--overlay-bg)]"
	>
		<div class="w-full max-w-sm rounded-[1rem] p-6 shadow-xl bg-[var(--bg-page)]">
			<h3 class="text-xl font-bold mb-1 bizpage-text-heading">Data Pesanan</h3>
			<p class="text-sm mb-5 bizpage-text-muted">Silakan isi nama Anda untuk melanjutkan.</p>

			<label for="customer_name" class="text-base font-semibold bizpage-text-heading"
				>Nama Lengkap</label
			>
			<input
				type="text"
				id="customer_name"
				v-model="customerName"
				placeholder="Masukkan nama Anda..."
				class="w-full mt-1 px-4 py-2 text-sm border rounded-[0.25rem] mb-6 bizpage-input"
			/>

			<div class="flex gap-3">
				<button
					@click="isCheckoutFormVisible = false"
					class="flex-1 px-4 py-2.5 rounded-[0.25rem] border text-sm font-medium transition-colors cursor-pointer bizpage-btn-cancel"
				>
					Batal
				</button>
				<button
					@click="sendWhatsApp"
					class="flex-1 px-4 py-2.5 rounded-[0.25rem] text-sm font-medium transition-colors cursor-pointer bizpage-btn-whatsapp"
				>
					Kirim Pesan
				</button>
			</div>
		</div>
	</div>
</template>

<script setup>
import { useRoute, useRouter } from "vue-router";
import { createResource } from "frappe-ui";
import { ref, computed, watch } from "vue";

const route = useRoute();
const router = useRouter();
const apiUrl = import.meta.env.VITE_API_URL;
const selectedVariant = ref(null);
const customerName = ref("");
const isCheckoutFormVisible = ref(false);
const customBuyerName = ref("");
const customNote = ref("");

const product = createResource({
	url: "bizpage.api.public_api.get_item_detail",
	params: { slug: route.params.slug },
	auto: true,
	onSuccess(data) {
		if (data) {
			document.title = `Bizpage | ${data.item_name}`;
			currentIndex.value = 0;
			selectedVariant.value = null;
			isCheckoutFormVisible.value = false;

			const correctCategory = data.item_group_slug || "produk";
			if (route.params.category !== correctCategory) {
				router.replace({
					name: "ProductDetail",
					params: {
						store: route.params.store,
						category: correctCategory,
						slug: route.params.slug,
					},
				});
			}
		} else {
			router.push({ name: "Not Found" });
		}
	},
});
const images = computed(() => product.data?.images || []);

const groupedVariants = computed(() => {
	const groups = {};
	if (product.data?.variants) {
		product.data.variants.forEach((v) => {
			const attr = v.attribute_label || v.attribute;
			if (!groups[attr]) groups[attr] = [];
			groups[attr].push(v);
		});
	}
	return groups;
});

const activePrice = computed(() => {
	const basePrice = Number(product.data?.price || 0);

	if (selectedVariant.value && selectedVariant.value.price_adjustment) {
		return basePrice + Number(selectedVariant.value.price_adjustment);
	}

	return basePrice;
});

const currentIndex = ref(0);
const slideDirection = ref("slide-right");

const slideLeft = () => {
	slideDirection.value = "slide-left";
	const total = images.value.length;
	currentIndex.value = (currentIndex.value - 1 + total) % total;
};

const slideRight = () => {
	slideDirection.value = "slide-right";
	const total = images.value.length;
	currentIndex.value = (currentIndex.value + 1) % total;
};

const goToSlide = (idx) => {
	slideDirection.value = idx > currentIndex.value ? "slide-right" : "slide-left";
	currentIndex.value = idx;
};

const touchStartX = ref(0);
const touchEndX = ref(0);

const handleTouchStart = (e) => {
	touchStartX.value = e.changedTouches[0].clientX;
};

const handleTouchEnd = (e) => {
	touchEndX.value = e.changedTouches[0].clientX;
	handleSwipe();
};

const handleSwipe = () => {
	const swipeThreshold = 50;
	const diff = touchStartX.value - touchEndX.value;
	if (Math.abs(diff) > swipeThreshold) {
		diff > 0 ? slideRight() : slideLeft();
	}
};

const goToStore = (storeSlug) => {
	router.push({ name: "Store", params: { store: storeSlug } });
};

watch(
	() => route.params.slug,
	(newSlug) => {
		product.update({ params: { slug: newSlug } });
		product.reload();
	},
);

const handleCheckout = () => {
	if (product.data.variants?.length && !selectedVariant.value) {
		alert("Silakan pilih varian produk terlebih dahulu.");
		return;
	}
	isCheckoutFormVisible.value = true;
};

const createOrderResource = createResource({
	url: "bizpage.api.public_api.create_sales_order",
});

const getStorePhoneNumber = () => {
	const rawPhone = product.data.business?.phone_number || "";
	let phone = rawPhone.replace(/\D/g, "");

	if (phone.startsWith("0")) {
		phone = "62" + phone.slice(1);
	}

	return phone;
};

const createSalesOrderRecord = (customer, note) => {
	if (!product.data?.name || !product.data?.business?.name) return;

	createOrderResource.submit(
		{
			item: product.data.name,
			business: product.data.business.name,
			customer,
			custom_note: note || "",
		},
		{
			onError(err) {
				console.error("Gagal membuat Sales Order:", err);
			},
		},
	);
};

const sendWhatsApp = () => {
	if (!customerName.value.trim()) {
		alert("Mohon masukkan nama Anda.");
		return;
	}

	const itemName = product.data.item_name;
	const variantText = selectedVariant.value
		? ` (Varian: ${selectedVariant.value.attribute_label} - ${selectedVariant.value.value_label})`
		: "";
	const priceText = `Rp ${activePrice.value.toLocaleString("id-ID")}`;

	const message = `Halo, saya ${customerName.value}.\n\nSaya tertarik memesan ${itemName}${variantText} dengan total harga ${priceText}. Apakah stoknya masih tersedia?`;

	const phone = getStorePhoneNumber();

	if (!phone) {
		alert("Nomor WhatsApp toko tidak tersedia.");
		return;
	}

	const waUrl = `https://wa.me/${phone}?text=${encodeURIComponent(message)}`;

	createSalesOrderRecord(customerName.value.trim(), "");
	window.open(waUrl, "_blank");
};

const sendCustomWhatsApp = () => {
	if (!customBuyerName.value.trim()) {
		alert("Mohon masukkan nama Anda.");
		return;
	}

	if (!customNote.value.trim()) {
		alert("Mohon isi request custom Anda dulu.");
		return;
	}

	const itemName = product.data.item_name;

	const message = `Halo, saya ${customBuyerName.value.trim()}. Saya tertarik dengan produk ${itemName}. Saya ada request khusus: ${customNote.value.trim()}. Apakah bisa?`;

	const phone = getStorePhoneNumber();

	if (!phone) {
		alert("Nomor WhatsApp toko tidak tersedia.");
		return;
	}

	const waUrl = `https://wa.me/${phone}?text=${encodeURIComponent(message)}`;

	createSalesOrderRecord(customBuyerName.value.trim(), customNote.value.trim());
	window.open(waUrl, "_blank");
};
</script>

<style scoped>
.no-scrollbar::-webkit-scrollbar {
	display: none;
}
.no-scrollbar {
	-ms-overflow-style: none;
	scrollbar-width: none;
}
.slide-right-enter-active,
.slide-right-leave-active {
	transition: transform 0.5s ease-in-out;
}
.slide-right-enter-from {
	transform: translateX(100%);
}
.slide-right-leave-to {
	transform: translateX(-100%);
}
.slide-left-enter-active,
.slide-left-leave-active {
	transition: transform 0.5s ease-in-out;
}
.slide-left-enter-from {
	transform: translateX(-100%);
}
.slide-left-leave-to {
	transform: translateX(100%);
}
</style>
