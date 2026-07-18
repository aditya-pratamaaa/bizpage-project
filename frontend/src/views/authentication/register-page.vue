<template>
	<div class="flex min-h-screen items-center justify-center bg-gray-50">
		<div class="w-full max-w-sm space-y-4 rounded-lg border p-6 shadow-sm">
			<h1 class="text-xl font-semibold">Daftar Akun</h1>

			<Input label="Username" v-model="fullName" placeholder="Nama kamu" />
			<Input type="email" label="Email" v-model="email" placeholder="you@example.com" />
			<Input type="password" label="Password" v-model="password" placeholder="••••••••" />

			<ErrorMessage :message="session.signup.error" />

			<div v-if="session.signup.data" class="text-sm text-green-600">
				Registrasi berhasil, cek email kamu untuk verifikasi.
			</div>

			<Button
				variant="solid"
				class="w-full"
				:loading="session.signup.loading"
				@click="submit"
			>
				Daftar
			</Button>

			<p class="text-center text-sm text-gray-600">
				Sudah punya akun?
				<router-link to="/login" class="text-blue-600 hover:underline">
					Login
				</router-link>
			</p>
		</div>
	</div>
</template>

<script setup>
import { ref } from "vue";
import { Input, Button, ErrorMessage, Password } from "frappe-ui";
import { session } from "../../auth/session.js";

const fullName = ref("");
const email = ref("");
const password = ref("");

function submit() {
	session.signup.submit({
		email: email.value,
		fullName: fullName.value,
		password: password.value,
	});
}
</script>
