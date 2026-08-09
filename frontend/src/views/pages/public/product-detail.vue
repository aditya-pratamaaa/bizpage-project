<template>
	<div v-if="product.loading" class="flex items-center justify-center h-screen text-gray-500">
		Memuat produk...
	</div>
	<div
		v-else-if="!product.data"
		class="flex flex-col items-center justify-center h-screen gap-4"
	>
		<p class="text-gray-500">Produk tidak ditemukan.</p>
		<button @click="router.back()" class="text-[var(--button-bg)] font-medium">
			← Kembali
		</button>
	</div>
	<div v-else class="m-6 sm:m-8 md:m-10">
		<button
			@click="router.back()"
			class="flex items-center gap-1 text-sm text-gray-500 hover:text-gray-800 mb-6 cursor-pointer"
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

		<div class="flex flex-col md:flex-row gap-8">
			<!-- Image Slider -->
			<div class="w-full md:w-1/2">
				<div
					@touchstart="handleTouchStart"
					@touchend="handleTouchEnd"
					class="relative w-full aspect-square bg-gray-100 rounded-[1rem] overflow-hidden group select-none"
				>
					<template v-if="images.length > 0">
						<transition :name="slideDirection">
							<img
								:key="currentIndex"
								:src="`${apiUrl}${images[currentIndex]}`"
								:alt="product.data.item_name"
								class="absolute inset-0 w-full h-full object-cover pointer-events-none"
							/>
						</transition>
					</template>
					<div
						v-else
						class="w-full h-full flex items-center justify-center text-gray-400 text-sm"
					>
						No Image
					</div>

					<button
						v-if="images.length > 1"
						@click="slideLeft"
						class="absolute z-10 left-3 top-1/2 -translate-y-1/2 w-9 h-9 bg-white/70 hover:bg-white text-gray-800 rounded-full flex items-center justify-center shadow-md opacity-0 group-hover:opacity-100 transition-all cursor-pointer hidden md:flex"
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
						class="absolute z-10 right-3 top-1/2 -translate-y-1/2 w-9 h-9 bg-white/70 hover:bg-white text-gray-800 rounded-full flex items-center justify-center shadow-md opacity-0 group-hover:opacity-100 transition-all cursor-pointer hidden md:flex"
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

				<!-- Dots indicator -->
				<div v-if="images.length > 1" class="flex justify-center gap-1.5 mt-3">
					<button
						v-for="(img, idx) in images"
						:key="idx"
						@click="goToSlide(idx)"
						:class="[
							'h-1.5 rounded-full transition-all cursor-pointer',
							idx === currentIndex
								? 'w-5 bg-[var(--button-bg)]'
								: 'w-1.5 bg-gray-300',
						]"
					/>
				</div>
			</div>

			<!-- Info -->
			<div class="w-full md:w-1/2 flex flex-col">
				<span
					v-if="product.data.item_group_name"
					class="inline-block w-fit text-xs font-medium text-[var(--button-bg)] bg-[var(--button-bg)]/10 px-2.5 py-0.5 rounded-full mb-2"
				>
					{{ product.data.item_group_name }}
				</span>

				<h1 class="text-2xl sm:text-3xl font-bold text-gray-900">
					{{ product.data.item_name }}
				</h1>

				<h2 class="mt-2 text-xl sm:text-2xl font-bold text-[var(--button-bg)]">
					Rp {{ product.data.price ? product.data.price.toLocaleString("id-ID") : "-" }}
				</h2>

				<p
					class="mt-4 text-sm sm:text-[15px] text-gray-600 leading-relaxed whitespace-pre-line"
				>
					{{ product.data.description || "Tidak ada deskripsi." }}
				</p>

				<!-- Pilih Varian -->
				<div v-if="Object.keys(attributes).length > 0" class="mt-6 flex flex-col gap-4">
					<div v-for="(values, attrName) in attributes" :key="attrName">
						<p class="text-sm font-semibold text-gray-800 mb-2">{{ attrName }}</p>
						<div class="flex flex-wrap gap-2">
							<button
								v-for="val in values"
								:key="val"
								@click="selectVariant(attrName, val)"
								:class="[
									'px-4 py-2 text-sm rounded-[0.5rem] border cursor-pointer transition-colors',
									selectedVariants[attrName] === val
										? 'bg-[var(--button-bg)] border-[var(--button-bg)] text-white'
										: 'bg-white border-gray-300 text-gray-700 hover:border-gray-400',
								]"
							>
								{{ val }}
							</button>
						</div>
					</div>
				</div>

				<!-- Isi Paket -->
				<div
					v-if="product.data.components && product.data.components.length > 0"
					class="mt-6"
				>
					<p class="text-sm font-semibold text-gray-800 mb-2">Isi Paket</p>
					<ul class="list-disc list-inside text-sm text-gray-600 space-y-1">
						<li v-for="(c, idx) in product.data.components" :key="idx">
							{{ c.component_name || c.component }}
							<span v-if="c.qty"> x{{ c.qty }}</span>
						</li>
					</ul>
				</div>

				<!-- Business info -->
				<div
					v-if="product.data.business"
					@click="goToStore(product.data.business.slug)"
					class="mt-6 flex items-center gap-3 p-3 border border-gray-200 rounded-[0.75rem] cursor-pointer hover:border-gray-300 transition-colors w-fit"
				>
					<img
						v-if="product.data.business.image"
						:src="`${apiUrl}${product.data.business.image}`"
						alt="Logo"
						class="h-10 w-10 rounded-full object-cover bg-gray-100"
					/>
					<div>
						<p class="text-xs text-gray-400">Dijual oleh</p>
						<p class="text-sm font-semibold text-gray-800">
							{{ product.data.business.business_name }}
						</p>
					</div>
				</div>

				<button
					@click="handleCheckout"
					class="mt-8 w-full sm:w-fit px-6 py-3 rounded-[0.75rem] bg-green-600 text-white font-medium hover:bg-green-700 transition-colors cursor-pointer flex items-center justify-center gap-2"
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

		<!-- Related products -->
		<div v-if="related.data && related.data.length > 0" class="mt-12">
			<h1 class="mb-6 text-xl font-bold">Produk Lainnya</h1>
			<div
				class="flex flex-nowrap overflow-x-auto gap-4 pb-2 no-scrollbar snap-x snap-mandatory"
			>
				<div
					v-for="i in related.data.filter((p) => p.name !== product.data.name)"
					:key="i.name"
					@click="goToProduct(i.slug)"
					class="flex flex-col w-[calc(50%-0.5rem)] min-w-[140px] sm:w-[15.1rem] shrink-0 snap-start rounded-[0.5rem] overflow-hidden shadow-md bg-white cursor-pointer"
				>
					<div class="w-full h-[14rem] bg-gray-100 flex items-center justify-center">
						<img
							v-if="i.image"
							:src="`${apiUrl}${i.image}`"
							:alt="i.item_name"
							class="w-full h-full object-cover"
						/>
						<div v-else class="text-gray-400 text-sm">No Image</div>
					</div>
					<div
						class="bg-indigo-500 w-full h-[7rem] flex flex-col justify-between p-[0.6rem]"
					>
						<h1 class="text-base font-bold text-white leading-tight line-clamp-1">
							{{ i.item_name }}
						</h1>
						<h2 class="text-lg font-bold text-white/90">
							Rp. {{ i.price ? i.price.toLocaleString("id-ID") : "-" }}
						</h2>
					</div>
				</div>
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

