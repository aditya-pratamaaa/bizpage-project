<template>
	<MainLayout :role="currentUser.role" :user="currentUser">
		<div class="bizpage-header">
			<h1 class="bizpage-header-title">Pengaturan Website</h1>
			<p class="bizpage-header-subtitle">Atur website kamu</p>
		</div>

		<div class="bizpage-website-content">
			<div class="bizpage-website-content__right">
				<div class="bizpage-form-group" style="margin-bottom: 1.5rem">
					<h1 class="bizpage-form-title">Info Dasar Website</h1>

					<div class="bizpage-form-input">
						<label class="bizpage-form-label">Nama Bisnis</label>
						<input
							class="bizpage-form-data_input"
							type="text"
							placeholder="Masukkan nama bisnis"
						/>
					</div>

					<div class="bizpage-form-input">
						<label class="bizpage-form-label">No Tlp Bisnis</label>
						<input
							class="bizpage-form-data_input"
							type="text"
							inputmode="numeric"
							placeholder="08123456789"
							v-model="form.phone"
							@input="form.phone = form.phone.replace(/\D/g, '')"
						/>
					</div>
					<div class="bizpage-form-input">
						<label class="bizpage-form-label">Deskripsi Bisnis</label>
						<div class="bizpage-editor-wrapper" @click="focusEditor">
							<TextEditor
								ref="textEditorRef"
								:content="form.description"
								@change="(val) => (form.description = val)"
								placeholder=""
								:fixed-menu="true"
							/>
						</div>
					</div>
				</div>
				<div class="bizpage-form-group">
					<h1 class="bizpage-form-title">Banner & Logo</h1>

					<!-- Grid 3 Kolom: Logo (1fr) dan Banner Background (2fr) -->
					<div class="grid grid-cols-3 gap-6 mt-4">
						<!-- LOGO SECTION (Satu File) -->
						<div class="col-span-1">
							<h2 class="text-sm font-semibold mb-2">Logo (Maks 1)</h2>

							<div class="mt-2 h-40">
								<label
									v-if="!logoUrl"
									class="w-full h-full border-2 border-dashed border-gray-400 rounded-2xl flex flex-col items-center justify-center cursor-pointer hover:bg-gray-50 hover:border-gray-500 transition-all duration-200"
								>
									<input
										type="file"
										class="hidden"
										@change="handleLogoUpload"
										accept="image/*"
										:disabled="isUploadingLogo"
									/>
									<svg
										v-if="!isUploadingLogo"
										xmlns="http://www.w3.org/2000/svg"
										class="w-8 h-8 text-gray-400"
										fill="none"
										viewBox="0 0 24 24"
										stroke="currentColor"
										stroke-width="2"
									>
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											d="M12 4v16m8-8H4"
										/>
									</svg>
									<span v-else class="text-sm text-gray-500 mt-2"
										>Uploading...</span
									>
								</label>

								<div
									v-else
									class="relative w-full h-full rounded-2xl border border-gray-200 overflow-hidden shadow-sm"
								>
									<img
										:src="logoUrl"
										alt="Logo"
										class="w-full h-full object-cover"
									/>
									<button
										@click="logoUrl = ''"
										class="absolute top-2 right-2 bg-red-500 text-white rounded-full w-7 h-7 flex items-center justify-center hover:bg-red-600"
									>
										✕
									</button>
								</div>
							</div>
						</div>

						<!-- BANNER BACKGROUND SECTION (Satu File) -->
						<div class="col-span-2">
							<h2 class="text-sm font-semibold mb-2">Banner Background (Maks 1)</h2>

							<div class="mt-2 h-40">
								<label
									v-if="!bannerBgUrl"
									class="w-full h-full border-2 border-dashed border-gray-400 rounded-2xl flex flex-col items-center justify-center cursor-pointer hover:bg-gray-50 hover:border-gray-500 transition-all duration-200"
								>
									<input
										type="file"
										class="hidden"
										@change="handleBannerBgUpload"
										accept="image/*"
										:disabled="isUploadingBannerBg"
									/>
									<svg
										v-if="!isUploadingBannerBg"
										xmlns="http://www.w3.org/2000/svg"
										class="w-8 h-8 text-gray-400"
										fill="none"
										viewBox="0 0 24 24"
										stroke="currentColor"
										stroke-width="2"
									>
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											d="M12 4v16m8-8H4"
										/>
									</svg>
									<span v-else class="text-sm text-gray-500 mt-2"
										>Uploading...</span
									>
								</label>

								<div
									v-else
									class="relative w-full h-full rounded-2xl border border-gray-200 overflow-hidden shadow-sm"
								>
									<img
										:src="bannerBgUrl"
										alt="Banner Background"
										class="w-full h-full object-cover"
									/>
									<button
										@click="bannerBgUrl = ''"
										class="absolute top-2 right-2 bg-red-500 text-white rounded-full w-7 h-7 flex items-center justify-center hover:bg-red-600"
									>
										✕
									</button>
								</div>
							</div>
						</div>
					</div>

					<!-- BANNER MULTIPLE SECTION (Tetap Ada) -->
					<div class="mt-8 border-t border-gray-200 pt-6">
						<h2 class="text-sm font-semibold mb-2">Banner (Bisa lebih dari 1)</h2>

						<div class="mt-2 flex flex-wrap gap-4">
							<div
								v-for="(url, index) in bannerUrls"
								:key="index"
								class="relative w-40 h-24 rounded-xl border border-gray-200 overflow-hidden shadow-sm"
							>
								<img :src="url" alt="Banner" class="w-full h-full object-cover" />
								<button
									@click="bannerUrls.splice(index, 1)"
									class="absolute top-1 right-1 bg-red-500 text-white rounded-full w-6 h-6 flex items-center justify-center text-xs hover:bg-red-600"
								>
									✕
								</button>
							</div>

							<label
								class="w-40 h-24 border-2 border-dashed border-gray-400 rounded-xl flex flex-col items-center justify-center cursor-pointer hover:bg-gray-50 hover:border-gray-500 transition-all duration-200"
							>
								<input
									type="file"
									multiple
									class="hidden"
									@change="handleBannerUpload"
									accept="image/*"
									:disabled="isUploadingBanner"
								/>
								<svg
									v-if="!isUploadingBanner"
									xmlns="http://www.w3.org/2000/svg"
									class="w-6 h-6 text-gray-400"
									fill="none"
									viewBox="0 0 24 24"
									stroke="currentColor"
									stroke-width="2"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										d="M12 4v16m8-8H4"
									/>
								</svg>
								<span v-else class="text-xs text-gray-500 mt-2">Uploading...</span>
							</label>
						</div>
					</div>
				</div>
			</div>

			<div class="bizpage-website-content__right">
				<div class="bizpage-form-group" style="margin-bottom: 1rem">
					<h1 class="bizpage-form-title">Info Toko</h1>
					<label class="bizpage-form-toggle">
						<input class="bizpage-form-toggle_input" type="checkbox" />
						<span class="bizpage-form-toggle_slider"></span>
						<span class="bizpage-form-toggle_label">Toko Buka</span>
					</label>
				</div>
				<div class="bizpage-form-group">
					<h1 class="bizpage-form-title">Qr Code Bisnis</h1>
					<div class="bizpage-form-qrcode">
						<div
							class="bizpage-form-qrcode_show"
							ref="qrCodeWrapper"
							style="
								width: 250px;
								height: 250px;
								overflow: hidden;
								display: flex;
								justify-content: center;
								align-items: center;
							"
						></div>
					</div>

					<div class="bizpage-form-qrcode_actions">
						<a :href="qrLinkData" target="_blank" class="bizpage-preview-button">
							Preview
						</a>
						<button
							@click="downloadQrCode"
							type="button"
							class="bizpage-download-button"
						>
							Download QR
						</button>
					</div>
				</div>
			</div>
		</div>
	</MainLayout>
