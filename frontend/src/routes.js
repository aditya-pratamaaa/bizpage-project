import { createRouter, createWebHistory } from "vue-router";
import { setupAuthGuard } from "./auth/authGuard.js";

const routes = [
	// ---------- PUBLIC / CUSTOMER (tanpa login) ----------
	{
		path: "/",
		name: "Home",
		component: () => import("./views/pages/home-page.vue"),
		meta: { title: "Home", guestOnly: true },
	},
	{
		path: "/login",
		name: "Login",
		component: () => import("./views/auth/login-page.vue"),
		meta: { title: "Login", guestOnly: true },
	},
	{
		path: "/register",
		name: "Register",
		component: () => import("./views/auth/register-page.vue"),
		meta: { title: "Daftar Akun", guestOnly: true },
	},
	// {
	// 	// Katalog publik: katalogin.id/:username
	// 	path: "/:username",
	// 	name: "PublicCatalog",
	// 	component: () => import("./views/catalog/catalog-page.vue"),
	// 	meta: { title: "Katalog" },
	// },

	// ---------- OWNER (wajib login, role: owner) ----------
	{
		path: "/dashboard",
		name: "Dashboard",
		component: () => import("./views/pages/dashboard/dashboard-page.vue"),
		meta: { requiresAuth: true, roles: ["owner"], title: "Dashboard" },
	},
	{
		path: "/products",
		name: "Products",
		component: () => import("./views/pages/owner/products/product/products-list.vue"),
		meta: { requiresAuth: true, roles: ["owner"], title: "Produk" },
	},
	// {
	// 	path: "/dashboard/products",
	// 	name: "Products",
	// 	component: () => import("./views/pages/products-page.vue"),
	// 	meta: { requiresAuth: true, roles: ["owner"], title: "Produk" },
	// },
	// {
	// 	path: "/dashboard/portfolio",
	// 	name: "Portfolio",
	// 	component: () => import("./views/pages/portfolio-page.vue"),
	// 	meta: { requiresAuth: true, roles: ["owner"], title: "Portfolio" },
	// },

	// ---------- ADMIN (wajib login, role: admin) ----------
	// {
	// 	path: "/admin",
	// 	name: "AdminDashboard",
	// 	component: () => import("./views/admin/admin-dashboard.vue"),
	// 	meta: { requiresAuth: true, roles: ["admin"], title: "Admin Panel" },
	// },
	// {
	// 	path: "/admin/businesses",
	// 	name: "AdminBusinesses",
	// 	component: () => import("./views/admin/admin-businesses.vue"),
	// 	meta: { requiresAuth: true, roles: ["admin"], title: "Kelola Bisnis" },
	// },
	// {
	// 	path: "/admin/users",
	// 	name: "AdminUsers",
	// 	component: () => import("./views/admin/admin-users.vue"),
	// 	meta: { requiresAuth: true, roles: ["admin"], title: "Kelola User" },
	// },

	// ---------- FALLBACK ----------
	// {
	// 	path: "/forbidden",
	// 	name: "Forbidden",
	// 	component: () => import("./views/errors/forbidden-page.vue"),
	// 	meta: { title: "Akses Ditolak" },
	// },
	// {
	// 	path: "/:pathMatch(.*)*",
	// 	name: "NotFound",
	// 	component: () => import("./views/errors/not-found-page.vue"),
	// 	meta: { title: "Halaman Tidak Ditemukan" },
	// },
];

const router = createRouter({
	history: createWebHistory("/bizpage"),
	routes,
});

setupAuthGuard(router);

export default router;
