<template>
	<div class="login-page">
		<!-- ===== Sisi kiri: branding dominan (65%) ===== -->
		<div class="login-brand">
			<!-- Grid Latar Belakang Tetap Dipertahankan -->
			<div class="brand-graphic-wrapper">
				<svg
					class="brand-svg"
					xmlns="http://www.w3.org/2000/svg"
					viewBox="0 0 800 600"
					fill="none"
				>
					<defs>
						<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
							<path
								d="M 40 0 L 0 0 0 40"
								fill="none"
								stroke="var(--color-accent-hover)"
								stroke-width="1.2"
								opacity="0.5"
							/>
						</pattern>
					</defs>
					<rect width="100%" height="100%" fill="url(#grid)" />

					<!-- Ornamen dekoratif samping dan bawah -->
					<path
						d="M-100,500 C200,450 300,580 500,480 C700,380 750,530 900,430"
						stroke="var(--color-primary)"
						stroke-width="3"
						stroke-linecap="round"
						opacity="0.4"
					/>
					<path
						d="M-100,530 C150,490 280,620 480,510 C680,400 720,570 900,470"
						stroke="var(--color-primary-hover)"
						stroke-width="1.5"
						stroke-dasharray="6 6"
						opacity="0.3"
					/>
					<rect
						x="680"
						y="80"
						width="80"
						height="80"
						rx="20"
						transform="rotate(15 680 80)"
						fill="var(--color-accent-hover)"
						opacity="0.6"
					/>
				</svg>
			</div>

			<!-- Konten Teks Branding -->
			<div class="brand-content">
				<div class="logo-container">
					<img
						class="login-logo"
						src="https://tailwindcss.com/plus-assets/img/logos/mark.svg?color=indigo&shade=500"
						alt="Your Company"
					/>
					<span class="logo-text">CompanySpace</span>
				</div>

				<!-- Tipografi Kombinasi Dua Warna & Besar-Kecil Huruf Normal -->
				<h1 class="login-brand-title">
					Kelola Semua Pekerjaan,<br />
					<span class="highlight-text">Dalam Satu Dasbor Terintegrasi.</span>
				</h1>

				<p class="login-brand-subtitle">
					Selamat datang kembali di platform kolaborasi digital kami. Optimalkan
					produktivitas tim Anda, pantau metrik performa secara real-time, dan kelola
					proses bisnis Anda dengan lebih efisien, aman, dan terukur dari mana saja.
				</p>

				<!-- CTA Info Box Ringkas -->
				<a href="#pelajari" class="brand-cta-box">
					<span class="cta-badge">BARU</span>
					<span class="cta-text"
						>Pelajari fitur otomasi alur kerja versi 2.0 &rarr;</span
					>
				</a>
			</div>
		</div>

		<!-- ===== Sisi kanan: form ringkas & pas (35%) ===== -->
		<div class="login-form-side">
			<div class="login-card">
				<div class="form-header">
					<h2 class="login-title">Sign in to your account</h2>
					<p class="form-subtitle">Masukkan kredensial Anda untuk mengakses dasbor.</p>
				</div>

				<div class="field">
					<label class="field-label" for="username">Username</label>
					<input
						id="username"
						class="field-input"
						v-model="username"
						placeholder="Username Anda"
					/>
				</div>

				<div class="field">
					<label class="field-label" for="password">Password</label>
					<input
						id="password"
						type="password"
						class="field-input"
						v-model="password"
						placeholder="••••••••"
						@keyup.enter="submit"
					/>
				</div>

				<ErrorMessage :message="session.login.error" />

				<button
					class="btn-primary"
					:class="{ 'is-loading': session.login.loading }"
					:disabled="session.login.loading"
					@click="submit"
				>
					{{ session.login.loading ? "Memproses..." : "Masuk ke Akun" }}
				</button>

				<p class="footer-text">
					Belum punya akun?
					<router-link to="/register" class="footer-link">Daftar Sekarang</router-link>
				</p>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref } from "vue";
import { ErrorMessage } from "frappe-ui";
import { session } from "../../auth/session.js";

const username = ref("");
const password = ref("");

function submit() {
	if (session?.login?.submit) {
		session.login.submit({
			userName: username.value,
			password: password.value,
		});
	}
}
</script>

<style scoped>
.login-page {
	display: flex;
	min-height: 100vh;
	width: 100%;
	overflow: hidden;
}

/* ===== Sisi kiri: branding dominan (65%) ===== */
.login-brand {
	display: flex;
	flex: 65 1 0%;
	flex-direction: column;
	align-items: flex-start;
	justify-content: center;
	padding: 4rem 5rem;
	position: relative;
	background: linear-gradient(145deg, var(--color-accent-light) 0%, var(--color-accent) 100%);
}

.brand-graphic-wrapper {
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	z-index: 1;
	pointer-events: none;
}

.brand-svg {
	width: 100%;
	height: 100%;
	object-fit: cover;
}

