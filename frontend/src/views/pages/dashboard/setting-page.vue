<template>
	<MainLayout>
		<div class="max-w-2xl mx-auto">
			<div class="mb-6">
				<h1 class="text-xl font-bold text-slate-900 dark:text-slate-100">Pengaturan</h1>
				<p class="text-sm text-slate-500 dark:text-slate-400 mt-1">
					Kelola tampilan dan keamanan akun kamu.
				</p>
			</div>

			<!-- Card: Tampilan -->
			<div
				class="bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-sm mb-6"
			>
				<div class="px-6 py-4 border-b border-slate-100 dark:border-slate-800">
					<h2 class="text-sm font-semibold text-slate-700 dark:text-slate-200">
						Tampilan
					</h2>
				</div>

				<div class="p-6">
					<div class="flex items-center justify-between">
						<div>
							<p class="text-sm font-medium text-slate-700 dark:text-slate-200">
								Mode Gelap
							</p>
							<p class="text-xs text-slate-400 dark:text-slate-500 mt-0.5">
								Ubah tampilan aplikasi jadi lebih gelap, nyaman di mata saat malam.
							</p>
						</div>

						<!-- Toggle switch -->
						<button
							type="button"
							role="switch"
							:aria-checked="theme.mode === 'dark'"
							@click="toggleTheme"
							:class="[
								'relative inline-flex h-6 w-11 shrink-0 items-center rounded-full transition-colors duration-200 focus:outline-none',
								theme.mode === 'dark'
									? 'bg-[var(--color-primary)]'
									: 'bg-slate-200 dark:bg-slate-700',
							]"
						>
							<span
								:class="[
									'inline-block h-4 w-4 transform rounded-full bg-white shadow transition-transform duration-200',
									theme.mode === 'dark' ? 'translate-x-6' : 'translate-x-1',
								]"
							></span>
						</button>
					</div>
				</div>
			</div>

			<!-- Card: Ubah Password -->
			<div
				class="bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-sm"
			>
				<div class="px-6 py-4 border-b border-slate-100 dark:border-slate-800">
					<h2 class="text-sm font-semibold text-slate-700 dark:text-slate-200">
						Ubah Password
					</h2>
				</div>

				<div class="p-6 space-y-5">
					<div>
						<label
							class="block text-sm font-medium text-slate-600 dark:text-slate-300 mb-1.5"
							for="old_password"
						>
							Password Lama
						</label>
						<input
							id="old_password"
							v-model="passwordForm.oldPassword"
							type="password"
							autocomplete="current-password"
							class="w-full px-3 py-2 rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-sm text-slate-700 dark:text-slate-100 focus:outline-none focus:ring-2 focus:ring-[var(--color-focus-ring)]"
						/>
					</div>

					<div>
						<label
							class="block text-sm font-medium text-slate-600 dark:text-slate-300 mb-1.5"
							for="new_password"
						>
							Password Baru
						</label>
						<input
							id="new_password"
							v-model="passwordForm.newPassword"
							type="password"
							autocomplete="new-password"
							class="w-full px-3 py-2 rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-sm text-slate-700 dark:text-slate-100 focus:outline-none focus:ring-2 focus:ring-[var(--color-focus-ring)]"
						/>
						<p class="text-xs text-slate-400 dark:text-slate-500 mt-1">
							Minimal 8 karakter.
						</p>
					</div>

					<div>
						<label
							class="block text-sm font-medium text-slate-600 dark:text-slate-300 mb-1.5"
							for="confirm_password"
						>
							Konfirmasi Password Baru
						</label>
						<input
							id="confirm_password"
							v-model="passwordForm.confirmPassword"
							type="password"
							autocomplete="new-password"
							class="w-full px-3 py-2 rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-sm text-slate-700 dark:text-slate-100 focus:outline-none focus:ring-2 focus:ring-[var(--color-focus-ring)]"
						/>
					</div>
				</div>

				<div
					class="flex items-center justify-between gap-3 px-6 py-4 border-t border-slate-100 dark:border-slate-800 bg-slate-50 dark:bg-slate-800/50 rounded-b-2xl"
				>
					<p v-if="passwordError" class="text-xs text-[var(--color-danger)]">
						{{ passwordError }}
					</p>
					<span v-else></span>

					<button
						type="button"
						:disabled="isChangingPassword"
						@click="handleChangePassword"
						class="flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-medium text-white bg-[var(--color-primary)] transition duration-200 hover:opacity-90 disabled:opacity-50 disabled:cursor-not-allowed"
					>
						<i
							v-if="isChangingPassword"
							class="mdi mdi-loading mdi-spin text-base leading-none"
						></i>
						{{ isChangingPassword ? "Menyimpan..." : "Ubah Password" }}
					</button>
				</div>
			</div>
		</div>
	</MainLayout>
</template>

<script setup>
import { reactive, ref } from "vue";
import { theme, toggleTheme } from "../../../auth/theme.js";
import MainLayout from "../../../components/main-layout.vue";
import { call } from "frappe-ui";
import Swal from "sweetalert2";

const passwordForm = reactive({
	oldPassword: "",
	newPassword: "",
	confirmPassword: "",
});

const isChangingPassword = ref(false);
const passwordError = ref("");

// ---------------------------------------------------------------------
// ⚠️ PERLU VERIFIKASI: method di bawah ini (frappe.core.doctype.user.user.
// update_password) adalah method BAWAAN Frappe yang biasa dipakai dialog
// "Change Password" di Desk sendiri — bukan endpoint custom buatan kita.
// Tapi signature parameter-nya BISA BEDA tergantung versi Frappe kamu.
// Cek dulu sebelum percaya ini jalan:
//   grep -n "def update_password" apps/frappe/frappe/core/doctype/user/user.py
// Lihat parameter apa saja yang diterima (nama param old_password/new_password
// bisa saja beda).
// ---------------------------------------------------------------------
async function handleChangePassword() {
	passwordError.value = "";

	if (!passwordForm.oldPassword || !passwordForm.newPassword || !passwordForm.confirmPassword) {
		passwordError.value = "Semua kolom wajib diisi.";
		return;
	}
	if (passwordForm.newPassword.length < 8) {
		passwordError.value = "Password baru minimal 8 karakter.";
		return;
	}
	if (passwordForm.newPassword !== passwordForm.confirmPassword) {
		passwordError.value = "Konfirmasi password tidak cocok.";
		return;
	}

	isChangingPassword.value = true;

	try {
		await call("frappe.core.doctype.user.user.update_password", {
			old_password: passwordForm.oldPassword,
			new_password: passwordForm.newPassword,
		});

		passwordForm.oldPassword = "";
		passwordForm.newPassword = "";
		passwordForm.confirmPassword = "";

		await Swal.fire({
			title: "Password diperbarui!",
			text: "Password kamu berhasil diubah.",
			icon: "success",
			timer: 1500,
			showConfirmButton: false,
		});
	} catch (error) {
		console.error("Gagal ubah password:", error);
		// Pesan error dari Frappe biasanya sudah cukup jelas (mis. "password lama salah"),
		// tampilkan langsung kalau ada.
		passwordError.value =
			error?.messages?.[0] || error?.message || "Gagal mengubah password. Coba lagi.";
	} finally {
		isChangingPassword.value = false;
	}
}
</script>