// ---------- Product data ----------
const product = createResource({
	url: "bizpage.api.public_api.get_item_detail",
	params: { slug: route.params.slug },
	auto: true,
	onSuccess(data) {
		if (data) {
			document.title = `Bizpage | ${data.item_name}`;
			currentIndex.value = 0;
			selectedVariants.value = {};
			related.update({
				params: {
					slug: route.params.store,
					item_group: data.item_group,
				},
			});
			related.reload();
		} else {
			router.push({ name: "Not Found" });
		}
	},
});

const related = createResource({
	url: "bizpage.api.public_api.get_items",
	params: { slug: route.params.store },
	auto: false,
});

const images = computed(() => product.data?.images || []);
const attributes = computed(() => product.data?.attributes || {});

// ---------- Image slider ----------
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

// ---------- Variant selection ----------
const selectedVariants = ref({});

const selectVariant = (attrName, value) => {
	selectedVariants.value[attrName] = value;
};

// ---------- Navigation ----------
const goToProduct = (slug) => {
	router.push({ name: "ProductDetail", params: { store: route.params.store, slug } });
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

// ---------- Checkout via WhatsApp ----------
const handleCheckout = () => {
	const attrNames = Object.keys(attributes.value);
	const missing = attrNames.some((name) => !selectedVariants.value[name]);

	if (attrNames.length > 0 && missing) {
		alert("Mohon pilih varian produk terlebih dahulu.");
		return;
	}

	const variantText = attrNames
		.map((name) => `${name}: ${selectedVariants.value[name]}`)
		.join(", ");

	const itemName = product.data.item_name;
	const price = product.data.price ? `Rp ${product.data.price.toLocaleString("id-ID")}` : "-";

	const message = variantText
		? `Halo, saya tertarik memesan ${itemName} (Varian: ${variantText}) dengan harga ${price}. Apakah stoknya masih tersedia?`
		: `Halo, saya tertarik memesan ${itemName} dengan harga ${price}. Apakah stoknya masih tersedia?`;

	const rawPhone = product.data.business?.phone_number || "";
	let phone = rawPhone.replace(/\D/g, "");

	if (phone.startsWith("0")) {
		phone = "62" + phone.slice(1);
	}

	if (!phone) {
		alert("Nomor WhatsApp toko tidak tersedia.");
		return;
	}

	const waUrl = `https://wa.me/${phone}?text=${encodeURIComponent(message)}`;
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
