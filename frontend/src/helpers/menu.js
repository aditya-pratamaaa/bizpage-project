/**
 * menu.js
 * -----------------------------------------------------------------------
 * Sumber tunggal (single source of truth) untuk struktur menu sidebar.
 *
 * Setiap item mendukung:
 *  - name    : label yang ditampilkan
 *  - route   : nama route (dipakai dengan router-link :to="{ name: route }")
 *              kosongkan/hapus jika item ini hanya parent dari submenu
 *  - icon    : nama icon MDI (Material Design Icons), TANPA prefix "mdi-".
 *              Cari nama lengkapnya di https://pictogrammers.com/library/mdi/
 *              lalu tulis di sini apa adanya, contoh: "home", "domain",
 *              "cart-outline", "cog-outline". Komponen otomatis nge-render
 *              <i class="mdi mdi-<icon>"></i> — nggak perlu mapping lagi.
 *  - roles   : array role yang boleh melihat item ini -> ['owner', 'admin']
 *  - children: (opsional) array submenu dengan struktur yang sama
 *              (name, route, roles, icon opsional) — kalau child tidak
 *              diberi 'icon', submenu tampil tanpa icon (rata kiri)
 *
 * Role yang tersedia saat ini: 'owner' dan 'admin'.
 * Tambahkan role baru di sini lalu filter otomatis berlaku di komponen.
 *
 * Wajib import CSS icon font-nya sekali di main.js:
 *   import "@mdi/font/css/materialdesignicons.css";
 * -----------------------------------------------------------------------
 */

export const menuItems = [
	{
		name: "Dashboard",
		route: "Dashboard",
		icon: "view-dashboard-outline",
		roles: ["owner", "admin"],
	},
	{
		name: "Produk",
		icon: "package-variant-closed",
		roles: ["owner", "admin"],
		children: [
			{
				name: "Semua Produk",
				route: "Products",
				icon: "format-list-bulleted",
				roles: ["owner", "admin"],
			},
			{
				name: "Tambah Produk",
				route: "produk.create",
				icon: "plus-box-outline",
				roles: ["owner", "admin"],
			},
			{
				name: "Kategori",
				route: "produk.kategori",
				icon: "shape-outline",
				roles: ["owner"],
			},
			{
				name: "Item",
				route: "produk.item",
				icon: "package-variant",
				roles: ["owner"],
			},
		],
	},
	{
		name: "Pesanan",
		route: "pesanan.index",
		icon: "cart-outline",
		roles: ["owner", "admin"],
		children: [
			{
				name: "Pesanan Masuk",
				route: "pesanan.index",
				icon: "clipboard-text-outline",
				roles: ["owner", "admin"],
			},
			{
				name: "Pesanan Diterima",
				route: "pesanan.pengiriman",
				icon: "clipboard-check-outline",
				roles: ["owner", "admin"],
			},
			{
				name: "Pesanan Diproses",
				route: "pesanan.proses",
				icon: "progress-clock",
				roles: ["owner", "admin"],
			},
			{
				name: "Pesanan Batal",
				route: "pesanan.batal",
				icon: "close-circle-outline",
				roles: ["owner", "admin"],
			},
			{
				name: "Pesanan Selesai",
				route: "pesanan.selesai",
				icon: "check-circle-outline",
				roles: ["owner", "admin"],
			},
		],
	},
	{
		name: "Website Saya",
		icon: "web",
		roles: ["owner", "admin"],
		children: [
			{
				name: "Pengaturan Website",
				route: "website.settings",
				icon: "cog-outline",
				roles: ["owner", "admin"],
			},
			{
				name: "Tema & Tampilan",
				route: "website.theme",
				icon: "palette-outline",
				roles: ["owner", "admin"],
			},
		],
	},
	{
		name: "Langganan",
		route: "billing.index",
		icon: "credit-card-outline",
		roles: ["owner"],
	},
	{
		name: "Pengaturan",
		route: "settings.index",
		icon: "cog-outline",
		roles: ["owner", "admin"],
	},
];

/**
 * Helper: filter menu berdasarkan role user saat ini.
 * Item parent tanpa children yang lolos filter akan otomatis disembunyikan.
 *
 * @param {Array} items - menuItems (atau subset-nya)
 * @param {string} role - 'owner' | 'admin'
 * @returns {Array} menu yang sudah difilter sesuai role
 */
export function filterMenuByRole(items, role) {
	return items
		.filter((item) => item.roles.includes(role))
		.map((item) => {
			if (!item.children) return item;
			const children = item.children.filter((child) => child.roles.includes(role));
			return { ...item, children };
		})
		.filter((item) => item.route || (item.children && item.children.length > 0));
}
