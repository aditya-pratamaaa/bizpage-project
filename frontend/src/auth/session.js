import { createResource } from "frappe-ui";
import { computed, reactive } from "vue";
import router from "../routes.js";

export function sessionUser() {
	const cookies = new URLSearchParams(document.cookie.split("; ").join("&"));
	let _sessionUser = cookies.get("user_id");
	if (_sessionUser === "Guest") {
		_sessionUser = null;
	}
	return _sessionUser;
}

export const session = reactive({
	user: sessionUser(),
	isLoggedIn: computed(() => !!session.user),
});

// Ambil role user dari backend (owner / super_admin).
// GANTI url di bawah dengan API kamu sendiri, contoh whitelisted method di Frappe:
//
//   @frappe.whitelist()
//   def get_user_role():
//       user = frappe.session.user
//       roles = frappe.get_roles(user)
//       if "System Manager" in roles or "Super Admin" in roles:
//           return {"role": "super_admin"}
//       return {"role": "owner"}
//
session.userRole = createResource({
	url: "bizpage.api.auth_api.get_user_role",
	auto: false,
	cache: "userRole",
});

// Helper: pastikan role sudah ke-fetch, dipakai di authGuard.
export async function ensureUserRole() {
	if (!session.isLoggedIn) return null;
	if (!session.userRole.data) {
		await session.userRole.fetch();
	}
	return session.userRole.data?.role || null;
}

session.login = createResource({
	url: "login",
	makeParams({ userName, password }) {
		return {
			usr: userName,
			pwd: password,
		};
	},
	onSuccess() {
		session.user = sessionUser();
		session.login.reset();
		session.userRole.reset(); // reset supaya role di-fetch ulang sesuai user baru
		router.replace(router.currentRoute.value.query.redirect || "/");
	},
});

session.logout = createResource({
	url: "logout",
	onSuccess() {
		session.user = null;
		session.userRole.reset();
		window.location.href = "/login";
	},
});

session.signup = createResource({
	url: "bizpage.api.auth_api.custom_sign_up",
	makeParams({ email, fullName, password }) {
		return { email, full_name: fullName, password };
	},
});

session.resendVerification = createResource({
	url: "bizpage.api.auth_api.resend_verification",
	makeParams({ email }) {
		return { email };
	},
});
