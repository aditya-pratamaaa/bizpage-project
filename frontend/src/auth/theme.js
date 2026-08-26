import { reactive, watch } from "vue";

const STORAGE_KEY = "bizpage-theme";

function getInitialMode() {
	const saved = localStorage.getItem(STORAGE_KEY);
	if (saved === "dark" || saved === "light") return saved;
	return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
}

function applyMode(mode) {
	document.documentElement.classList.toggle("dark", mode === "dark");
	localStorage.setItem(STORAGE_KEY, mode);
}

export const theme = reactive({
	mode: getInitialMode(),
});

// Terapkan langsung saat module ini pertama kali di-import (sebelum
// komponen manapun mount), supaya tidak ada "kedipan" tema salah
// sesaat sebelum toggle sempat jalan.
applyMode(theme.mode);

watch(
	() => theme.mode,
	(mode) => applyMode(mode),
);

export function toggleTheme() {
	theme.mode = theme.mode === "dark" ? "light" : "dark";
}
