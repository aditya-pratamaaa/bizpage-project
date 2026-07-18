<template>
	<div class="flex min-h-screen items-center justify-center bg-gray-50">
		<div class="w-full max-w-sm space-y-4 rounded-lg border p-6 shadow-sm">
			<h1 class="text-xl font-semibold">Login</h1>

			<Input type="text" label="Username" v-model="username" placeholder="Username Anda" />
			<Input
				type="password"
				label="Password"
				v-model="password"
				placeholder="••••••••"
				@keyup.enter="submit"
			/>

			<ErrorMessage :message="session.login.error" />

			<Button
				variant="solid"
				class="w-full"
				:loading="session.login.loading"
				@click="submit"
			>
				Login
			</Button>

			<p class="text-center text-sm text-gray-600">
				Belum punya akun?
				<router-link to="/register" class="text-blue-600 hover:underline">
					Daftar
				</router-link>
			</p>
		</div>
	</div>
</template>

<script setup>
import { ref } from "vue";
import { Input, Button, ErrorMessage } from "frappe-ui";
import { session } from "../../auth/session.js";

const username = ref("");
const password = ref("");

function submit() {
	session.login.submit({
		userName: username.value,
		password: password.value,
	});
}
</script>
