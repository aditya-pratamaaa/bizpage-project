<template>
	<div v-if="store.loading" class="flex items-center justify-center h-screen text-gray-500">
		Memuat data toko...
	</div>
	<div
		v-else-if="store.data && (store.data.is_active === 1 || store.data.is_active === true)"
		class="m-6 sm:m-8 md:m-10"
	>
		<section class="w-full">
			<div
				class="relative w-full aspect-[16/6] sm:aspect-[16/5] md:aspect-[4/1] bg-gray-100 overflow-hidden rounded-[1rem]"
			>
				<img
					v-if="store.data?.banner"
					:src="`${apiUrl}${store.data.banner}`"
					alt="Banner"
					class="w-full h-full object-cover"
				/>
				<div
					v-else
					class="w-full h-full bg-gradient-to-br from-gray-200 to-gray-300"
				></div>
				<div
					class="absolute inset-0 bg-gradient-to-t from-black/25 via-transparent to-transparent"
				></div>
			</div>
			<div class="relative px-4 sm:px-8 max-w-5xl mx-auto pb-6 border-b border-gray-100">
				<div
					class="flex flex-col items-center text-center sm:flex-row sm:items-end sm:text-left sm:gap-5 -mt-12 sm:-mt-14"
				>
					<div class="relative shrink-0">
						<img
							v-if="store.data?.image"
							:src="`${apiUrl}${store.data.image}`"
							alt="Logo"
							class="h-24 w-24 sm:h-28 sm:w-28 md:h-32 md:w-32 rounded-full object-cover ring-4 ring-white shadow-md bg-white"
						/>
						<div
							v-else
							class="h-24 w-24 sm:h-28 sm:w-28 md:h-32 md:w-32 rounded-full ring-4 ring-white shadow-md bg-gray-200 flex items-center justify-center text-gray-400 text-xs"
						>
							No Logo
						</div>
					</div>
					<div class="mt-4 sm:mt-0 sm:pb-1 max-w-full sm:max-w-md md:max-w-xl">
						<div class="flex items-center gap-2 justify-center sm:justify-start">
							<h1
								class="text-2xl sm:text-2xl md:text-3xl font-bold tracking-tight text-gray-900"
							>
								{{ store.data?.business_name || "Memuat..." }}
							</h1>
							<svg
								v-if="store.data?.is_verified"
								xmlns="http://www.w3.org/2000/svg"
								viewBox="0 0 24 24"
								fill="currentColor"
								class="h-5 w-5 text-[var(--button-bg)] shrink-0"
							>
								<path
									fill-rule="evenodd"
									d="M8.603 3.799A4.49 4.49 0 0 1 12 2.25c1.357 0 2.573.6 3.397 1.549a4.49 4.49 0 0 1 3.498 1.307 4.49 4.49 0 0 1 1.307 3.497A4.49 4.49 0 0 1 21.75 12a4.49 4.49 0 0 1-1.549 3.397 4.49 4.49 0 0 1-1.307 3.497 4.49 4.49 0 0 1-3.497 1.307A4.49 4.49 0 0 1 12 21.75a4.49 4.49 0 0 1-3.397-1.549 4.49 4.49 0 0 1-3.498-1.306 4.491 4.491 0 0 1-1.307-3.498A4.49 4.49 0 0 1 2.25 12c0-1.357.6-2.573 1.549-3.397a4.49 4.49 0 0 1 1.307-3.497 4.49 4.49 0 0 1 3.497-1.307Zm7.007 6.387a.75.75 0 1 0-1.22-.872l-3.236 4.53L9.53 12.22a.75.75 0 0 0-1.06 1.06l2.25 2.25a.75.75 0 0 0 1.14-.094l3.75-5.25Z"
									clip-rule="evenodd"
								/>
							</svg>
						</div>
						<span
							v-if="store.data?.category"
							class="inline-block mt-1.5 text-xs font-medium text-[var(--button-bg)] bg-[var(--button-bg)]/10 px-2.5 py-0.5 rounded-full"
						>
							{{ store.data.category }}
						</span>

						<p
							class="mt-2 text-sm sm:text-[15px] text-gray-500 leading-relaxed line-clamp-2 sm:line-clamp-3"
						>
							{{ store.data?.description }}
						</p>
					</div>
				</div>
			</div>
		</section>

		<div v-if="store.loading" class="text-center py-4 text-gray-500">Memuat data toko...</div>
		<div v-else-if="!store.data" class="text-center py-4 text-gray-500">
			Toko tidak ditemukan.
		</div>

		<h1 class="mt-4 mb-8 text-2xl font-bold">Recomended For you!</h1>

		<div v-if="recommendedItem.loading" class="text-center py-4 text-gray-500">
			Memuat produk...
		</div>
		<div
			v-else-if="!recommendedItem.data || recommendedItem.data.length === 0"
			class="text-center py-4 text-gray-500"
		>
			Belum ada produk.
		</div>
		<div
			v-else
			class="flex flex-nowrap overflow-x-auto gap-4 pb-2 no-scrollbar snap-x snap-mandatory scroll-smooth"
		>
			<div
				v-for="i in recommendedItem.data"
				:key="i.name"
				@click="
					router.push({ name: 'ProductDetail', params: { store: slug, slug: i.slug } })
				"
				class="flex flex-col w-[calc(50%-0.5rem)] min-w-[140px] sm:w-[15.1rem] shrink-0 snap-start rounded-[0.5rem] overflow-hidden shadow-md bg-white"
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
					<div class="flex flex-col">
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
		<div
			@touchstart="handleTouchStart"
			@touchend="handleTouchEnd"
			class="relative w-full h-[20rem] bg-gray-100 mt-6 mb-6 rounded-[1rem] overflow-hidden group select-none"
		>
			<template v-if="store.data?.section_banner && store.data.section_banner.length > 0">
				<transition :name="slideDirection">
					<img
						:key="currentIndex"
						:src="`${apiUrl}${store.data.section_banner[currentIndex].image}`"
						alt="Section Banner"
						class="absolute inset-0 w-full h-full object-cover pointer-events-none"
					/>
				</transition>
			</template>

			<div
				v-else
				class="w-full h-full absolute inset-0 bg-gradient-to-br from-gray-200 to-gray-300"
			></div>

			<button
				v-if="store.data?.section_banner && store.data.section_banner.length > 1"
				@click="slideLeft"
				class="absolute z-10 left-4 top-1/2 -translate-y-1/2 w-10 h-10 bg-white/70 hover:bg-white text-gray-800 rounded-full flex items-center justify-center shadow-md opacity-0 group-hover:opacity-100 transition-all cursor-pointer hidden md:flex"
			>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					fill="none"
					viewBox="0 0 24 24"
					stroke-width="2"
					stroke="currentColor"
					class="w-5 h-5"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						d="M15.75 19.5L8.25 12l7.5-7.5"
					/>
				</svg>
			</button>

			<button
				v-if="store.data?.section_banner && store.data.section_banner.length > 1"
				@click="slideRight"
				class="absolute z-10 right-4 top-1/2 -translate-y-1/2 w-10 h-10 bg-white/70 hover:bg-white text-gray-800 rounded-full flex items-center justify-center shadow-md opacity-0 group-hover:opacity-100 transition-all cursor-pointer hidden md:flex"
			>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					fill="none"
					viewBox="0 0 24 24"
					stroke-width="2"
					stroke="currentColor"
					class="w-5 h-5"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						d="M8.25 4.5l7.5 7.5-7.5 7.5"
					/>
				</svg>
			</button>
		</div>

		<h1 class="mt-4 mb-8 text-2xl font-bold">Spesial Diskon</h1>

		<div v-if="item.loading" class="text-center py-4 text-gray-500">Memuat produk...</div>
		<div
			v-else-if="!item.data || item.data.length === 0"
			class="text-center py-4 text-gray-500"
		>
			Belum ada produk.
		</div>
		<div
			v-else
			class="flex flex-nowrap overflow-x-auto gap-4 pb-2 no-scrollbar snap-x snap-mandatory scroll-smooth"
		>
			<div
				v-for="i in item.data"
				:key="i.name"
				@click="
					router.push({ name: 'ProductDetail', params: { store: slug, slug: i.slug } })
				"
				class="flex flex-col w-[calc(50%-0.5rem)] min-w-[140px] sm:w-[15.1rem] shrink-0 snap-start rounded-[0.5rem] overflow-hidden shadow-md bg-white"
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
					<div class="flex flex-col">
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

		<div
			v-if="itemGroup.data?.length > 0"
			class="w-full flex overflow-x-auto gap-3 py-3 no-scrollbar"
		>
			<div
				@click="resetFilter"
				:class="[
					'flex items-center gap-2 px-4 py-2 border rounded-full whitespace-nowrap cursor-pointer transition-colors shrink-0',
					selectedGroup === null
						? 'bg-[var(--button-bg)] border-[var(--button-bg)] text-white'
						: 'bg-white border-gray-300 hover:border-gray-400 text-gray-800',
				]"
			>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					fill="none"
					viewBox="0 0 24 24"
					stroke-width="1.5"
					stroke="currentColor"
					class="w-5 h-5"
					:class="selectedGroup === null ? 'text-white' : 'text-gray-700'"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						d="M3.75 6A2.25 2.25 0 016 3.75h2.25A2.25 2.25 0 0110.5 6v2.25a2.25 2.25 0 01-2.25 2.25H6a2.25 2.25 0 01-2.25-2.25V6zM3.75 15.75A2.25 2.25 0 016 13.5h2.25a2.25 2.25 0 012.25 2.25V18a2.25 2.25 0 01-2.25 2.25H6A2.25 2.25 0 013.75 18v-2.25zM13.5 6a2.25 2.25 0 012.25-2.25H18A2.25 2.25 0 0120.25 6v2.25A2.25 2.25 0 0118 10.5h-2.25a2.25 2.25 0 01-2.25-2.25V6zM13.5 15.75a2.25 2.25 0 012.25-2.25H18a2.25 2.25 0 012.25 2.25V18A2.25 2.25 0 0118 20.25h-2.25A2.25 2.25 0 0113.5 18v-2.25z"
					/>
				</svg>
				<span class="text-sm">Kategori</span>
			</div>

			<div
				v-for="category in itemGroup.data"
				:key="category.name"
				@click="filterByGroup(category.name)"
				:class="[
					'flex items-center gap-2 px-4 py-2 border rounded-full whitespace-nowrap cursor-pointer transition-colors shrink-0',
					selectedGroup === category.name
						? 'bg-[var(--button-bg)] border-[var(--button-bg)] text-white'
						: 'bg-white border-gray-300 hover:border-gray-400 text-gray-800',
				]"
			>
				<img
					v-if="category.image"
					:src="`${apiUrl}${category.image}`"
					:alt="category.item_group_name"
					class="w-5 h-5 object-contain"
				/>
				<span class="text-sm">
					{{ category.item_group_name }}
				</span>
			</div>
		</div>

		<h1 class="mt-4 mb-8 text-2xl font-bold">Semua Produk</h1>

		<div v-if="allProducts.loading && !allProducts.data" class="flex flex-wrap gap-4">
			<div
				v-for="n in 4"
				:key="n"
				class="flex flex-col w-[calc(50%-0.5rem)] min-w-[140px] sm:w-[15.1rem] rounded-[0.5rem] overflow-hidden shadow-md bg-white animate-pulse"
			>
				<div class="w-full h-[14rem] bg-gray-200"></div>
				<div class="bg-gray-100 w-full h-[7rem]"></div>
			</div>
		</div>
		<div
			v-else-if="!allProducts.data || allProducts.data.length === 0"
			class="text-center py-4 text-gray-500"
		>
			Belum ada produk.
		</div>
		<div
			v-else
			class="flex flex-wrap gap-4 transition-opacity duration-300"
			:class="allProducts.loading ? 'opacity-40 pointer-events-none' : 'opacity-100'"
		>
			<div
				v-for="i in allProducts.data"
				:key="i.name"
				@click="
					router.push({ name: 'ProductDetail', params: { store: slug, slug: i.slug } })
				"
				class="flex flex-col w-[calc(50%-0.5rem)] min-w-[140px] sm:w-[15.1rem] rounded-[0.5rem] overflow-hidden shadow-md bg-white"
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
					<div class="flex flex-col">
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
import { ref } from "vue";