.brand-content {
	position: relative;
	z-index: 10;
	display: flex;
	flex-direction: column;
	align-items: flex-start;
	gap: 1.5rem;
	max-width: 40rem;
}

.logo-container {
	display: flex;
	align-items: center;
	gap: 0.75rem;
	margin-bottom: 0.5rem;
}

.login-logo {
	height: 2.25rem;
	width: auto;
}

.logo-text {
	font-family: var(--font-display);
	font-size: 1.125rem;
	font-weight: 700;
	color: var(--color-primary-active);
	letter-spacing: -0.01em;
}

.login-brand-title {
	font-family: var(--font-display);
	font-size: 3.25rem; /* Ukuran teks besar sesuai referensi */
	font-weight: 800;
	line-height: 1.15;
	letter-spacing: -0.02em;
	color: var(--color-primary-active); /* Warna gelap utama */
	text-transform: none; /* Menonaktifkan uppercase agar mengikuti tulisan kode */
}

/* Pewarnaan Aksen Hijau untuk frasa kunci sesuai gambar */
.highlight-text {
	color: var(--color-accent-active);
}

.login-brand-subtitle {
	font-size: 1.05rem;
	line-height: 1.7;
	color: var(--color-gray-700);
	opacity: 0.9;
	max-width: 36rem;
}

/* CTA Box Link Style */
.brand-cta-box {
	display: inline-flex;
	align-items: center;
	gap: 0.75rem;
	background: rgba(255, 255, 255, 0.6);
	padding: 0.5rem 1rem;
	border-radius: var(--radius-full);
	border: 1px solid rgba(255, 255, 255, 0.8);
	text-decoration: none;
	transition: all 0.2s ease;
	margin-top: 0.5rem;
}

.brand-cta-box:hover {
	background: rgba(255, 255, 255, 0.9);
	transform: translateY(-1px);
}

.cta-badge {
	font-size: 0.6875rem;
	font-weight: 700;
	background-color: var(--color-primary);
	color: var(--color-white);
	padding: 0.125rem 0.5rem;
	border-radius: var(--radius-full);
}

.cta-text {
	font-size: 0.8125rem;
	font-weight: 600;
	color: var(--color-primary-active);
}

/* ===== Sisi kanan: form ringkas (35%) ===== --> */
.login-form-side {
	display: flex;
	flex: 35 1 0%;
	align-items: center;
	justify-content: center;
	padding: 3rem 2.5rem;
	background-color: var(--color-white);
	box-shadow: -4px 0 24px rgba(0, 0, 0, 0.02);
	z-index: 20;
}

.login-card {
	display: flex;
	flex-direction: column;
	gap: 1.25rem;
	width: 100%;
	max-width: 22rem;
}

.form-header {
	margin-bottom: 0.5rem;
}

.login-title {
	font-family: var(--font-display);
	font-size: 1.375rem;
	font-weight: 700;
	letter-spacing: -0.01em;
	color: var(--color-gray-900);
	margin-bottom: 0.25rem;
}

.form-subtitle {
	font-size: 0.8125rem;
	color: var(--color-gray-500);
}

.field {
	display: flex;
	flex-direction: column;
	gap: 0.375rem;
}

.field-label {
	font-size: 0.8125rem;
	font-weight: 500;
	color: var(--color-gray-700);
}

.field-input {
	width: 100%;
	padding: 0.5rem 0.75rem;
	border: 1px solid var(--color-gray-300);
	border-radius: var(--radius-md);
	font-size: 0.875rem;
	color: var(--color-gray-900);
	outline: none;
	transition:
		border-color 0.15s ease,
		box-shadow 0.15s ease;
}

.field-input:focus {
	border-color: var(--color-primary);
	box-shadow: 0 0 0 3px var(--color-focus-ring);
}

.btn-primary {
	display: flex;
	width: 100%;
	justify-content: center;
	align-items: center;
	border: none;
	border-radius: var(--radius-md);
	padding: 0.625rem 0.75rem;
	font-size: 0.875rem;
	font-weight: 600;
	color: var(--color-white);
	background-color: var(--color-primary);
	cursor: pointer;
	transition: background-color 0.15s ease;
	margin-top: 0.25rem;
}

.btn-primary:hover:not(:disabled) {
	background-color: var(--color-primary-hover);
}

.footer-text {
	text-align: center;
	font-size: 0.8125rem;
	color: var(--color-gray-500);
	margin-top: 0.25rem;
}

.footer-link {
	font-weight: 600;
	color: var(--color-primary);
	text-decoration: none;
}

/* ===== Responsive ===== */
@media (max-width: 1024px) {
	.login-brand {
		padding: 3rem;
	}
	.login-brand-title {
		font-size: 2.5rem;
	}
}

@media (max-width: 768px) {
	.login-page {
		flex-direction: column;
		overflow-y: auto;
	}

	.login-brand {
		flex: 0 0 auto;
		padding: 3.5rem 2rem;
	}

	.login-form-side {
		flex: 1 1 auto;
		padding: 3rem 1.5rem;
	}
}
</style>
