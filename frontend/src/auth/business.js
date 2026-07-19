// auth/business.js
//
// Simpan info bisnis milik user login, di-refresh SETELAH login.
// Dipakai buat TAMPILAN (nama toko di header, dsb) dan buat
// auto-isi field "business" pas bikin produk baru.
//
// PENTING: ini BUKAN buat filter data. Filter data tetap dikerjakan
// backend lewat permission_query_conditions (lihat permissions.py).
// Jadi walaupun value di sini "dicurangin" lewat DevTools,
// gak akan bisa nembus data bisnis lain, karena backend tetap
// nge-cek ulang dari frappe.session.user.

import { createResource } from "frappe-ui";
import { reactive } from "vue";
import { session } from "./session.js";

export const businessStore = reactive({
	data: null, // { name, business_name, username, logo, ... }
});

const myBusinessResource = createResource({
	url: "bizpage.api.business_api.get_my_business",
	auto: false,
	onSuccess(data) {
		businessStore.data = data;
	},
});

export async function loadMyBusiness() {
	if (!session.isLoggedIn) {
		businessStore.data = null;
		return null;
	}
	if (!businessStore.data) {
		await myBusinessResource.fetch();
	}
	return businessStore.data;
}

export function clearBusinessCache() {
	businessStore.data = null;
	myBusinessResource.reset();
}
