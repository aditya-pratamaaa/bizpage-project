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
	// Menyisipkan konfigurasi server proxy untuk Socket.io
	server: {
		proxy: {
			"/socket.io": {
				target: "http://localhost:9002", // Ubah ke port 9002 (sesuai port socketio bench kamu)
				ws: true, // Wajib true untuk mengaktifkan WebSockets
				changeOrigin: true,
			},
		},
	},
	optimizeDeps: {
		include: ["feather-icons", "debug", "vue", "vue-router"],
	},
});
