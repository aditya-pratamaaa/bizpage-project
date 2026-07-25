<template>
	<div class="min-h-screen bg-slate-50 text-slate-900 flex flex-col md:flex-row">
		<!-- Mobile Header -->
		<header
			class="md:hidden flex items-center justify-between px-4 py-3 bg-white border-b border-slate-200 sticky top-0 z-40"
		>
			<div class="flex items-center gap-2.5">
				<span
					class="flex h-9 w-9 items-center justify-center rounded-xl bg-[var(--color-primary)] text-sm font-bold text-white shadow-md"
					>K</span
				>
				<span class="text-lg font-bold tracking-tight text-slate-900">Katalogin</span>
			</div>
			<button
				type="button"
				@click="isMobileMenuOpen = !isMobileMenuOpen"
				class="flex h-10 w-10 items-center justify-center rounded-lg text-slate-600 transition duration-300 hover:bg-slate-100 focus:outline-none"
				aria-label="Buka menu"
			>
				<i
					class="mdi text-2xl leading-none"
					:class="isMobileMenuOpen ? 'mdi-close' : 'mdi-menu'"
				></i>
			</button>
		</header>

		<!-- Overlay Mobile -->
		<div
			v-if="isMobileMenuOpen"
			@click="isMobileMenuOpen = false"
			class="fixed inset-0 bg-slate-900/40 z-40 md:hidden"
		></div>

		<!-- SIDEBAR -->
		<aside
			:class="[
				'fixed md:static inset-y-0 left-0 z-50 w-72 md:w-64 bg-white border-r border-slate-200 flex flex-col justify-between transition-transform duration-300 ease-in-out',
				isMobileMenuOpen ? 'translate-x-0' : '-translate-x-full md:translate-x-0',
			]"
		>
			<div class="flex flex-col min-h-0 flex-1">
				<!-- Logo Brand -->
				<div class="flex items-center gap-2.5 px-5 py-5 border-b border-slate-100">
					<span
						class="flex h-9 w-9 items-center justify-center rounded-xl bg-[var(--color-primary)] text-sm font-bold text-white shadow-md"
						>K</span
					>
					<span class="text-lg font-bold tracking-tight text-slate-900">Katalogin</span>
				</div>

				<!-- Main Navigation -->
				<nav class="flex-1 overflow-y-auto px-3 py-4 space-y-1">
					<div v-for="item in visibleMenu" :key="item.name">
						<!-- Item tanpa submenu -->
						<router-link
							v-if="!item.children"
							:to="safeRoute(item.route)"
							:class="[
								'flex items-center gap-3 rounded-xl px-3 py-2.5 text-sm font-medium transition duration-300',
								isActiveRoute(item.route)
									? 'bg-[var(--color-primary-light)] text-[var(--color-primary)] font-semibold'
									: 'text-slate-600 hover:bg-slate-100 hover:text-slate-900',
							]"
							@click="isMobileMenuOpen = false"
						>
							<i
								class="mdi text-lg leading-none shrink-0"
								:class="[
									`mdi-${item.icon}`,
									isActiveRoute(item.route)
										? 'text-[var(--color-primary)]'
										: 'text-slate-400',
								]"
							></i>
							<span>{{ item.name }}</span>
						</router-link>

						<!-- Item dengan submenu -->
						<div v-else>
							<button
								type="button"
								@click="toggleSubmenu(item.name)"
								:class="[
									'flex w-full items-center justify-between gap-3 rounded-xl px-3 py-2.5 text-sm font-medium transition duration-300',
									hasActiveChild(item)
										? 'text-[var(--color-primary)] bg-[var(--color-primary-light)]/60'
										: 'text-slate-600 hover:bg-slate-100 hover:text-slate-900',
								]"
							>
								<span class="flex items-center gap-3">
									<i
										class="mdi text-lg leading-none shrink-0"
										:class="[
											`mdi-${item.icon}`,
											hasActiveChild(item)
												? 'text-[var(--color-primary)]'
												: 'text-slate-400',
										]"
									></i>
									<span>{{ item.name }}</span>
								</span>
								<i
									class="mdi mdi-chevron-down text-base shrink-0 text-slate-400 transition-transform duration-300"
									:class="openSubmenu === item.name ? 'rotate-180' : ''"
								></i>
							</button>

							<Transition
								@before-enter="beforeExpand"
								@enter="expand"
								@after-enter="afterExpand"
								@before-leave="beforeCollapse"
								@leave="collapse"
							>
								<div
									v-show="openSubmenu === item.name"
									class="mt-1 ml-4 space-y-0.5 border-l border-slate-200 pl-4 overflow-hidden"
								>
									<router-link
										v-for="child in item.children"
										:key="child.name"
										:to="safeRoute(child.route)"
										:class="[
											'flex items-center gap-2.5 rounded-lg px-3 py-2 text-sm transition duration-300',
											isActiveRoute(child.route)
												? 'text-[var(--color-primary)] font-semibold'
												: 'text-slate-500 hover:text-slate-900 hover:bg-slate-100',
										]"
										@click="isMobileMenuOpen = false"
									>
										<i
											v-if="child.icon"
											class="mdi text-base leading-none shrink-0"
											:class="[
												`mdi-${child.icon}`,
												isActiveRoute(child.route)
													? 'text-[var(--color-primary)]'
													: 'text-slate-400',
											]"
										></i>
										<span>{{ child.name }}</span>
									</router-link>
								</div>
							</Transition>
						</div>
					</div>
				</nav>
			</div>

			<!-- Bottom: Role badge + Settings -->
			<div class="border-t border-slate-100 p-4 space-y-3">
				<div
					class="flex items-center gap-2 rounded-xl bg-[var(--color-accent-light)] px-3 py-2"
				>
					<span class="h-1.5 w-1.5 rounded-full bg-[var(--color-accent-active)]"></span>
					<span class="text-xs font-semibold text-slate-700 capitalize">{{ role }}</span>
				</div>
			</div>
		</aside>

		<!-- CONTENT AREA -->
		<div class="flex-1 flex flex-col min-w-0">
			<!-- Top Navbar -->
			<header
				class="h-16 border-b border-slate-200 bg-white/95 backdrop-blur-sm px-4 md:px-8 flex items-center justify-between sticky top-0 z-30"
			>
				<!-- Search -->
				<div class="flex-1 max-w-md relative">
					<!-- <span
						class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none text-slate-400"
					>
						<i class="mdi mdi-magnify text-base leading-none"></i>
					</span>
					<input
						type="text"
						placeholder="Cari..."
						class="w-full pl-9 pr-4 py-2 bg-slate-100 rounded-lg text-sm text-slate-700 placeholder-slate-400 border-none focus:outline-none focus:ring-2 focus:ring-[var(--color-focus-ring)]"
					/> -->
				</div>

				<!-- Right Menu -->
				<div class="flex items-center gap-4">
					<button
						type="button"
						class="relative flex h-9 w-9 items-center justify-center rounded-lg text-slate-500 transition duration-300 hover:bg-slate-100 hover:text-slate-900 focus:outline-none"
						aria-label="Notifikasi"
					>
						<i class="mdi mdi-bell-outline text-lg leading-none"></i>
						<span
							class="absolute top-1.5 right-1.5 h-2 w-2 rounded-full bg-[var(--color-accent-active)] ring-2 ring-white"
						></span>
					</button>

					<div class="h-5 w-px bg-slate-200"></div>

					<!-- Profile Dropdown -->
					<div class="relative">
						<button
							ref="profileButtonRef"
							type="button"
							@click="isProfileOpen = !isProfileOpen"
							class="flex items-center gap-2.5 focus:outline-none"
						>
							<img
								:src="user.avatar"
								alt="Avatar"
								class="h-8 w-8 rounded-full object-cover ring-2 ring-slate-100"
							/>
							<span class="hidden sm:flex flex-col items-start leading-tight">
								<span class="text-sm font-semibold text-slate-800">{{
									user.name
								}}</span>
								<span class="text-[11px] text-slate-400 capitalize">{{
									role
								}}</span>
							</span>
							<i
								class="mdi mdi-chevron-down text-base leading-none text-slate-400"
							></i>
						</button>

						<Transition
							enter-active-class="transition duration-150 ease-out"
							enter-from-class="opacity-0 scale-95 -translate-y-1"
							enter-to-class="opacity-100 scale-100 translate-y-0"
							leave-active-class="transition duration-100 ease-in"
							leave-from-class="opacity-100 scale-100 translate-y-0"
							leave-to-class="opacity-0 scale-95 -translate-y-1"
						>
							<div
								v-if="isProfileOpen"
								ref="profileMenuRef"
								class="absolute right-0 mt-2 w-48 bg-white rounded-xl border border-slate-200 shadow-xl py-1 z-50 origin-top-right"
							>
								<router-link
									:to="safeRoute('profile')"
									class="block px-4 py-2 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900"
									@click="isProfileOpen = false"
									>Profil Saya</router-link
								>
								<router-link
									:to="safeRoute('settings.index')"
									class="block px-4 py-2 text-sm text-slate-600 hover:bg-slate-50 hover:text-slate-900"
									@click="isProfileOpen = false"
									>Pengaturan</router-link
								>
								<div class="my-1 border-t border-slate-100"></div>
								<button
									type="button"
									class="block w-full text-left px-4 py-2 text-sm text-[var(--color-danger)] hover:bg-slate-50"
									@click="handleLogout"
								>
									Keluar
								</button>
							</div>
						</Transition>
					</div>
				</div>
			</header>

			<!-- DYNAMIC PAGE CONTENT -->
			<main class="flex-1 overflow-y-auto p-4 md:p-8">
				<slot />
			</main>
		</div>
	</div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from "vue";
