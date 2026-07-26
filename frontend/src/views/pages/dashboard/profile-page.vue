<template>
	<MainLayout>
		<div class="max-w-2xl mx-auto">
			<!-- Header halaman -->
			<div class="mb-6">
				<h1 class="text-xl font-bold text-slate-900">Profil Saya</h1>
				<p class="text-sm text-slate-500 mt-1">
					Kelola informasi akun dan data pribadi kamu.
				</p>
			</div>

			<!-- Loading state -->
			<div v-if="isLoading" class="flex items-center justify-center py-20">
				<i class="mdi mdi-loading mdi-spin text-3xl text-slate-300"></i>
			</div>

			<template v-else>
				<!-- Card: Avatar + identitas ringkas (dari doctype User) -->
				<div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 mb-6">
					<div class="flex items-center gap-4">
						<div class="relative shrink-0">
							<img
								:src="
									avatarPreview || (user.avatar ? `${apiUrl}${user.avatar}` : '')
								"
								alt="Avatar"
								class="h-16 w-16 rounded-full object-cover ring-2 ring-slate-100 bg-slate-100"
							/>
							<button
								type="button"
								@click="triggerFilePicker"
								:disabled="isUploadingAvatar"
								class="absolute -bottom-1 -right-1 flex h-6 w-6 items-center justify-center rounded-full bg-[var(--color-primary)] text-white shadow-md hover:opacity-90 disabled:opacity-50"
								aria-label="Ganti foto profil"
							>
								<i
									class="mdi text-xs leading-none"
									:class="
										isUploadingAvatar ? 'mdi-loading mdi-spin' : 'mdi-camera'
									"
								></i>
							</button>
							<input
								ref="fileInputRef"
								type="file"
								accept="image/png, image/jpeg, image/webp"
								class="hidden"
								@change="handleAvatarSelected"
							/>
						</div>
						<div class="min-w-0">
							<p class="text-base font-semibold text-slate-800 truncate">
								{{ form.owner_name || user.name }}
							</p>
							<!-- Email dari doctype User -->
							<p class="text-sm text-slate-400 truncate">{{ user.id }}</p>
							<p v-if="avatarError" class="text-xs text-[var(--color-danger)] mt-1">
								{{ avatarError }}
							</p>
						</div>
					</div>
				</div>

				<!-- Card: Form data pribadi (dari doctype Owner) -->
				<div class="bg-white rounded-2xl border border-slate-200 shadow-sm">
					<div class="px-6 py-4 border-b border-slate-100">
						<h2 class="text-sm font-semibold text-slate-700">Informasi Pribadi</h2>
					</div>

					<div class="p-6 space-y-5">
						<!-- Owner Name -->
						<div>
							<label
								class="block text-sm font-medium text-slate-600 mb-1.5"
								for="owner_name"
							>
								Nama
							</label>
							<input
								id="owner_name"
								v-model="form.owner_name"
								type="text"
								placeholder="Nama lengkap"
								class="w-full px-3 py-2 rounded-lg border border-slate-200 text-sm text-slate-700 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-[var(--color-focus-ring)]"
							/>
						</div>

						<!-- Gender -->
						<div>
							<label
								class="block text-sm font-medium text-slate-600 mb-1.5"
								for="gender"
							>
								Jenis Kelamin
							</label>
							<select
								id="gender"
								v-model="form.gender"
								class="w-full px-3 py-2 rounded-lg border border-slate-200 text-sm text-slate-700 focus:outline-none focus:ring-2 focus:ring-[var(--color-focus-ring)]"
							>
								<option value="" disabled>Pilih jenis kelamin</option>
								<!--
									⚠️ Opsi ini masih ASUMSI. Cek opsi asli di Desk:
									Customize Form → Owner → field "Gender" → lihat isian "Options".
								-->
								<option value="Male">Laki-laki</option>
								<option value="Female">Perempuan</option>
								<option value="Other">Lainnya</option>
							</select>
						</div>

						<!-- Phone Number -->
						<div>
							<label
								class="block text-sm font-medium text-slate-600 mb-1.5"
								for="phone"
							>
								Nomor Telepon
							</label>
							<input
								id="phone"
								v-model="form.phone_number"
								type="tel"
								placeholder="08xxxxxxxxxx"
								class="w-full px-3 py-2 rounded-lg border border-slate-200 text-sm text-slate-700 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-[var(--color-focus-ring)]"
							/>
						</div>

						<!-- Birthday -->
						<div>
							<label
								class="block text-sm font-medium text-slate-600 mb-1.5"
								for="birthday"
							>
								Tanggal Lahir
							</label>
							<input
								id="birthday"
								v-model="form.birthday"
								type="date"
								class="w-full px-3 py-2 rounded-lg border border-slate-200 text-sm text-slate-700 focus:outline-none focus:ring-2 focus:ring-[var(--color-focus-ring)]"
							/>
						</div>
					</div>

					<!-- Footer: tombol simpan -->
					<div
						class="flex items-center justify-between gap-3 px-6 py-4 border-t border-slate-100 bg-slate-50 rounded-b-2xl"
					>
						<p v-if="saveError" class="text-xs text-[var(--color-danger)]">
							{{ saveError }}
						</p>
						<span v-else></span>

						<button
							type="button"
							:disabled="isSaving"
							@click="handleSave"
							class="flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-medium text-white bg-[var(--color-primary)] transition duration-200 hover:opacity-90 disabled:opacity-50 disabled:cursor-not-allowed"
						>
							<i
								v-if="isSaving"
								class="mdi mdi-loading mdi-spin text-base leading-none"
							></i>
							{{ isSaving ? "Menyimpan..." : "Simpan Perubahan" }}
						</button>
					</div>
				</div>
			</template>
		</div>
	</MainLayout>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from "vue";
