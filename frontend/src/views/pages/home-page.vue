<template>
	<div class="min-h-screen bg-white text-slate-900 antialiased">
		<header
			class="sticky top-0 z-50 border-b border-slate-200/80 bg-white/95 backdrop-blur-sm"
		>
			<div
				class="mx-auto flex max-w-7xl items-center justify-between px-4 py-4 sm:px-6 lg:px-8"
			>
				<router-link to="/" class="flex items-center gap-2.5">
					<span
						class="flex h-9 w-9 items-center justify-center rounded-xl bg-[var(--color-primary)] text-sm font-bold text-white shadow-md"
						>B</span
					>
					<span class="text-lg font-bold tracking-tight text-slate-900">BizPage</span>
				</router-link>

				<nav class="hidden items-center gap-8 md:flex">
					<a
						v-for="link in navLinks"
						:key="link.href"
						:href="link.href"
						class="text-sm font-medium text-slate-600 transition duration-300 hover:text-[var(--color-primary)]"
					>
						{{ link.label }}
					</a>
				</nav>

				<div class="hidden items-center gap-3 md:flex">
					<router-link
						to="/login"
						class="rounded-lg px-4 py-2 text-sm font-semibold text-slate-700 transition duration-300 hover:bg-slate-100"
					>
						Login
					</router-link>
					<router-link
						to="/register"
						class="rounded-lg bg-[var(--color-primary)] px-5 py-2.5 text-sm font-semibold text-white shadow-sm transition duration-300 hover:bg-[var(--color-primary-hover)]"
					>
						Buat Website
					</router-link>
				</div>

				<button
					type="button"
					class="flex h-10 w-10 items-center justify-center rounded-lg text-slate-700 transition duration-300 hover:bg-slate-100 md:hidden"
					aria-label="Buka menu"
					@click="mobileMenuOpen = !mobileMenuOpen"
				>
					<svg v-if="!mobileMenuOpen" viewBox="0 0 24 24" fill="none" class="h-6 w-6">
						<path
							d="M4 7h16M4 12h16M4 17h16"
							stroke="currentColor"
							stroke-width="1.8"
							stroke-linecap="round"
						/>
					</svg>
					<svg v-else viewBox="0 0 24 24" fill="none" class="h-6 w-6">
						<path
							d="M6 6l12 12M18 6L6 18"
							stroke="currentColor"
							stroke-width="1.8"
							stroke-linecap="round"
						/>
					</svg>
				</button>
			</div>

			<div
				v-if="mobileMenuOpen"
				class="border-t border-slate-200 bg-white px-4 py-4 md:hidden"
			>
				<nav class="flex flex-col gap-1">
					<a
						v-for="link in navLinks"
						:key="link.href"
						:href="link.href"
						class="rounded-lg px-3 py-2.5 text-sm font-medium text-slate-700 transition duration-300 hover:bg-slate-100"
						@click="mobileMenuOpen = false"
					>
						{{ link.label }}
					</a>
					<div class="mt-3 flex flex-col gap-2 border-t border-slate-200 pt-3">
						<router-link
							to="/login"
							class="rounded-lg border border-slate-200 px-4 py-2.5 text-center text-sm font-semibold text-slate-700 transition duration-300 hover:bg-slate-50"
						>
							Login
						</router-link>
						<router-link
							to="/register"
							class="rounded-lg bg-[var(--color-primary)] px-4 py-2.5 text-center text-sm font-semibold text-white transition duration-300 hover:bg-[var(--color-primary-hover)]"
						>
							Buat Website
						</router-link>
					</div>
				</nav>
			</div>
		</header>

		<section
			class="relative overflow-hidden bg-gradient-to-b from-[var(--color-accent-light)] via-white to-white"
		>
			<div
				class="pointer-events-none absolute -right-24 -top-24 h-96 w-96 rounded-full bg-[radial-gradient(circle,_rgba(45,62,112,0.18)_0%,_transparent_70%)]"
			></div>
			<div
				class="pointer-events-none absolute -left-32 top-40 h-80 w-80 rounded-full bg-[radial-gradient(circle,_rgba(193,255,114,0.35)_0%,_transparent_70%)]"
			></div>

			<div
				class="relative mx-auto grid max-w-7xl gap-14 px-4 py-20 sm:px-6 lg:grid-cols-2 lg:items-center lg:py-28 lg:px-8"
			>
				<div>
					<span
						class="inline-flex items-center gap-2 rounded-full border border-slate-200 bg-white/90 px-4 py-1.5 text-xs font-semibold text-slate-700 shadow-sm"
					>
						<span
							class="h-1.5 w-1.5 rounded-full bg-[var(--color-accent-active)]"
						></span>
						Platform No-Code untuk UMKM & Bisnis Kreatif
					</span>

					<h1
						class="mt-6 text-4xl font-extrabold leading-[1.1] tracking-tight text-slate-900 sm:text-5xl lg:text-[3.25rem]"
					>
						Website Bisnis Profesional,
						<span class="text-[var(--color-accent-active)]"
							>Tanpa Coding Sama Sekali.</span
						>
					</h1>

					<p class="mt-6 max-w-xl text-lg leading-relaxed text-slate-600">
						Buat website, katalog produk, dan portfolio dalam hitungan menit. Terima
						pesanan langsung lewat WhatsApp, bagikan lewat QR Code, dan pantau performa
						bisnis dengan analytics real-time.
					</p>

					<div class="mt-8 flex flex-col gap-3 sm:flex-row">
						<router-link
							to="/register"
							class="inline-flex items-center justify-center rounded-xl bg-[var(--color-primary)] px-7 py-3.5 text-sm font-semibold text-white shadow-lg transition duration-300 hover:bg-[var(--color-primary-hover)] hover:-translate-y-0.5"
						>
							Buat Website Gratis
						</router-link>
						<a
							href="#preview"
							class="inline-flex items-center justify-center rounded-xl border border-slate-300 bg-white px-7 py-3.5 text-sm font-semibold text-slate-800 transition duration-300 hover:border-slate-400 hover:bg-slate-50"
						>
							Lihat Contoh Website
						</a>
					</div>

					<div class="mt-9 flex items-center gap-3">
						<div class="flex -space-x-2">
							<span
								class="h-8 w-8 rounded-full border-2 border-white bg-[var(--color-primary)]"
							></span>
							<span
								class="h-8 w-8 rounded-full border-2 border-white bg-[var(--color-primary-hover)]"
							></span>
							<span
								class="h-8 w-8 rounded-full border-2 border-white bg-[var(--color-primary-active)]"
							></span>
							<span
								class="h-8 w-8 rounded-full border-2 border-white bg-slate-400"
							></span>
						</div>
						<p class="text-sm text-slate-500">
							Dipercaya
							<span class="font-semibold text-slate-900">10.000+ pelaku UMKM</span>
							di seluruh Indonesia
						</p>
					</div>
				</div>

				<div class="relative">
					<div class="rounded-2xl border border-slate-200 bg-white p-3 shadow-2xl">
						<div class="flex items-center gap-1.5 border-b border-slate-100 px-2 pb-3">
							<span class="h-2.5 w-2.5 rounded-full bg-slate-300"></span>
							<span class="h-2.5 w-2.5 rounded-full bg-slate-300"></span>
							<span class="h-2.5 w-2.5 rounded-full bg-slate-300"></span>
							<span
								class="ml-3 flex-1 truncate rounded-md bg-slate-100 px-3 py-1 text-xs text-slate-400"
								>bizpage.id/tokobungaayu</span
							>
						</div>

						<div class="mt-3 rounded-xl bg-[var(--color-primary)] p-6">
							<p class="text-xs font-semibold uppercase tracking-wide text-white/70">
								Toko Bunga Ayu
							</p>
							<p class="mt-1 text-xl font-bold text-white">
								Rangkaian Bunga Segar Setiap Hari
							</p>
							<span
								class="mt-4 inline-block rounded-lg bg-[var(--color-accent)] px-4 py-2 text-xs font-semibold text-[var(--color-primary)]"
								>Pesan via WhatsApp</span
							>
						</div>

						<div class="mt-3 grid grid-cols-3 gap-2">
							<div class="rounded-lg border border-slate-100 bg-slate-50 p-2">
								<div class="h-14 rounded-md bg-[var(--color-primary-light)]"></div>
								<p class="mt-2 text-[11px] font-semibold text-slate-700">
									Buket Rose
								</p>
								<p class="text-[11px] text-slate-400">Rp185.000</p>
							</div>
							<div class="rounded-lg border border-slate-100 bg-slate-50 p-2">
								<div class="h-14 rounded-md bg-[var(--color-accent-light)]"></div>
								<p class="mt-2 text-[11px] font-semibold text-slate-700">
									Buket Sunflower
								</p>
								<p class="text-[11px] text-slate-400">Rp165.000</p>
							</div>
							<div class="rounded-lg border border-slate-100 bg-slate-50 p-2">
								<div class="h-14 rounded-md bg-slate-100"></div>
								<p class="mt-2 text-[11px] font-semibold text-slate-700">
									Buket Lavender
								</p>
								<p class="text-[11px] text-slate-400">Rp210.000</p>
							</div>
						</div>
					</div>

					<div
						class="absolute -bottom-6 -left-6 flex items-center gap-2 rounded-xl border border-slate-200 bg-white px-4 py-3 shadow-xl"
					>
						<span
							class="flex h-9 w-9 items-center justify-center rounded-lg bg-[var(--color-accent-light)] text-[var(--color-primary)]"
						>
							<svg viewBox="0 0 24 24" fill="none" class="h-4 w-4">
								<path
									d="M5 13l4 4L19 7"
									stroke="currentColor"
									stroke-width="2"
									stroke-linecap="round"
									stroke-linejoin="round"
								/>
							</svg>
						</span>
						<div>
							<p class="text-xs font-semibold text-slate-900">Pesanan Baru Masuk</p>
							<p class="text-[11px] text-slate-500">via WhatsApp Order</p>
						</div>
					</div>
				</div>
			</div>
		</section>

		<section class="border-y border-slate-100 bg-slate-50">
			<div
				class="mx-auto grid max-w-7xl grid-cols-2 gap-8 px-4 py-12 sm:px-6 lg:grid-cols-4 lg:px-8"
			>
				<div v-for="stat in stats" :key="stat.label" class="text-center">
					<p class="text-3xl font-extrabold tracking-tight text-slate-900 sm:text-4xl">
						{{ stat.value }}
					</p>
					<p class="mt-1 text-sm text-slate-500">{{ stat.label }}</p>
				</div>
			</div>
		</section>

		<section class="mx-auto max-w-7xl px-4 py-20 sm:px-6 lg:px-8">
			<div class="mx-auto max-w-2xl text-center">
				<h2 class="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl">
					Masih Jualan Cuma Lewat DM & Story?
				</h2>
				<p class="mt-4 text-lg text-slate-600">
					Cara jualan yang lama bikin bisnis kamu sulit berkembang dan kalah saing dari
					kompetitor yang sudah lebih rapi.
				</p>
			</div>

			<div class="mt-12 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
				<div
					class="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm transition duration-300 hover:shadow-lg"
				>
					<span
						class="flex h-11 w-11 items-center justify-center rounded-xl bg-[var(--color-primary-light)] text-[var(--color-primary)]"
					>
						<svg viewBox="0 0 24 24" fill="none" class="h-5 w-5">
							<path
								d="M4 19V5a1 1 0 0 1 1-1h14a1 1 0 0 1 1 1v10a1 1 0 0 1-1 1H9l-5 4Z"
								stroke="currentColor"
								stroke-width="1.7"
								stroke-linejoin="round"
							/>
						</svg>
					</span>
					<h3 class="mt-4 text-base font-semibold text-slate-900">
						Chat WA Numpuk & Kelewat
					</h3>
					<p class="mt-2 text-sm leading-relaxed text-slate-500">
						Pesanan campur aduk dengan chat pribadi, banyak yang terlewat dan customer
						kabur.
					</p>
				</div>
				<div
					class="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm transition duration-300 hover:shadow-lg"
				>
					<span
						class="flex h-11 w-11 items-center justify-center rounded-xl bg-[var(--color-primary-light)] text-[var(--color-primary)]"
					>
						<svg viewBox="0 0 24 24" fill="none" class="h-5 w-5">
							<rect
								x="3.5"
								y="3.5"
								width="17"
								height="17"
								rx="2"
								stroke="currentColor"
								stroke-width="1.7"
							/>
							<circle
								cx="9"
								cy="9.5"
								r="1.6"
								stroke="currentColor"
								stroke-width="1.7"
							/>
							<path
								d="M4.5 17l5-5 4 3 5.5-5.5"
								stroke="currentColor"
								stroke-width="1.7"
								stroke-linecap="round"
								stroke-linejoin="round"
							/>
						</svg>
					</span>
					<h3 class="mt-4 text-base font-semibold text-slate-900">
						Feed IG Bukan Etalase Jualan
					</h3>
					<p class="mt-2 text-sm leading-relaxed text-slate-500">
						Produk lama tenggelam, susah dicari, dan bergantung penuh pada algoritma.
					</p>
				</div>
				<div
					class="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm transition duration-300 hover:shadow-lg"
				>
					<span
						class="flex h-11 w-11 items-center justify-center rounded-xl bg-[var(--color-primary-light)] text-[var(--color-primary)]"
					>
						<svg viewBox="0 0 24 24" fill="none" class="h-5 w-5">
							<path
								d="M8 8l-4 4 4 4M16 8l4 4-4 4M13.5 5.5l-3 13"
								stroke="currentColor"
								stroke-width="1.7"
								stroke-linecap="round"
								stroke-linejoin="round"
							/>
						</svg>
					</span>
					<h3 class="mt-4 text-base font-semibold text-slate-900">
						Bikin Website Sendiri Ribet
					</h3>
					<p class="mt-2 text-sm leading-relaxed text-slate-500">
						Butuh developer, biaya besar, dan waktu berminggu-minggu hanya untuk tampil
						online.
					</p>
				</div>
				<div
					class="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm transition duration-300 hover:shadow-lg"
				>
					<span
						class="flex h-11 w-11 items-center justify-center rounded-xl bg-[var(--color-primary-light)] text-[var(--color-primary)]"
					>
						<svg viewBox="0 0 24 24" fill="none" class="h-5 w-5">
							<path
								d="M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6l7-3Z"
								stroke="currentColor"
								stroke-width="1.7"
								stroke-linejoin="round"
							/>
							<path
								d="M9 12l2 2 4-4"
								stroke="currentColor"
								stroke-width="1.7"
								stroke-linecap="round"
								stroke-linejoin="round"
							/>
						</svg>
					</span>
					<h3 class="mt-4 text-base font-semibold text-slate-900">
						Sulit Dipercaya Calon Customer
					</h3>
					<p class="mt-2 text-sm leading-relaxed text-slate-500">
						Tanpa website resmi, bisnis kamu terlihat kurang meyakinkan dibanding
						kompetitor.
					</p>
				</div>
			</div>
		</section>

		<section id="fitur" class="bg-slate-50 py-20">
			<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
				<div class="mx-auto max-w-2xl text-center">
					<h2 class="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl">
						Satu Platform, Semua Kebutuhan Bisnis Kamu
					</h2>
					<p class="mt-4 text-lg text-slate-600">
						Dari tampil profesional sampai menerima pesanan, semua sudah tersedia tanpa
						perlu tools tambahan.
					</p>
				</div>

				<div class="mt-12 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
					<div
						class="group rounded-2xl border border-slate-200 bg-white p-7 shadow-sm transition duration-300 hover:-translate-y-1 hover:shadow-xl"
					>
						<div
							class="flex h-12 w-12 items-center justify-center rounded-xl bg-[var(--color-primary)] text-white shadow-md"
						>
							<svg viewBox="0 0 24 24" fill="none" class="h-6 w-6">
								<circle
									cx="12"
									cy="12"
									r="9"
									stroke="currentColor"
									stroke-width="1.7"
								/>
								<path
									d="M3 12h18M12 3c2.5 2.6 3.8 5.8 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.8-3.8-9s1.3-6.4 3.8-9Z"
									stroke="currentColor"
									stroke-width="1.7"
								/>
							</svg>
						</div>
						<h3 class="mt-5 text-lg font-semibold text-slate-900">Website Bisnis</h3>
						<p class="mt-2 text-sm leading-relaxed text-slate-500">
							Tampil profesional dengan website custom yang mencerminkan brand kamu,
							tanpa sentuh kode sama sekali.
						</p>
					</div>

					<div
						class="group rounded-2xl border border-slate-200 bg-white p-7 shadow-sm transition duration-300 hover:-translate-y-1 hover:shadow-xl"
					>
						<div
							class="flex h-12 w-12 items-center justify-center rounded-xl bg-[var(--color-primary)] text-white shadow-md"
						>
							<svg viewBox="0 0 24 24" fill="none" class="h-6 w-6">
								<rect
									x="3.5"
									y="3.5"
									width="7"
									height="7"
									rx="1.5"
									stroke="currentColor"
									stroke-width="1.7"
								/>
								<rect
									x="13.5"
									y="3.5"
									width="7"
									height="7"
									rx="1.5"
									stroke="currentColor"
									stroke-width="1.7"
								/>
								<rect
									x="3.5"
									y="13.5"
									width="7"
									height="7"
									rx="1.5"
									stroke="currentColor"
									stroke-width="1.7"
								/>
								<rect
									x="13.5"
									y="13.5"
									width="7"
									height="7"
									rx="1.5"
									stroke="currentColor"
									stroke-width="1.7"
								/>
							</svg>
						</div>
						<h3 class="mt-5 text-lg font-semibold text-slate-900">Katalog Produk</h3>
						<p class="mt-2 text-sm leading-relaxed text-slate-500">
							Pajang seluruh produk lengkap dengan foto, harga, dan varian dalam
							katalog yang rapi dan mudah dicari.
						</p>
					</div>

					<div
						class="group rounded-2xl border border-slate-200 bg-white p-7 shadow-sm transition duration-300 hover:-translate-y-1 hover:shadow-xl"
					>
						<div
							class="flex h-12 w-12 items-center justify-center rounded-xl bg-[var(--color-primary)] text-white shadow-md"
						>
							<svg viewBox="0 0 24 24" fill="none" class="h-6 w-6">
								<rect
									x="3"
									y="4"
									width="18"
									height="14"
									rx="2"
									stroke="currentColor"
									stroke-width="1.7"
								/>
								<path
									d="M3 15l5-4 4 3 4-5 5 6"
									stroke="currentColor"
									stroke-width="1.7"
									stroke-linecap="round"
									stroke-linejoin="round"
								/>
							</svg>
						</div>
						<h3 class="mt-5 text-lg font-semibold text-slate-900">Portfolio</h3>
						<p class="mt-2 text-sm leading-relaxed text-slate-500">
							Tunjukkan hasil karya terbaik untuk meyakinkan calon klien sebelum
							mereka order.
						</p>
					</div>

					<div
						class="group rounded-2xl border border-slate-200 bg-white p-7 shadow-sm transition duration-300 hover:-translate-y-1 hover:shadow-xl"
					>
						<div
							class="flex h-12 w-12 items-center justify-center rounded-xl bg-[var(--color-primary)] text-white shadow-md"
						>
							<svg viewBox="0 0 24 24" fill="none" class="h-6 w-6">
								<path
									d="M20.5 11.5a8 8 0 1 1-3.2-6.4M20.5 4v5h-5"
									stroke="currentColor"
									stroke-width="1.7"
									stroke-linecap="round"
									stroke-linejoin="round"
								/>
							</svg>
						</div>
						<h3 class="mt-5 text-lg font-semibold text-slate-900">WhatsApp Order</h3>
						<p class="mt-2 text-sm leading-relaxed text-slate-500">
							Customer checkout langsung ke WhatsApp kamu, lengkap dengan detail
							pesanan otomatis.
						</p>
					</div>

					<div
						class="group rounded-2xl border border-slate-200 bg-white p-7 shadow-sm transition duration-300 hover:-translate-y-1 hover:shadow-xl"
					>
						<div
							class="flex h-12 w-12 items-center justify-center rounded-xl bg-[var(--color-primary)] text-white shadow-md"
						>
							<svg viewBox="0 0 24 24" fill="none" class="h-6 w-6">
								<rect
									x="3.5"
									y="3.5"
									width="6"
									height="6"
									stroke="currentColor"
									stroke-width="1.7"
								/>
								<rect
									x="14.5"
									y="3.5"
									width="6"
									height="6"
									stroke="currentColor"
									stroke-width="1.7"
								/>
								<rect
									x="3.5"
									y="14.5"
									width="6"
									height="6"
									stroke="currentColor"
									stroke-width="1.7"
								/>
								<path
									d="M14.5 14.5h3v3h-3zM20.5 14.5v3M17.5 20.5h3"
									stroke="currentColor"
									stroke-width="1.7"
								/>
							</svg>
						</div>
						<h3 class="mt-5 text-lg font-semibold text-slate-900">QR Code</h3>
						<p class="mt-2 text-sm leading-relaxed text-slate-500">
							Sebar QR Code di kemasan, banner, atau kartu nama biar customer
							langsung mampir ke website.
						</p>
					</div>

					<div
						class="group rounded-2xl border border-slate-200 bg-white p-7 shadow-sm transition duration-300 hover:-translate-y-1 hover:shadow-xl"
					>
						<div
							class="flex h-12 w-12 items-center justify-center rounded-xl bg-[var(--color-primary)] text-white shadow-md"
						>
							<svg viewBox="0 0 24 24" fill="none" class="h-6 w-6">
								<path
									d="M4 20V10M11 20V4M18 20v-7"
									stroke="currentColor"
									stroke-width="1.7"
									stroke-linecap="round"
								/>
							</svg>
						</div>
						<h3 class="mt-5 text-lg font-semibold text-slate-900">Analytics</h3>
						<p class="mt-2 text-sm leading-relaxed text-slate-500">
							Pantau pengunjung, produk terlaris, dan performa website secara
							real-time.
						</p>
					</div>
				</div>
			</div>
		</section>

		<section id="cara-kerja" class="mx-auto max-w-7xl px-4 py-20 sm:px-6 lg:px-8">
			<div class="mx-auto max-w-2xl text-center">
				<h2 class="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl">
					Online dalam 4 Langkah Mudah
				</h2>
				<p class="mt-4 text-lg text-slate-600">
					Nggak perlu tim IT, nggak perlu nunggu berminggu-minggu.
				</p>
			</div>

			<div class="mt-12 grid gap-8 sm:grid-cols-2 lg:grid-cols-4">
				<div class="relative">
					<span
						class="flex h-11 w-11 items-center justify-center rounded-xl bg-[var(--color-primary)] text-sm font-bold text-white"
						>01</span
					>
					<h3 class="mt-4 text-base font-semibold text-slate-900">Daftar Akun Gratis</h3>
					<p class="mt-2 text-sm leading-relaxed text-slate-500">
						Buat akun dalam hitungan detik, tanpa perlu kartu kredit.
					</p>
				</div>
				<div class="relative">
					<span
						class="flex h-11 w-11 items-center justify-center rounded-xl bg-[var(--color-primary)] text-sm font-bold text-white"
						>02</span
					>
					<h3 class="mt-4 text-base font-semibold text-slate-900">
						Pilih Template & Brand
					</h3>
					<p class="mt-2 text-sm leading-relaxed text-slate-500">
						Sesuaikan warna, font, dan logo sesuai identitas bisnis kamu.
					</p>
				</div>
				<div class="relative">
					<span
						class="flex h-11 w-11 items-center justify-center rounded-xl bg-[var(--color-primary)] text-sm font-bold text-white"
						>03</span
					>
					<h3 class="mt-4 text-base font-semibold text-slate-900">
						Tambah Produk & Portfolio
					</h3>
					<p class="mt-2 text-sm leading-relaxed text-slate-500">
						Upload foto produk atau hasil kerja lengkap dengan deskripsi dan harga.
					</p>
				</div>
				<div class="relative">
					<span
						class="flex h-11 w-11 items-center justify-center rounded-xl bg-[var(--color-primary)] text-sm font-bold text-white"
						>04</span
					>
					<h3 class="mt-4 text-base font-semibold text-slate-900">
						Publish & Terima Pesanan
					</h3>
					<p class="mt-2 text-sm leading-relaxed text-slate-500">
						Website live dan siap menerima order lewat WhatsApp hari itu juga.
					</p>
				</div>
			</div>
		</section>

		<section id="preview" class="bg-[var(--color-primary-active)] py-20">
			<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
				<div class="mx-auto max-w-2xl text-center">
					<h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl">
						Lihat Seperti Apa Website Kamu Nanti
					</h2>
					<p class="mt-4 text-lg text-white/60">
						Tampilan modern dan rapi, siap dipakai untuk berbagai jenis bisnis.
					</p>
				</div>

				<div class="mt-12 grid gap-6 lg:grid-cols-3">
					<div
						class="overflow-hidden rounded-2xl border border-white/10 bg-white/5 shadow-2xl transition duration-300 hover:-translate-y-1"
					>
						<div class="h-40 bg-[var(--color-primary)]"></div>
						<div class="p-5">
							<p class="text-sm font-semibold text-white">Homepage</p>
							<p class="mt-1 text-xs text-white/50">
								Kesan pertama yang profesional untuk bisnis kamu.
							</p>
						</div>
					</div>
					<div
						class="overflow-hidden rounded-2xl border border-white/10 bg-white/5 shadow-2xl transition duration-300 hover:-translate-y-1"
					>
						<div class="h-40 bg-[var(--color-accent)]"></div>
						<div class="p-5">
							<p class="text-sm font-semibold text-white">Halaman Produk</p>
							<p class="mt-1 text-xs text-white/50">
								Katalog rapi lengkap dengan tombol pesan WhatsApp.
							</p>
						</div>
					</div>
					<div
						class="overflow-hidden rounded-2xl border border-white/10 bg-white/5 shadow-2xl transition duration-300 hover:-translate-y-1"
					>
						<div class="h-40 bg-slate-600"></div>
						<div class="p-5">
							<p class="text-sm font-semibold text-white">Dashboard</p>
							<p class="mt-1 text-xs text-white/50">
								Kelola produk, pesanan, dan analytics dalam satu tempat.
							</p>
						</div>
					</div>
				</div>
			</div>
		</section>

		<section class="mx-auto max-w-7xl px-4 py-20 sm:px-6 lg:px-8">
			<div class="mx-auto max-w-2xl text-center">
				<h2 class="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl">
					Dibuat untuk Berbagai Jenis Bisnis
				</h2>
				<p class="mt-4 text-lg text-slate-600">
					Apa pun jenis usaha kamu, BizPage siap membantu tampil lebih profesional.
				</p>
			</div>

			<div class="mt-12 grid grid-cols-2 gap-4 sm:grid-cols-3 lg:grid-cols-4">
				<div
					v-for="item in targetMarket"
					:key="item.label"
					class="flex items-center gap-3 rounded-2xl border border-slate-200 bg-white px-4 py-4 shadow-sm transition duration-300 hover:-translate-y-1 hover:border-[var(--color-primary-light)] hover:shadow-lg"
				>
					<span
						class="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg bg-[var(--color-primary-light)] text-xs font-bold text-[var(--color-primary)]"
					>
						{{ item.initial }}
					</span>
					<span class="text-sm font-semibold text-slate-700">{{ item.label }}</span>
				</div>
			</div>
		</section>

		<section class="bg-slate-50 py-20">
			<div class="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8">
				<div class="mx-auto max-w-2xl text-center">
					<h2 class="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl">
						Instagram vs BizPage
					</h2>
					<p class="mt-4 text-lg text-slate-600">
						Instagram bagus untuk promosi, tapi bukan tempat terbaik untuk jualan
						serius.
					</p>
				</div>

				<div
					class="mt-12 overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm"
				>
					<div
						class="grid grid-cols-3 border-b border-slate-200 bg-slate-50 text-sm font-semibold text-slate-700"
					>
						<div class="px-5 py-4">Fitur</div>
						<div class="px-5 py-4 text-center">Instagram</div>
						<div class="px-5 py-4 text-center text-[var(--color-primary)]">
							BizPage
						</div>
					</div>
					<div
						v-for="row in comparisonRows"
						:key="row.label"
						class="grid grid-cols-3 items-center border-b border-slate-100 text-sm last:border-b-0"
					>
						<div class="px-5 py-4 text-slate-700">{{ row.label }}</div>
						<div class="flex justify-center px-5 py-4">
							<svg
								v-if="row.instagram"
								viewBox="0 0 24 24"
								fill="none"
								class="h-4 w-4 text-slate-400"
							>
								<path
									d="M5 13l4 4L19 7"
									stroke="currentColor"
									stroke-width="2"
									stroke-linecap="round"
									stroke-linejoin="round"
								/>
							</svg>
							<svg
								v-else
								viewBox="0 0 24 24"
								fill="none"
								class="h-4 w-4 text-slate-300"
							>
								<path
									d="M6 6l12 12M18 6L6 18"
									stroke="currentColor"
									stroke-width="2"
									stroke-linecap="round"
								/>
							</svg>
						</div>
						<div
							class="flex justify-center bg-[var(--color-primary-light)]/40 px-5 py-4"
						>
							<svg
								v-if="row.bizpage"
								viewBox="0 0 24 24"
								fill="none"
								class="h-4 w-4 text-[var(--color-primary)]"
							>
								<path
									d="M5 13l4 4L19 7"
									stroke="currentColor"
									stroke-width="2.4"
									stroke-linecap="round"
									stroke-linejoin="round"
								/>
							</svg>
							<svg
								v-else
								viewBox="0 0 24 24"
								fill="none"
								class="h-4 w-4 text-slate-300"
							>
								<path
									d="M6 6l12 12M18 6L6 18"
									stroke="currentColor"
									stroke-width="2"
									stroke-linecap="round"
								/>
							</svg>
						</div>
					</div>
				</div>
			</div>
		</section>

		<section id="harga" class="mx-auto max-w-7xl px-4 py-20 sm:px-6 lg:px-8">
			<div class="mx-auto max-w-2xl text-center">
				<h2 class="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl">
					Harga Simpel, Tanpa Kejutan
				</h2>
				<p class="mt-4 text-lg text-slate-600">
					Mulai gratis, upgrade kapan saja kalau bisnis kamu sudah siap naik level.
				</p>
			</div>

			<div class="mx-auto mt-12 grid max-w-4xl gap-8 sm:grid-cols-2">
				<div class="rounded-2xl border border-slate-200 bg-white p-8 shadow-sm">
					<p class="text-sm font-semibold text-slate-500">Free</p>
					<p class="mt-2 text-4xl font-extrabold tracking-tight text-slate-900">Rp0</p>
					<p class="mt-1 text-sm text-slate-500">
						Selamanya, cocok untuk mulai berjualan
					</p>
					<ul class="mt-6 space-y-3 text-sm text-slate-600">
						<li class="flex items-center gap-2">
							<svg
								viewBox="0 0 24 24"
								fill="none"
								class="h-4 w-4 text-[var(--color-primary)]"
							>
								<path
									d="M5 13l4 4L19 7"
									stroke="currentColor"
									stroke-width="2"
									stroke-linecap="round"
									stroke-linejoin="round"
								/>
							</svg>
							1 Website Bisnis
						</li>
						<li class="flex items-center gap-2">
							<svg
								viewBox="0 0 24 24"
								fill="none"
								class="h-4 w-4 text-[var(--color-primary)]"
							>
								<path
									d="M5 13l4 4L19 7"
									stroke="currentColor"
									stroke-width="2"
									stroke-linecap="round"
									stroke-linejoin="round"
								/>
							</svg>
							Katalog hingga 20 produk
						</li>
						<li class="flex items-center gap-2">
							<svg
								viewBox="0 0 24 24"
								fill="none"
								class="h-4 w-4 text-[var(--color-primary)]"
							>
								<path
									d="M5 13l4 4L19 7"
									stroke="currentColor"
									stroke-width="2"
									stroke-linecap="round"
									stroke-linejoin="round"
								/>
							</svg>
							WhatsApp Order
						</li>
						<li class="flex items-center gap-2">
							<svg
								viewBox="0 0 24 24"
								fill="none"
								class="h-4 w-4 text-[var(--color-primary)]"
							>
								<path
									d="M5 13l4 4L19 7"
									stroke="currentColor"
									stroke-width="2"
									stroke-linecap="round"
									stroke-linejoin="round"
								/>
							</svg>
							1 QR Code Bisnis
						</li>
					</ul>
					<router-link
						to="/register"
						class="mt-8 block rounded-xl border border-slate-300 py-3 text-center text-sm font-semibold text-slate-800 transition duration-300 hover:bg-slate-50"
					>
						Mulai Gratis
					</router-link>
				</div>

				<div
					class="relative rounded-2xl border-2 border-[var(--color-primary)] bg-white p-8 shadow-xl"
				>
					<span
						class="absolute -top-3 right-8 rounded-full bg-[var(--color-accent)] px-3 py-1 text-xs font-semibold text-[var(--color-primary)]"
						>Paling Populer</span
					>
					<p class="text-sm font-semibold text-[var(--color-primary)]">Pro</p>
					<p class="mt-2 text-4xl font-extrabold tracking-tight text-slate-900">
						Rp99rb<span class="text-base font-medium text-slate-400">/bulan</span>
					</p>
					<p class="mt-1 text-sm text-slate-500">
						Untuk bisnis yang siap bertumbuh lebih cepat
					</p>
					<ul class="mt-6 space-y-3 text-sm text-slate-600">
						<li class="flex items-center gap-2">
							<svg
								viewBox="0 0 24 24"
								fill="none"
								class="h-4 w-4 text-[var(--color-primary)]"
							>
								<path
									d="M5 13l4 4L19 7"
									stroke="currentColor"
									stroke-width="2"
									stroke-linecap="round"
									stroke-linejoin="round"
								/>
							</svg>
							Produk & Portfolio tanpa batas
						</li>
						<li class="flex items-center gap-2">
							<svg
								viewBox="0 0 24 24"
								fill="none"
								class="h-4 w-4 text-[var(--color-primary)]"
							>
								<path
									d="M5 13l4 4L19 7"
									stroke="currentColor"
									stroke-width="2"
									stroke-linecap="round"
									stroke-linejoin="round"
								/>
							</svg>
							Custom Domain sendiri
						</li>
						<li class="flex items-center gap-2">
							<svg
								viewBox="0 0 24 24"
								fill="none"
								class="h-4 w-4 text-[var(--color-primary)]"
							>
								<path
									d="M5 13l4 4L19 7"
									stroke="currentColor"
									stroke-width="2"
									stroke-linecap="round"
									stroke-linejoin="round"
								/>
							</svg>
							Analytics lengkap
						</li>
						<li class="flex items-center gap-2">
							<svg
								viewBox="0 0 24 24"
								fill="none"
								class="h-4 w-4 text-[var(--color-primary)]"
							>
								<path
									d="M5 13l4 4L19 7"
									stroke="currentColor"
									stroke-width="2"
									stroke-linecap="round"
									stroke-linejoin="round"
								/>
							</svg>
							AI Content Assistant
						</li>
						<li class="flex items-center gap-2">
							<svg
								viewBox="0 0 24 24"
								fill="none"
								class="h-4 w-4 text-[var(--color-primary)]"
							>
								<path
									d="M5 13l4 4L19 7"
									stroke="currentColor"
									stroke-width="2"
									stroke-linecap="round"
									stroke-linejoin="round"
								/>
							</svg>
							QR Code tanpa batas
						</li>
					</ul>
					<router-link
						to="/register"
						class="mt-8 block rounded-xl bg-[var(--color-primary)] py-3 text-center text-sm font-semibold text-white shadow-lg transition duration-300 hover:bg-[var(--color-primary-hover)]"
					>
						Upgrade ke Pro
					</router-link>
				</div>
			</div>
		</section>

		<section id="faq" class="bg-slate-50 py-20">
			<div class="mx-auto max-w-3xl px-4 sm:px-6 lg:px-8">
				<div class="text-center">
					<h2 class="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl">
						Pertanyaan yang Sering Ditanyakan
					</h2>
					<p class="mt-4 text-lg text-slate-600">
						Masih ada yang mengganjal? Cek jawabannya di sini.
					</p>
				</div>

				<div class="mt-10 space-y-3">
					<div
						v-for="(item, index) in faqs"
						:key="item.q"
						class="rounded-2xl border border-slate-200 bg-white shadow-sm transition duration-300"
					>
						<button
							type="button"
							class="flex w-full items-center justify-between gap-4 px-6 py-5 text-left"
							@click="toggleFaq(index)"
						>
							<span class="text-sm font-semibold text-slate-900">{{ item.q }}</span>
							<span
								class="flex h-7 w-7 shrink-0 items-center justify-center rounded-full bg-slate-100 text-slate-600 transition duration-300"
								:class="
									activeFaq === index
										? 'rotate-45 bg-[var(--color-primary-light)] text-[var(--color-primary)]'
										: ''
								"
							>
								+
							</span>
						</button>
						<div
							v-if="activeFaq === index"
							class="px-6 pb-5 text-sm leading-relaxed text-slate-500"
						>
							{{ item.a }}
						</div>
					</div>
				</div>
			</div>
		</section>

		<section class="relative overflow-hidden bg-[var(--color-primary)] py-20">
			<div
				class="pointer-events-none absolute -bottom-24 -left-16 h-80 w-80 rounded-full bg-[radial-gradient(circle,_rgba(193,255,114,0.25)_0%,_transparent_70%)]"
			></div>
			<div class="relative mx-auto max-w-3xl px-4 text-center sm:px-6 lg:px-8">
				<h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl">
					Saatnya Bisnis Kamu Naik Level
				</h2>
				<p class="mt-4 text-lg text-white/70">
					Bergabung bersama ribuan pelaku UMKM yang sudah tampil lebih profesional dengan
					BizPage.
				</p>
				<router-link
					to="/register"
					class="mt-8 inline-flex items-center justify-center rounded-xl bg-[var(--color-accent)] px-8 py-3.5 text-sm font-semibold text-[var(--color-primary)] shadow-lg transition duration-300 hover:bg-[var(--color-accent-hover)] hover:-translate-y-0.5"
				>
					Buat Website Sekarang — Gratis
				</router-link>
			</div>
		</section>

		<footer class="bg-slate-900">
			<div class="mx-auto grid max-w-7xl gap-10 px-4 py-16 sm:px-6 lg:grid-cols-4 lg:px-8">
				<div class="lg:col-span-1">
					<div class="flex items-center gap-2.5">
						<span
							class="flex h-9 w-9 items-center justify-center rounded-xl bg-[var(--color-primary)] text-sm font-bold text-white"
							>B</span
						>
						<span class="text-lg font-bold text-white">BizPage</span>
					</div>
					<p class="mt-4 max-w-xs text-sm leading-relaxed text-slate-400">
						Platform website bisnis untuk UMKM dan bisnis kreatif, tanpa perlu coding
						sama sekali.
					</p>
				</div>

				<div>
					<p class="text-xs font-semibold uppercase tracking-wider text-slate-500">
						Produk
					</p>
					<div class="mt-4 flex flex-col gap-3 text-sm">
						<a
							href="#fitur"
							class="text-slate-400 transition duration-300 hover:text-[var(--color-accent)]"
							>Fitur</a
						>
						<a
							href="#harga"
							class="text-slate-400 transition duration-300 hover:text-[var(--color-accent)]"
							>Harga</a
						>
						<a
							href="#preview"
							class="text-slate-400 transition duration-300 hover:text-[var(--color-accent)]"
							>Template</a
						>
					</div>
				</div>

				<div>
					<p class="text-xs font-semibold uppercase tracking-wider text-slate-500">
						Perusahaan
					</p>
					<div class="mt-4 flex flex-col gap-3 text-sm">
						<a
							href="#"
							class="text-slate-400 transition duration-300 hover:text-[var(--color-accent)]"
							>Tentang Kami</a
						>
						<a
							href="#"
							class="text-slate-400 transition duration-300 hover:text-[var(--color-accent)]"
							>Karier</a
						>
						<a
							href="#"
							class="text-slate-400 transition duration-300 hover:text-[var(--color-accent)]"
							>Kontak</a
						>
					</div>
				</div>

				<div>
					<p class="text-xs font-semibold uppercase tracking-wider text-slate-500">
						Akun
					</p>
					<div class="mt-4 flex flex-col gap-3 text-sm">
						<router-link
							to="/login"
							class="text-slate-400 transition duration-300 hover:text-[var(--color-accent)]"
							>Login</router-link
						>
						<router-link
							to="/register"
							class="text-slate-400 transition duration-300 hover:text-[var(--color-accent)]"
							>Daftar</router-link
						>
						<a
							href="#faq"
							class="text-slate-400 transition duration-300 hover:text-[var(--color-accent)]"
							>FAQ</a
						>
					</div>
				</div>
			</div>

			<div class="border-t border-white/10">
				<div
					class="mx-auto flex max-w-7xl flex-col items-center justify-between gap-4 px-4 py-6 text-sm sm:flex-row sm:px-6 lg:px-8"
				>
					<p class="text-slate-500">&copy; 2026 BizPage. Semua hak dilindungi.</p>
					<div class="flex gap-6">
						<a
							href="#"
							class="text-slate-500 transition duration-300 hover:text-slate-300"
							>Kebijakan Privasi</a
						>
						<a
							href="#"
							class="text-slate-500 transition duration-300 hover:text-slate-300"
							>Syarat & Ketentuan</a
						>
					</div>
				</div>
			</div>
		</footer>
	</div>
