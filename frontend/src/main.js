import { createApp } from "vue";
import App from "./App.vue";
import router from "./routes.js";

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue-next/dist/bootstrap-vue-next.css";
import "@vueform/multiselect/themes/default.css";
import "@vueform/slider/themes/default.css";

import "./style.css";

const app = createApp(App);

app.use(router);

app.mount("#app");