const route = useRoute();
const router = useRouter();
const slug = route.params.business;
const apiUrl = import.meta.env.VITE_API_URL;

const currentIndex = ref(0);
const slideDirection = ref("slide-right");
const selectedGroup = ref(null);

const slideLeft = () => {
	slideDirection.value = "slide-left";
	const totalBanners = store.data.section_banner.length;
	currentIndex.value = (currentIndex.value - 1 + totalBanners) % totalBanners;
};

const slideRight = () => {
	slideDirection.value = "slide-right";
	const totalBanners = store.data.section_banner.length;
	currentIndex.value = (currentIndex.value + 1) % totalBanners;
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
		if (diff > 0) {
			slideRight();
		} else {
			slideLeft();
		}
	}
};

const store = createResource({
	url: "bizpage.api.public_api.get_store_profile",
	params: {
		slug: slug,
	},
	auto: true,
	onSuccess(data) {
		if (data) {
			if (data.is_active === 0 || data.is_active === false) {
				router.push({ name: "Closed" });
			} else {
				document.title = `Bizpage | ${data.business_name}`;
			}
		} else {
			router.push({ name: "Not Found" });
		}
	},
	onError(error) {
		console.error("Gagal mengambil data toko:", error);
	},
});

const item = createResource({
	url: "bizpage.api.public_api.get_items",
	params: {
		slug: slug,
	},
	auto: true,
	onError(error) {
		console.error(error);
	},
});

const recommendedItem = createResource({
	url: "bizpage.api.public_api.get_items",
	params: {
		slug: slug,
		recomended: 1,
	},
	auto: true,
	onError(error) {
		console.error(error);
	},
});

const itemGroup = createResource({
	url: "bizpage.api.public_api.get_item_groups_by_store",
	params: {
		slug: slug,
	},
	auto: true,
	onError(error) {
		console.error(error);
	},
});

const allProducts = createResource({
	url: "bizpage.api.public_api.get_items",
	params: {
		slug: slug,
	},
	auto: true,
	onError(error) {
		console.error(error);
	},
});

const filterByGroup = (groupName) => {
	if (selectedGroup.value === groupName) return;
	selectedGroup.value = groupName;
	allProducts.update({
		params: {
			slug: slug,
			item_group: groupName,
		},
	});
	allProducts.reload();
};

const resetFilter = () => {
	if (selectedGroup.value === null) return;
	selectedGroup.value = null;
	allProducts.update({
		params: {
			slug: slug,
		},
	});
	allProducts.reload();
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