</template>

<script setup>
import { ref } from "vue";

const mobileMenuOpen = ref(false);
const activeFaq = ref(0);

const navLinks = [
	{ href: "#fitur", label: "Fitur" },
	{ href: "#cara-kerja", label: "Cara Kerja" },
	{ href: "#harga", label: "Harga" },
	{ href: "#faq", label: "FAQ" },
];

const stats = [
	{ value: "10.000+", label: "Website Dibuat" },
	{ value: "50.000+", label: "Produk Terpajang" },
	{ value: "98%", label: "Kepuasan Pengguna" },
	{ value: "24/7", label: "Dukungan Tim" },
];

const targetMarket = [
	{ initial: "FL", label: "Florist" },
	{ initial: "WO", label: "Wedding Organizer" },
	{ initial: "MU", label: "MUA" },
	{ initial: "PH", label: "Photographer" },
	{ initial: "SV", label: "Souvenir" },
	{ initial: "HM", label: "Handmade" },
	{ initial: "BK", label: "Bakery" },
	{ initial: "CS", label: "Coffee Shop" },
	{ initial: "PC", label: "Percetakan" },
	{ initial: "FN", label: "Furniture" },
	{ initial: "UM", label: "UMKM Lainnya" },
];

const comparisonRows = [
	{ label: "Tampilan Profesional & Custom", instagram: false, bizpage: true },
	{ label: "Katalog Produk Terstruktur", instagram: false, bizpage: true },
	{ label: "Checkout Langsung ke WhatsApp", instagram: false, bizpage: true },
	{ label: "QR Code Khusus Bisnis", instagram: false, bizpage: true },
	{ label: "Analytics Pengunjung & Produk", instagram: false, bizpage: true },
	{ label: "Bisa Diakses Tanpa Aplikasi", instagram: false, bizpage: true },
	{ label: "Algoritma Menentukan Jangkauan", instagram: true, bizpage: false },
];

const faqs = [
	{
		q: "Apakah saya perlu bisa coding untuk pakai BizPage?",
		a: "Sama sekali tidak. Semua bisa diatur lewat dashboard drag and drop, dari pemilihan template sampai pengaturan produk.",
	},
	{
		q: "Apakah pesanan bisa langsung masuk ke WhatsApp saya?",
		a: "Bisa. Setiap kali customer checkout, detail pesanan otomatis terkirim ke nomor WhatsApp bisnis kamu.",
	},
	{
		q: "Apakah saya bisa ganti template kapan saja?",
		a: "Ya, kamu bebas ganti template dan menyesuaikan warna, font, serta layout tanpa kehilangan data produk.",
	},
	{
		q: "Apakah ada biaya tersembunyi di paket Free?",
		a: "Tidak ada. Paket Free bisa dipakai selamanya dengan fitur inti, tanpa perlu kartu kredit.",
	},
	{
		q: "Bagaimana cara mendapatkan QR Code untuk bisnis saya?",
		a: "QR Code otomatis dibuat begitu website kamu publish, dan bisa langsung diunduh untuk dicetak di kemasan atau banner.",
	},
];

function toggleFaq(index) {
	activeFaq.value = activeFaq.value === index ? -1 : index;
}
</script>
