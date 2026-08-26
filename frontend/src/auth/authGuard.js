// auth/authGuard.js
// Guard global Vue Router: cek login + role (owner / admin).
// Jalan di setiap perpindahan route, termasuk tombol back/forward browser.

import { session, ensureUserRole } from "./session.js";

// Halaman "home" default per role, dipakai buat redirect
// kalau user salah akses (guestOnly page) atau salah role.
const HOME_BY_ROLE = {
	owner: { name: "Dashboard" },
	admin: { name: "AdminDashboard" },
};
const DEFAULT_HOME = { name: "Dashboard" };

export function setupAuthGuard(router) {
	router.beforeEach(async (to, from, next) => {
		const loggedIn = session.isLoggedIn;

		const requiresAuth = to.matched.some((r) => r.meta.requiresAuth);
		const guestOnly = to.matched.some((r) => r.meta.guestOnly);
		// gabungkan roles dari semua matched record (kalau nested route)
		const allowedRoles = to.matched.flatMap((r) => r.meta.roles || []).filter(Boolean);

		// 1) Belum login tapi mau akses halaman yang butuh login
		if (requiresAuth && !loggedIn) {
			return next({ name: "Login", query: { redirect: to.fullPath } });
		}

		// 2) Sudah login tapi mau ke halaman guest-only (/, /login, /register)
		//    -> lempar ke home sesuai role (termasuk saat pencet tombol back)
		if (guestOnly && loggedIn) {
			const role = await ensureUserRole();
			return next(HOME_BY_ROLE[role] || { name: "Dashboard" });
		}

		// 3) Sudah login, route butuh role tertentu -> cek rolenya cocok atau tidak
		if (requiresAuth && allowedRoles.length > 0) {
			const role = await ensureUserRole();

			if (!role) {
				// Gagal ambil role (mis. API error) -> aman-nya lempar ke login
				return next({ name: "Login", query: { redirect: to.fullPath } });
			}

			if (!allowedRoles.includes(role)) {
				// Login valid, tapi role gak sesuai (mis. owner coba ke /admin)
				return next(HOME_BY_ROLE[role] || { name: "Dashboard" });
				// Ganti ke next({ name: "Forbidden" }) kalau route /forbidden sudah di-uncomment
			}
		}

		next();
	});
}
