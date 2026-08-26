<template>
	<div class="min-h-screen flex items-center justify-center bg-slate-50 dark:bg-slate-950 px-4">
		<div class="w-full max-w-sm">
			<div class="flex justify-center mb-6">
				<span
					class="flex h-10 w-10 items-center justify-center rounded-xl bg-[var(--color-primary)] text-sm font-bold text-white shadow-md"
					>K</span
				>
			</div>

			<div
				class="bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-sm p-6"
			>
				<template v-if="!isSent">
					<h1 class="text-lg font-bold text-slate-900 dark:text-slate-100 text-center">
						Lupa Password?
					</h1>
					<p class="text-sm text-slate-500 dark:text-slate-400 text-center mt-1 mb-6">
						Masukkan email akun kamu, kami kirim link untuk atur ulang password.
					</p>

					<form @submit.prevent="handleSubmit" class="space-y-4">
						<div>
							<label
								class="block text-sm font-medium text-slate-600 dark:text-slate-300 mb-1.5"
								for="email"
							>
								Email
							</label>
							<input
								id="email"
								v-model="email"
								type="email"
								required
								autocomplete="email"
								placeholder="nama@email.com"
								class="w-full px-3 py-2 rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-sm text-slate-700 dark:text-slate-100 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-[var(--color-focus-ring)]"
							/>
						</div>

						<p v-if="errorMessage" class="text-xs text-[var(--color-danger)]">
							{{ errorMessage }}
						</p>

						<button
							type="submit"
							:disabled="isSubmitting"
							class="w-full flex items-center justify-center gap-2 px-4 py-2.5 rounded-lg text-sm font-medium text-white bg-[var(--color-primary)] transition duration-200 hover:opacity-90 disabled:opacity-50 disabled:cursor-not-allowed"
						>
							<i
								v-if="isSubmitting"
								class="mdi mdi-loading mdi-spin text-base leading-none"
							></i>
							{{ isSubmitting ? "Mengirim..." : "Kirim Link Reset" }}
						</button>
					</form>
				</template>

				<!-- State setelah berhasil kirim -->
				<template v-else>
					<div class="flex justify-center mb-4">
						<span
							class="flex h-12 w-12 items-center justify-center rounded-full bg-[var(--color-accent-light)] text-[var(--color-accent-active)]"
						>
							<i class="mdi mdi-email-check-outline text-2xl leading-none"></i>
						</span>
					</div>
					<h1 class="text-lg font-bold text-slate-900 dark:text-slate-100 text-center">
						Cek Email Kamu
					</h1>
					<p class="text-sm text-slate-500 dark:text-slate-400 text-center mt-1">
						Kami sudah kirim link reset password ke
						<span class="font-medium text-slate-700 dark:text-slate-200">{{
							email
						}}</span>
						kalau email itu terdaftar. Cek juga folder spam kalau belum kelihatan.
					</p>
				</template>

				<div class="mt-6 text-center">
					<router-link
						to="/login"
						class="text-sm font-medium text-[var(--color-primary)] hover:underline"
					>
						← Kembali ke Login
					</router-link>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref } from "vue";
import { call } from "frappe-ui";

const email = ref("");
const isSubmitting = ref(false);
const isSent = ref(false);
const errorMessage = ref("");

// ---------------------------------------------------------------------
// ⚠️ PERLU VERIFIKASI: method bawaan Frappe untuk trigger email reset
// password. Nama & parameter method ini BISA BEDA tergantung versi.
// Cek dulu sebelum percaya ini jalan:
//   grep -n "def reset_password" apps/frappe/frappe/core/doctype/user/user.py
// Kalau nama method/parameternya beda, sesuaikan baris call() di bawah.
//
// Juga WAJIB: server Frappe kamu harus sudah dikonfigurasi bisa kirim
// email (Desk → Email Account → outgoing SMTP), kalau belum, method ini
// mungkin tidak error tapi email tidak pernah terkirim.
// ---------------------------------------------------------------------
async function handleSubmit() {
	errorMessage.value = "";
	isSubmitting.value = true;

	try {
		await call("frappe.core.doctype.user.user.reset_password", {
			user: email.value,
		});

		// Sengaja selalu tampilkan sukses (walau email tidak terdaftar)
		// supaya tidak bocorkan info "email ini terdaftar atau tidak" ke
		// orang luar — praktik keamanan standar untuk fitur forgot password.
		isSent.value = true;
	} catch (error) {
		console.error("Gagal kirim reset password:", error);
		errorMessage.value = "Gagal mengirim link reset. Coba lagi beberapa saat.";
	} finally {
		isSubmitting.value = false;
	}
}
</script>