import { session } from "../auth/session.js";
import { useRoute, useRouter } from "vue-router";
import { menuItems, filterMenuByRole } from "../helpers/menu.js";
import { createResource } from "frappe-ui";

import Swal from "sweetalert2";
// ---------------------------------------------------------------------
// Props: role user saat ini datang dari luar (mis. dari auth store)
// ---------------------------------------------------------------------
const props = defineProps({
	role: {
		type: String,
		default: "admin", // 'owner' | 'admin'
	},
	user: {
		type: Object,
		default: () => ({
			name: "Tom Cook",
			avatar: "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80",
		}),
	},
});

const role = computed(() => props.role);
const user = computed(() => props.user);

// ---------------------------------------------------------------------
// State
// ---------------------------------------------------------------------
const isMobileMenuOpen = ref(false);
const isProfileOpen = ref(false);
const openSubmenu = ref(null);
const profileButtonRef = ref(null);
const profileMenuRef = ref(null);

function handleClickOutside(event) {
	if (!isProfileOpen.value) return;
	const clickedButton = profileButtonRef.value?.contains(event.target);
	const clickedMenu = profileMenuRef.value?.contains(event.target);
	if (!clickedButton && !clickedMenu) {
		isProfileOpen.value = false;
	}
}

onMounted(() => document.addEventListener("click", handleClickOutside));
onUnmounted(() => document.removeEventListener("click", handleClickOutside));

