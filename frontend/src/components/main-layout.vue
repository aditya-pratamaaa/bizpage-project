<template>
	<div
		class="h-screen overflow-hidden bg-[var(--bg-page)] text-[var(--text)] flex flex-col md:flex-row"
	>
		<!-- Mobile Header -->
		<header
			class="md:hidden flex items-center justify-between px-4 py-3 bg-[var(--bg-subtle)] border-b border-[var(--border)] sticky top-0 z-40"
		>
			<div class="flex items-center gap-2.5">
				<span
					class="flex h-9 w-9 items-center justify-center rounded-xl bg-gradient-to-br from-[var(--button-bg)] to-[var(--button-bg-hover)] text-sm font-bold text-[var(--button-text)] shadow-md"
					>K</span
				>
				<span class="text-lg font-bold tracking-tight text-[var(--text)]">Katalogin</span>
			</div>

			<div class="flex items-center gap-1.5">
				<!-- Toggle Dark Mode (mobile) -->
				<button
					type="button"
					@click="toggleTheme"
					class="flex h-9 w-9 items-center justify-center rounded-lg text-[var(--text-muted)] transition duration-300 hover:bg-[var(--surface-hover)] hover:text-[var(--text)] focus:outline-none"
					:aria-label="
						theme.mode === 'dark' ? 'Aktifkan mode terang' : 'Aktifkan mode gelap'
					"
				>
					<i
						class="mdi text-lg leading-none"
						:class="
							theme.mode === 'dark' ? 'mdi-white-balance-sunny' : 'mdi-weather-night'
						"
					></i>
				</button>

				<!-- Notifikasi (mobile) -->
				<div class="relative">
					<button
						ref="notifButtonMobileRef"
						type="button"
						@click="openNotifications"
						class="relative flex h-9 w-9 items-center justify-center rounded-lg text-[var(--text-muted)] transition duration-300 hover:bg-[var(--surface-hover)] hover:text-[var(--text)] focus:outline-none"
						aria-label="Notifikasi"
					>
						<i class="mdi mdi-bell-outline text-lg leading-none"></i>
						<span
							v-if="unreadCount > 0"
							class="absolute -top-0.5 -right-0.5 flex h-4 min-w-4 items-center justify-center rounded-full bg-[var(--button-bg)] text-[var(--button-text)] px-1 text-[10px] font-bold ring-2 ring-[var(--bg-subtle)]"
						>
							{{ unreadCount > 9 ? "9+" : unreadCount }}
						</span>
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
							v-if="isNotifOpen"
							ref="notifMenuMobileRef"
							class="absolute right-0 mt-2 w-72 max-w-[85vw] bg-[var(--bg-subtle)] rounded-xl border border-[var(--border)] shadow-xl py-1 z-50 origin-top-right max-h-96 overflow-y-auto"
						>
							<div class="flex items-center justify-between px-4 py-2">
								<span
									class="text-xs font-semibold text-[var(--icon)] uppercase tracking-wide"
								>
									Notifikasi
								</span>
								<button
									v-if="unreadCount > 0"
									type="button"
									@click="handleMarkAllRead"
									class="text-xs font-medium text-[var(--text-accent-strong)] hover:underline"
								>
									Tandai semua dibaca
								</button>
							</div>

							<p
								v-if="!notifications.data || notifications.data.length === 0"
								class="px-4 py-6 text-center text-sm text-[var(--icon)]"
							>
								Tidak ada notifikasi
							</p>

							<button
								v-for="notif in notifications.data"
								:key="notif.name"
								type="button"
								@click="handleNotifClick(notif)"
								:class="[
									'flex w-full items-start gap-3 px-4 py-2.5 text-left transition duration-200 hover:bg-[var(--surface-hover)]',
									!notif.read ? 'bg-[var(--surface-accent-hover)]' : '',
								]"
							>
								<span
									class="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-[var(--surface-hover)] text-[var(--text-muted)]"
								>
									<i
										class="mdi text-base leading-none"
										:class="`mdi-${notifIcon(notif)}`"
									></i>
								</span>
								<span class="flex-1 min-w-0">
									<span
										class="block text-sm text-[var(--text-muted)] line-clamp-2"
										>{{ notif.subject }}</span
									>
									<span class="block text-[11px] text-[var(--icon)] mt-0.5">{{
										notif.creation
									}}</span>
								</span>
								<span
									v-if="!notif.read"
									class="mt-1 h-1.5 w-1.5 shrink-0 rounded-full bg-[var(--button-bg)]"
								></span>
							</button>
						</div>
					</Transition>
				</div>

				<!-- Profile (mobile) -->
				<div class="relative">
					<button
						ref="profileButtonMobileRef"
						type="button"
						@click="isProfileOpen = !isProfileOpen"
						class="flex h-9 w-9 items-center justify-center focus:outline-none"
						aria-label="Menu profil"
					>
						<img
							:src="user.avatar ? `${apiUrl}${user.avatar}` : ''"
							alt="Avatar"
							class="h-8 w-8 rounded-full object-cover ring-2 ring-[var(--button-bg)]/40"
						/>
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
							ref="profileMenuMobileRef"
							class="absolute right-0 mt-2 w-48 bg-[var(--bg-subtle)] rounded-xl border border-[var(--border)] shadow-xl py-1 z-50 origin-top-right"
						>
							<div class="px-4 py-2 border-b border-[var(--border-subtle)]">
								<p class="text-sm font-semibold text-[var(--text)] truncate">
									{{ user.name }}
								</p>
								<p class="text-[11px] text-[var(--icon)] capitalize">{{ role }}</p>
							</div>
							<router-link
								:to="safeRoute('Profile')"
								class="block px-4 py-2 text-sm text-[var(--text-muted)] hover:bg-[var(--surface-hover)] hover:text-[var(--text)]"
								@click="isProfileOpen = false"
								>Profil Saya</router-link
							>
							<router-link
								:to="safeRoute('Settings')"
								class="block px-4 py-2 text-sm text-[var(--text-muted)] hover:bg-[var(--surface-hover)] hover:text-[var(--text)]"
								@click="isProfileOpen = false"
								>Pengaturan</router-link
							>
							<div class="my-1 border-t border-[var(--border-subtle)]"></div>
							<button
								type="button"
								class="block w-full text-left px-4 py-2 text-sm text-[var(--color-danger)] hover:bg-[var(--surface-hover)]"
								@click="handleLogout"
							>
								Keluar
							</button>
						</div>
					</Transition>
				</div>

				<!-- Hamburger -->
				<button
					type="button"
					@click="isMobileMenuOpen = !isMobileMenuOpen"
					class="flex h-10 w-10 items-center justify-center rounded-lg text-[var(--text-muted)] transition duration-300 hover:bg-[var(--surface-hover)] focus:outline-none"
					aria-label="Buka menu"
				>
					<i
						class="mdi text-2xl leading-none"
						:class="isMobileMenuOpen ? 'mdi-close' : 'mdi-menu'"
					></i>
				</button>
			</div>
		</header>

		<!-- Overlay Mobile -->
		<div
			v-if="isMobileMenuOpen"
			@click="isMobileMenuOpen = false"
			class="fixed inset-0 bg-[var(--overlay-bg)] z-40 md:hidden"
		></div>

		<!-- SIDEBAR -->
		<aside
			:class="[
				'fixed md:sticky md:top-0 inset-y-0 left-0 z-50 w-72 md:w-64 md:h-screen bg-[var(--bg-subtle)] border-r border-[var(--border)] flex flex-col justify-between transition-transform duration-300 ease-in-out',
				isMobileMenuOpen ? 'translate-x-0' : '-translate-x-full md:translate-x-0',
			]"
		>
			<div class="flex flex-col min-h-0 flex-1">
				<!-- Logo Brand -->
				<div
					class="h-16 flex items-center gap-2.5 px-5 border-b border-[var(--border)] shrink-0"
				>
					<span
						class="flex h-9 w-9 items-center justify-center rounded-xl bg-gradient-to-br from-[var(--button-bg)] to-[var(--button-bg-hover)] text-sm font-bold text-[var(--button-text)] shadow-md"
						>K</span
					>
					<span class="text-lg font-bold tracking-tight text-[var(--text)]"
						>Katalogin</span
					>
				</div>

				<!-- Main Navigation -->
				<nav class="flex-1 overflow-y-auto px-3 py-4 space-y-1">
					<div v-for="item in visibleMenu" :key="item.name">
						<!-- Item tanpa submenu -->
						<router-link
							v-if="!item.children"
							:to="safeRoute(item.route)"
							:class="[
								'flex items-center gap-3 rounded-lg px-4 py-2.5 text-sm font-medium transition duration-300',
								isActiveRoute(item.route)
									? 'bg-gradient-to-r from-[var(--button-bg)] to-transparent text-[var(--button-text)] font-semibold'
									: 'text-[var(--text-muted)] hover:bg-[var(--surface-hover)] hover:text-[var(--text)]',
							]"
							@click="isMobileMenuOpen = false"
						>
							<i
								class="mdi text-lg leading-none shrink-0"
								:class="[
									`mdi-${item.icon}`,
									isActiveRoute(item.route)
										? 'text-[var(--button-text)]'
										: 'text-[var(--icon)]',
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
									'flex w-full items-center justify-between gap-3 rounded-lg px-4 py-2.5 text-sm font-medium transition duration-300',
									hasActiveChild(item)
										? 'text-[var(--button-text)] bg-gradient-to-r from-[var(--button-bg)] to-transparent'
										: 'text-[var(--text-muted)] hover:bg-[var(--surface-hover)] hover:text-[var(--text)]',
								]"
							>
								<span class="flex items-center gap-3">
									<i
										class="mdi text-lg leading-none shrink-0"
										:class="[
											`mdi-${item.icon}`,
											hasActiveChild(item)
												? 'text-[var(--button-text)]'
												: 'text-[var(--icon)]',
										]"
									></i>
									<span>{{ item.name }}</span>
								</span>
								<i
									class="mdi mdi-chevron-down text-base shrink-0 transition-transform duration-300"
									:class="[
										openSubmenu === item.name ? 'rotate-180' : '',
										hasActiveChild(item)
											? 'text-[var(--button-text)]'
											: 'text-[var(--icon)]',
									]"
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
									class="mt-1 ml-4 space-y-0.5 border-l border-[var(--border)] pl-4 overflow-hidden"
								>
									<router-link
										v-for="child in item.children"
										:key="child.name"
										:to="safeRoute(child.route)"
										:class="[
											'flex items-center gap-2.5 rounded-lg px-3 py-2 text-sm transition duration-300',
											isActiveRoute(child.route)
												? 'text-[var(--text-accent-strong)] font-semibold'
												: 'text-[var(--icon)] hover:text-[var(--text)] hover:bg-[var(--surface-hover)]',
										]"
										@click="isMobileMenuOpen = false"
									>
										<i
											v-if="child.icon"
											class="mdi text-base leading-none shrink-0"
											:class="[
												`mdi-${child.icon}`,
												isActiveRoute(child.route)
													? 'text-[var(--text-accent-strong)]'
													: 'text-[var(--icon)]',
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
			<div class="border-t border-[var(--border-subtle)] p-4 space-y-3 shrink-0">
				<div
					class="flex items-center gap-2 rounded-xl bg-[var(--surface-accent)] px-3 py-2"
				>
					<span class="h-1.5 w-1.5 rounded-full bg-[var(--button-bg)]"></span>
					<span
						class="text-xs font-semibold text-[var(--text-accent-strong)] capitalize"
						>{{ role }}</span
					>
				</div>
			</div>
		</aside>

		<!-- CONTENT AREA -->
		<div class="flex-1 flex flex-col min-w-0 h-screen overflow-hidden">
			<!-- Top Navbar (desktop only, mobile version is in the mobile header above) -->
			<header
				class="hidden md:flex h-16 border-b border-[var(--border)] bg-[var(--bg-subtle)]/95 backdrop-blur-sm px-4 md:px-8 items-center justify-between sticky top-0 z-30 shrink-0"
			>
				<!-- Search -->
				<div class="flex-1 max-w-md relative"></div>

				<!-- Right Menu -->
				<div class="flex items-center gap-4">
					<!-- Toggle Dark Mode -->
					<button
						type="button"
						@click="toggleTheme"
						class="flex h-9 w-9 items-center justify-center rounded-lg text-[var(--text-muted)] transition duration-300 hover:bg-[var(--surface-hover)] hover:text-[var(--text)] focus:outline-none"
						:aria-label="
							theme.mode === 'dark' ? 'Aktifkan mode terang' : 'Aktifkan mode gelap'
						"
					>
						<i
							class="mdi text-lg leading-none"
							:class="
								theme.mode === 'dark'
									? 'mdi-white-balance-sunny'
									: 'mdi-weather-night'
							"
						></i>
					</button>

					<!-- Notifikasi -->
					<div class="relative">
						<button
							ref="notifButtonRef"
							type="button"
							@click="openNotifications"
							class="relative flex h-9 w-9 items-center justify-center rounded-lg text-[var(--text-muted)] transition duration-300 hover:bg-[var(--surface-hover)] hover:text-[var(--text)] focus:outline-none"
							aria-label="Notifikasi"
						>
							<i class="mdi mdi-bell-outline text-lg leading-none"></i>
							<span
								v-if="unreadCount > 0"
								class="absolute -top-0.5 -right-0.5 flex h-4 min-w-4 items-center justify-center rounded-full bg-[var(--button-bg)] text-[var(--button-text)] px-1 text-[10px] font-bold ring-2 ring-[var(--bg-subtle)]"
							>
								{{ unreadCount > 9 ? "9+" : unreadCount }}
							</span>
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
								v-if="isNotifOpen"
								ref="notifMenuRef"
								class="absolute right-0 mt-2 w-80 bg-[var(--bg-subtle)] rounded-xl border border-[var(--border)] shadow-xl py-1 z-50 origin-top-right max-h-96 overflow-y-auto"
							>
								<div class="flex items-center justify-between px-4 py-2">
									<span
										class="text-xs font-semibold text-[var(--icon)] uppercase tracking-wide"
									>
										Notifikasi
									</span>
									<button
										v-if="unreadCount > 0"
										type="button"
										@click="handleMarkAllRead"
										class="text-xs font-medium text-[var(--text-accent-strong)] hover:underline"
									>
										Tandai semua dibaca
									</button>
								</div>

								<p
									v-if="!notifications.data || notifications.data.length === 0"
									class="px-4 py-6 text-center text-sm text-[var(--icon)]"
								>
									Tidak ada notifikasi
								</p>

								<button
									v-for="notif in notifications.data"
									:key="notif.name"
									type="button"
									@click="handleNotifClick(notif)"
									:class="[
										'flex w-full items-start gap-3 px-4 py-2.5 text-left transition duration-200 hover:bg-[var(--surface-hover)]',
										!notif.read ? 'bg-[var(--surface-accent-hover)]' : '',
									]"
								>
									<span
										class="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-[var(--surface-hover)] text-[var(--text-muted)]"
									>
										<i
											class="mdi text-base leading-none"
											:class="`mdi-${notifIcon(notif)}`"
										></i>
									</span>
									<span class="flex-1 min-w-0">
										<span
											class="block text-sm text-[var(--text-muted)] line-clamp-2"
											>{{ notif.subject }}</span
										>
										<span
											class="block text-[11px] text-[var(--icon)] mt-0.5"
											>{{ notif.creation }}</span
										>
									</span>
									<span
										v-if="!notif.read"
										class="mt-1 h-1.5 w-1.5 shrink-0 rounded-full bg-[var(--button-bg)]"
									></span>
								</button>
							</div>
						</Transition>
					</div>

					<div class="h-5 w-px bg-[var(--border)]"></div>

					<!-- Profile Dropdown -->
					<div class="relative">
						<button
							ref="profileButtonRef"
							type="button"
							@click="isProfileOpen = !isProfileOpen"
							class="flex items-center gap-2.5 focus:outline-none"
						>
							<img
								:src="user.avatar ? `${apiUrl}${user.avatar}` : ''"
								alt="Avatar"
								class="h-8 w-8 rounded-full object-cover ring-2 ring-[var(--button-bg)]/40"
							/>
							<span class="hidden sm:flex flex-col items-start leading-tight">
								<span class="text-sm font-semibold text-[var(--text)]">{{
									user.name
								}}</span>
								<span class="text-[11px] text-[var(--icon)] capitalize">{{
									role
								}}</span>
							</span>
							<i
								class="mdi mdi-chevron-down text-base leading-none text-[var(--icon)]"
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
								class="absolute right-0 mt-2 w-48 bg-[var(--bg-subtle)] rounded-xl border border-[var(--border)] shadow-xl py-1 z-50 origin-top-right"
							>
								<router-link
									:to="safeRoute('Profile')"
									class="block px-4 py-2 text-sm text-[var(--text-muted)] hover:bg-[var(--surface-hover)] hover:text-[var(--text)]"
									@click="isProfileOpen = false"
									>Profil Saya</router-link
								>
								<router-link
									:to="safeRoute('Settings')"
									class="block px-4 py-2 text-sm text-[var(--text-muted)] hover:bg-[var(--surface-hover)] hover:text-[var(--text)]"
									@click="isProfileOpen = false"
									>Pengaturan</router-link
								>
								<div class="my-1 border-t border-[var(--border-subtle)]"></div>
								<button
									type="button"
									class="block w-full text-left px-4 py-2 text-sm text-[var(--color-danger)] hover:bg-[var(--surface-hover)]"
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

		<!-- Modal Detail Notifikasi -->
		<Transition
			enter-active-class="transition duration-200 ease-out"
			enter-from-class="opacity-0"
			enter-to-class="opacity-100"
			leave-active-class="transition duration-150 ease-in"
			leave-from-class="opacity-100"
			leave-to-class="opacity-0"
		>
			<div
				v-if="selectedNotif"
				class="fixed inset-0 z-[60] flex items-center justify-center bg-[var(--overlay-bg)] p-4"
				@click.self="closeNotifDetail"
			>
				<div
					class="w-full max-w-lg bg-[var(--bg-subtle)] rounded-2xl shadow-2xl overflow-hidden"
				>
					<div
						class="flex items-start justify-between gap-4 px-6 py-4 border-b border-[var(--border-subtle)]"
					>
						<h3 class="text-base font-semibold text-[var(--text)]">
							{{ selectedNotif.subject }}
						</h3>
						<button
							type="button"
							@click="closeNotifDetail"
							class="text-[var(--icon)] hover:text-[var(--text-muted)] shrink-0"
							aria-label="Tutup"
						>
							<i class="mdi mdi-close text-xl leading-none"></i>
						</button>
					</div>
					<div class="px-6 py-4 max-h-96 overflow-y-auto">
						<p class="text-sm text-[var(--text-muted)] whitespace-pre-line">
							{{ selectedNotif.email_content || "Tidak ada detail tambahan." }}
						</p>
						<p class="text-xs text-[var(--icon)] mt-4">
							{{ selectedNotif.creation }}
						</p>
					</div>
					<div
						class="flex justify-end gap-2 px-6 py-3 border-t border-[var(--border-subtle)] bg-[var(--surface-hover)]/50"
					>
						<button
							type="button"
							@click="closeNotifDetail"
							class="px-4 py-2 text-sm font-medium rounded-lg text-[var(--text-muted)] hover:bg-[var(--surface-hover)]"
						>
							Tutup
						</button>
					</div>
				</div>
			</div>
		</Transition>
	</div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from "vue";
