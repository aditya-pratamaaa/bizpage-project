import path from "path";
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import frappeui from "frappe-ui/vite";

export default defineConfig({
	plugins: [
		frappeui({
			frontendRoute: "/bizpage",
		}),
		vue(),
	],
	resolve: {
		alias: {
			"@": path.resolve(__dirname, "src"),
		},
	},

	server: {
		proxy: {
			"/socket.io": {
				target: "http://localhost:9002",
				ws: true,
				changeOrigin: true,
			},
		},
	},
	optimizeDeps: {
		include: ["feather-icons", "debug", "vue", "vue-router"],
	},
});