import { session } from "../../../auth/session.js";
import MainLayout from "../../../components/main-layout.vue";
import { call } from "frappe-ui";
import Swal from "sweetalert2";

// apiUrl HANYA dipakai untuk menampilkan gambar (<img src>), BUKAN untuk
// fetch/upload — karena request fetch/upload harus lewat proxy Vite
// (path relatif) supaya tidak kena CORS. Lihat penjelasan di handleAvatarSelected.
const apiUrl = import.meta.env.VITE_API_URL;

const user = computed(() => session.currentUser);

const isLoading = ref(true);
const isSaving = ref(false);
const saveError = ref("");

// Menandai apakah record Owner untuk user ini sudah ada atau belum.
// Kalau belum ada, handleSave akan membuat baru (upsert), bukan gagal.
const hasOwnerRecord = ref(false);

const form = reactive({
	owner_name: "",
	gender: "",
	phone_number: "",
	birthday: "",
});

// ---------------------------------------------------------------------
// Ambil data profil gabungan: identitas (email/avatar) dari User,
// data pribadi (owner_name, gender, phone_number, birthday) dari Owner.
// Lewat method custom supaya tidak butuh Read permission mentah ke Owner,
// dan supaya "belum punya record Owner" ditangani rapi (bukan error).
// ---------------------------------------------------------------------
async function loadOwnerProfile() {
	isLoading.value = true;
	try {
		const result = await call("bizpage.api.dashboard_api.get_owner_profile");

		if (result) {
			hasOwnerRecord.value = !!result.exists;
			form.owner_name = result.owner_name || "";
			form.gender = result.gender || "";
			form.phone_number = result.phone_number || "";
			form.birthday = result.birthday || "";
		}
	} catch (error) {
		console.error("Gagal memuat profil:", error);
	} finally {
		isLoading.value = false;
	}
}