import { session, ensureUserRole } from "../auth/session.js";
import { theme, toggleTheme } from "../auth/theme.js";
import { useRoute, useRouter } from "vue-router";
import { menuItems, filterMenuByRole } from "../helpers/menu.js";
import { createResource, call } from "frappe-ui";
import { io } from "socket.io-client";

import Swal from "sweetalert2";

const apiUrl = import.meta.env.VITE_API_URL;
const siteName = import.meta.env.VITE_SITE_NAME;
const socketioPort = import.meta.env.VITE_SOCKETIO_PORT;

const role = computed(() => session.currentUser.role);
const user = computed(() => session.currentUser);

onMounted(async () => {
	await ensureUserRole();
});

const isMobileMenuOpen = ref(false);
const isProfileOpen = ref(false);
const openSubmenu = ref(null);
const profileButtonRef = ref(null);
const profileMenuRef = ref(null);

const isNotifOpen = ref(false);
const notifButtonRef = ref(null);
const notifMenuRef = ref(null);
const notifButtonMobileRef = ref(null);
const notifMenuMobileRef = ref(null);
const profileButtonMobileRef = ref(null);
const profileMenuMobileRef = ref(null);

function handleClickOutside(event) {
	if (isProfileOpen.value) {
		const clickedButton =
			profileButtonRef.value?.contains(event.target) ||
			profileButtonMobileRef.value?.contains(event.target);
		const clickedMenu =
			profileMenuRef.value?.contains(event.target) ||
			profileMenuMobileRef.value?.contains(event.target);
		if (!clickedButton && !clickedMenu) isProfileOpen.value = false;
	}
	if (isNotifOpen.value) {
		const clickedNotifButton =
			notifButtonRef.value?.contains(event.target) ||
			notifButtonMobileRef.value?.contains(event.target);
		const clickedNotifMenu =
			notifMenuRef.value?.contains(event.target) ||
			notifMenuMobileRef.value?.contains(event.target);
		if (!clickedNotifButton && !clickedNotifMenu) isNotifOpen.value = false;
	}
}

