<template>
	<router-view />
</template>

<script setup>
import { useRoute } from "vue-router";
import { watch } from "vue";

const route = useRoute();

watch(
	() => route.meta.title,
	(title) => {
		document.title = title ? `Bizpage | ${title}` : "Bizpage";
	},
	{ immediate: true },
);
</script>
