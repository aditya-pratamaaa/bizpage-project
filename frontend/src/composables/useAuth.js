// composables/useAuth.js
import { createResource } from "frappe-ui";
import { computed, ref } from "vue";

const loading = ref(true);
const errorMessage = ref(null);
const currentUser = ref({
	name: "",
	fullName: "",
	avatar: "",
	role: null,
});

function loadFromBoot() {
	const boot = window.frappe?.boot;
	if (!boot) return;

	const userId = boot.user?.name;
	const info = boot.user_info?.[userId];

	currentUser.value.name = userId || "";
	currentUser.value.fullName = info?.fullname || userId || "";
	currentUser.value.avatar = info?.image || "";
}

const userRoleResource = createResource({
	url: "bizpage.api.auth_api.get_user_role",
	auto: false,
	onSuccess(data) {
		currentUser.value.role = data.role; // "owner" | "admin"
		loading.value = false;
	},
	onError(error) {
		// muncul kalau: belum login (Guest) atau role_profile_name belum diisi
		errorMessage.value = error.messages?.[0] || "Gagal memuat data pengguna";
		loading.value = false;
	},
});

export function useAuth() {
	if (!currentUser.value.name && window.frappe?.session?.user !== "Guest") {
		loadFromBoot();
		userRoleResource.fetch();
	} else if (window.frappe?.session?.user === "Guest") {
		loading.value = false;
	}

	return {
		currentUser: computed(() => currentUser.value),
		loading: computed(() => loading.value),
		error: computed(() => errorMessage.value),
	};
}