onMounted(() => document.addEventListener("click", handleClickOutside));
onUnmounted(() => document.removeEventListener("click", handleClickOutside));

const route = useRoute();
const router = useRouter();

function safeRoute(routeName) {
	if (!routeName) return "#";
	if (router.hasRoute(routeName)) return { name: routeName };
	console.warn(`[menu.js] Route "${routeName}" belum terdaftar di router.`);
	return "#";
}

const visibleMenu = computed(() => filterMenuByRole(menuItems, role.value));

function toggleSubmenu(name) {
	openSubmenu.value = openSubmenu.value === name ? null : name;
}

function isActiveRoute(routeName) {
	if (!routeName) return false;
	if (route.name === routeName) return true;
	if (route.matched.some((r) => r.name === routeName)) return true;
	if (route.meta?.activeMenu === routeName) return true;

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
		confirmButtonColor: "var(--color-danger)",
		cancelButtonColor: "var(--gray-9)",
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

visibleMenu.value.forEach((item) => {
	if (item.children && hasActiveChild(item)) {
		openSubmenu.value = item.name;
	}
});

const notifications = createResource({
	url: "frappe.client.get_list",
	params: {
		doctype: "Notification Log",
		fields: [
			"name",
			"subject",
			"type",
			"document_type",
			"document_name",
			"read",
			"creation",
			"email_content",
		],
		filters: { for_user: session.currentUser.id },
		order_by: "creation desc",
		limit_page_length: 10,
	},
	auto: true,
});

const unreadCount = computed(() => notifications.data?.filter((n) => !n.read)?.length ?? 0);

const selectedNotif = ref(null);

function openNotifications() {
	isNotifOpen.value = !isNotifOpen.value;
	if (isNotifOpen.value) {
		notifications.reload();
	}
}

async function markNotifAsRead(notifName) {
	try {
		await call("bizpage.api.dashboard_api.mark_notification_read", {
			name: notifName,
		});
		return true;
	} catch (error) {
		console.error("Gagal tandai notifikasi sebagai dibaca:", error);
		return false;
	}
}

async function handleNotifClick(notif) {
	selectedNotif.value = notif;
	isNotifOpen.value = false;

	if (!notif.read) {
		const success = await markNotifAsRead(notif.name);
		if (success) {
			notif.read = 1;
			notifications.reload();
		}
	}
}

function closeNotifDetail() {
	selectedNotif.value = null;
}

async function handleMarkAllRead() {
	try {
		await call("bizpage.api.dashboard_api.mark_all_notifications_read");
		notifications.reload();
	} catch (error) {
		console.error("Gagal tandai semua notifikasi sebagai dibaca:", error);
	}
}

function notifIcon(notif) {
	if (notif.document_type === "Sales Order" || notif.document_type === "Pesanan") {
		return "cart-outline";
	}
	const typeMap = {
		Alert: "alert-circle-outline",
		Mention: "at",
		Assignment: "clipboard-check-outline",
		Share: "share-variant",
		"Energy Point": "star-outline",
	};
	return typeMap[notif.type] || "bell-outline";
}

let socket = null;

function connectNotificationSocket() {
	const backend = new URL(apiUrl);
	const port = socketioPort ? `:${socketioPort}` : "";
	const url = `${backend.protocol}//${backend.hostname}${port}/${siteName}`;
	return io(url, { withCredentials: true });
}

let notifInterval = null;

function handleVisibilityChange() {
	if (document.visibilityState === "visible") {
		notifications.reload();
	}
}

onMounted(() => {
	socket = connectNotificationSocket();
	socket.on("notification", () => {
		notifications.reload();
	});

	document.addEventListener("visibilitychange", handleVisibilityChange);
	notifInterval = setInterval(() => notifications.reload(), 120000);
});

onUnmounted(() => {
	socket?.off("notification");
	socket?.disconnect();
	document.removeEventListener("visibilitychange", handleVisibilityChange);
	if (notifInterval) clearInterval(notifInterval);
});
</script>
