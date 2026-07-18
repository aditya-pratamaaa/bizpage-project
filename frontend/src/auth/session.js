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
		router.replace(router.currentRoute.value.query.redirect || "/");
	},
});

session.logout = createResource({
	url: "logout",
	onSuccess() {
		session.user = null;
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