const route = useRoute();
const router = useRouter();

// Cegah crash kalau nama route di menu.js belum terdaftar di router.
// Kalau tidak ketemu, link jadi non-aktif ('#') dan warning muncul di console
// supaya gampang ketahuan route mana yang belum dibuat.
function safeRoute(routeName) {
	if (!routeName) return "#";
	if (router.hasRoute(routeName)) return { name: routeName };
	console.warn(`[menu.js] Route "${routeName}" belum terdaftar di router.`);
	return "#";
}

// Menu difilter sesuai role, sumbernya dari menu.js
const visibleMenu = computed(() => filterMenuByRole(menuItems, role.value));

function toggleSubmenu(name) {
	openSubmenu.value = openSubmenu.value === name ? null : name;
}

function isActiveRoute(routeName) {
	if (!routeName) return false;

	// 1) Exact match — halaman ini persis route yang di-klik
	if (route.name === routeName) return true;

	// 2) Nested route — kalau di router.js halaman detail/edit didaftarkan
	//    sebagai children dari route ini, Vue Router otomatis memasukkan
	//    parent-nya ke route.matched.
	if (route.matched.some((r) => r.name === routeName)) return true;

	// 3) Override manual lewat meta — dipakai kalau mau eksplisit nunjuk
	//    halaman ini "milik" menu tertentu, terlepas dari struktur URL-nya.
	//      { path: '/produk/:id/edit', name: 'produk.edit',
	//        meta: { activeMenu: 'produk.index' } }
	if (route.meta?.activeMenu === routeName) return true;

	// 4) Path-prefix — paling praktis: asal URL diawali path menu ini,
	//    otomatis aktif seberapa pun dalamnya. Contoh: menu "Produk" (/produk)
	//    tetap aktif walau bukanya /produk/semua/kategori atau /produk/5/edit,
	//    tanpa perlu setting nested route atau meta satu-satu.
	const basePath = resolvePath(routeName);
	if (
		basePath &&
		basePath !== "/" &&
		(route.path === basePath || route.path.startsWith(basePath + "/"))
	) {
		return true;
	}

	return false;
}

