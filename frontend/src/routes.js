import { createRouter, createWebHistory } from "vue-router";
import Home from "./views/pages/home-page.vue";

const routes = [
	{
		path: "/",
		name: "Home",
		component: Home,
		meta: {
			title: "Dashboard - Katalogin",
			requiresAuth: false,
		},
	},
	// {
	// 	path: "/login",
	// 	name: "Login",

	// 	component: () => import("./views/pages/login-page.vue"),
	// 	meta: {
	// 		title: "Masuk - Katalogin",
	// 		requiresAuth: false,
	// 	},
	// },
];

const router = createRouter({
	history: createWebHistory(),
	routes,
});

router.beforeEach((to, from, next) => {
	document.title = to.meta.title || "Katalogin";
	next();
});

export default router;