// ---------------------------------------------------------------------
// Simpan perubahan. Method custom ini upsert di sisi backend:
// kalau record Owner belum ada untuk user ini, dibuat baru;
// kalau sudah ada, diupdate. Frontend tidak perlu tahu bedanya.
// ---------------------------------------------------------------------
async function handleSave() {
	isSaving.value = true;
	saveError.value = "";

	try {
		await call("bizpage.api.dashboard_api.save_owner_profile", {
			owner_name: form.owner_name,
			gender: form.gender,
			phone_number: form.phone_number,
			birthday: form.birthday,
		});

		hasOwnerRecord.value = true;

		await Swal.fire({
			title: "Tersimpan!",
			text: "Profil kamu berhasil diperbarui.",
			icon: "success",
			timer: 1500,
			showConfirmButton: false,
		});
	} catch (error) {
		console.error("Gagal menyimpan profil:", error);
		saveError.value = "Gagal menyimpan perubahan. Coba lagi.";
	} finally {
		isSaving.value = false;
	}
}

// ---------------------------------------------------------------------
// Upload avatar — dua tahap:
// 1) Upload file mentah ke endpoint generik bawaan Frappe (upload_file),
//    PAKAI PATH RELATIF (bukan apiUrl) supaya lewat proxy Vite dan tidak
//    kena CORS — sama seperti request call() dari frappe-ui yang selama
//    ini berhasil.
// 2) Simpan path hasil upload lewat method custom sendiri
//    (bizpage.api.dashboard_api.update_avatar) ke field avatar di User.
// ---------------------------------------------------------------------
const fileInputRef = ref(null);
const isUploadingAvatar = ref(false);
const avatarPreview = ref("");
const avatarError = ref("");

function triggerFilePicker() {
	avatarError.value = "";
	fileInputRef.value?.click();
}

async function handleAvatarSelected(event) {
	const file = event.target.files?.[0];
	if (!file) return;

	if (!file.type.startsWith("image/")) {
		avatarError.value = "File harus berupa gambar.";
		return;
	}
	if (file.size > 2 * 1024 * 1024) {
		avatarError.value = "Ukuran gambar maksimal 2MB.";
		return;
	}

	avatarError.value = "";
	avatarPreview.value = URL.createObjectURL(file);
	isUploadingAvatar.value = true;

	try {
		const formData = new FormData();
		formData.append("file", file);
		formData.append("is_private", "0");

		// ⚠️ PENTING: path relatif "/api/method/upload_file", BUKAN
		// `${apiUrl}/api/method/upload_file`. Path relatif diteruskan lewat
		// proxy Vite (dev server) ke backend tanpa perlu izin CORS eksplisit,
		// karena browser menganggapnya same-origin. Kalau pakai apiUrl
		// (cross-origin langsung), browser wajib dapat header
		// Access-Control-Allow-Origin dari backend — yang belum dikonfigurasi,
		// makanya sebelumnya gagal dengan CORS error.
		const uploadRes = await fetch("/api/method/upload_file", {
			method: "POST",
			body: formData,
			credentials: "include",
		});

		if (!uploadRes.ok) throw new Error("Upload gagal, status: " + uploadRes.status);

		const uploadJson = await uploadRes.json();
		const fileUrl = uploadJson?.message?.file_url;
		if (!fileUrl) throw new Error("Respon upload tidak berisi file_url");

		await call("bizpage.api.dashboard_api.update_avatar", {
			file_url: fileUrl,
		});

		session.currentUser.avatar = fileUrl;

		await Swal.fire({
			title: "Foto diperbarui!",
			icon: "success",
			timer: 1200,
			showConfirmButton: false,
		});
	} catch (error) {
		console.error("Gagal upload avatar:", error);
		avatarError.value = "Gagal mengunggah foto. Coba lagi.";
		avatarPreview.value = "";
	} finally {
		isUploadingAvatar.value = false;
		event.target.value = "";
	}
}

onMounted(() => {
	loadOwnerProfile();
});
</script>
