import { createRouter, createWebHistory } from "vue-router";
import { session } from "./auth/session.js";

const routes = [
	{
		path: "/login",
		name: "Login",
		component: () => import("./views/authentication/login-page.vue"),
		meta: { title: "Login" },
	},
	{
		path: "/register",
		name: "Register",
		component: () => import("./views/authentication/register-page.vue"),
		meta: { title: "Daftar Akun" },
	},
	{
		path: "/",
		name: "Home",
		component: () => import("./views/pages/home-page.vue"),
		meta: { requiresAuth: true, title: "Dashboard" },
	},
];

const router = createRouter({
	history: createWebHistory("/bizpage"),
	routes,
});

router.beforeEach((to, from, next) => {
	if (to.meta.requiresAuth && !session.isLoggedIn) {
		next({ name: "Login", query: { redirect: to.fullPath } });
	} else {
		next();
	}
});

export default router;
