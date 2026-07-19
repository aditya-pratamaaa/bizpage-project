import { createApp } from "vue";
import { FrappeUI, setConfig, frappeRequest, resourcesPlugin } from "frappe-ui";
import App from "./App.vue";
import router from "./routes.js";
import PrimeVue from "primevue/config";

import "@vueform/multiselect/themes/default.css";
import "@vueform/slider/themes/default.css";

import "primeicons/primeicons.css";

import "./style.css";

const app = createApp(App);

setConfig("socketioURL", "/");

setConfig("resourceFetcher", frappeRequest);

app.use(FrappeUI, {
	socketio: { port: 9002 },
});
// app.use(resourcesPlugin);
app.use(router);

app.mount("#app");