</template>

<script setup>
import MainLayout from "@/components/main-layout.vue";
import { session } from "@/auth/session.js";
import { reactive, ref, watch, onMounted } from "vue";
import { TextEditor } from "frappe-ui";
import QRCodeStyling from "qr-code-styling";

const currentUser = session.currentUser;
const textEditorRef = ref(null);

const form = reactive({
	phone: "",
	description: "",
});

function focusEditor(e) {
	if (e.target.closest(".frappe-editor-menu") || e.target.closest("button")) return;
	textEditorRef.value?.editor?.commands?.focus();
}

const qrLinkData = ref("https://www.youtube.com/watch?v=HquFbKYvWtI");
const qrCodeWrapper = ref(null);

const qrCode = new QRCodeStyling({
	width: 1000,
	height: 1000,
	type: "canvas",
	data: qrLinkData.value,
	image: "https://upload.wikimedia.org/wikipedia/commons/9/95/Vue.js_Logo_2.svg",
	dotsOptions: {
		color: "#000000",
		type: "rounded",
	},
	cornersSquareOptions: {
		type: "extra-rounded",
	},
	imageOptions: {
		crossOrigin: "anonymous",
		margin: 15,
		hideBackgroundDots: true,
		imageSize: 0.4,
	},
});

onMounted(() => {
	if (qrCodeWrapper.value) {
		qrCode.append(qrCodeWrapper.value);

		const canvas = qrCodeWrapper.value.querySelector("canvas");
		if (canvas) {
			canvas.style.width = "100%";
			canvas.style.height = "100%";
		}
	}
});

watch(qrLinkData, (newLink) => {
	qrCode.update({
		data: newLink,
	});
});

const downloadQrCode = () => {
	qrCode.download({
		name: "QR-Code-Bizpage",
		extension: "png",
	});
};

const isUploadingLogo = ref(false);
const logoUrl = ref("");

const isUploadingBanner = ref(false);
const bannerUrls = ref([]);

const uploadToBackend = async (file) => {
	const formData = new FormData();
	formData.append("file", file, file.name);
	formData.append("is_private", 0);

	const response = await fetch("/api/method/upload_file", {
		method: "POST",
		headers: {
			Accept: "application/json",
		},
		body: formData,
	});

	if (!response.ok) {
		throw new Error("Gagal mengunggah file");
	}

	return await response.json();
};

const handleLogoUpload = async (event) => {
	const file = event.target.files[0];
	if (!file) return;

	isUploadingLogo.value = true;

	try {
		const result = await uploadToBackend(file);
		if (result.message && result.message.file_url) {
			logoUrl.value = result.message.file_url;
		}
	} catch (error) {
		console.error("Error upload logo:", error);
	} finally {
		isUploadingLogo.value = false;
		event.target.value = "";
	}
};

const handleBannerUpload = async (event) => {
	const files = event.target.files;
	if (!files.length) return;

	isUploadingBanner.value = true;

	try {
		for (const file of files) {
			const result = await uploadToBackend(file);
			if (result.message && result.message.file_url) {
				bannerUrls.value.push(result.message.file_url);
			}
		}
	} catch (error) {
		console.error("Error upload banner:", error);
	} finally {
		isUploadingBanner.value = false;
		event.target.value = "";
	}
};
</script>