// Ambil path asli dari nama route (buat pengecekan prefix di atas).
// Kalau nama route belum terdaftar, balikin null biar nggak error.
function resolvePath(routeName) {
	if (!router.hasRoute(routeName)) return null;
	return router.resolve({ name: routeName }).path;
}

const logout = createResource({
	url: "logout",
});

async function handleLogout() {
	isProfileOpen.value = false;

	const result = await Swal.fire({
		title: "Logout?",
		text: "Apakah Anda yakin ingin keluar dari aplikasi?",
		icon: "question",
		showCancelButton: true,
		confirmButtonText: "Ya, Logout",
		cancelButtonText: "Batal",
		confirmButtonColor: "#dc2626",
		cancelButtonColor: "#6b7280",
		reverseButtons: true,
	});

	if (!result.isConfirmed) return;

	try {
		await logout.submit();

		session.user = null;
		session.userRole.reset();

		localStorage.clear();

		await Swal.fire({
			title: "Berhasil!",
			text: "Anda telah logout.",
			icon: "success",
			timer: 1500,
			showConfirmButton: false,
		});

		await router.replace({ name: "Login" });
	} catch (error) {
		await Swal.fire({
			title: "Oops...",
			text: error?.message || "Logout gagal.",
			icon: "error",
		});
	}
}

function hasActiveChild(item) {
	return item.children?.some((child) => isActiveRoute(child.route)) ?? false;
}

// ---------------------------------------------------------------------
// Animasi expand/collapse submenu — dihitung dari scrollHeight elemen
// supaya transisinya smooth walau jumlah item submenu beda-beda tingginya
// ---------------------------------------------------------------------
function beforeExpand(el) {
	el.style.height = "0";
	el.style.opacity = "0";
}
function expand(el, done) {
	el.style.transition = "height 220ms ease, opacity 220ms ease";
	requestAnimationFrame(() => {
		el.style.height = el.scrollHeight + "px";
		el.style.opacity = "1";
	});
	el.addEventListener("transitionend", done, { once: true });
}
function afterExpand(el) {
	el.style.height = "auto";
	el.style.transition = "";
}
function beforeCollapse(el) {
	el.style.height = el.scrollHeight + "px";
	el.style.opacity = "1";
}
function collapse(el, done) {
	el.style.transition = "height 180ms ease, opacity 180ms ease";
	requestAnimationFrame(() => {
		el.style.height = "0";
		el.style.opacity = "0";
	});
	el.addEventListener("transitionend", done, { once: true });
}

// Buka otomatis submenu yang sedang aktif saat halaman dimuat
visibleMenu.value.forEach((item) => {
	if (item.children && hasActiveChild(item)) {
		openSubmenu.value = item.name;
	}
});
</script>
