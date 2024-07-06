<template>
        <v-card @click="redirectToMovie">
            <v-card-title>{{ movie.title }}</v-card-title>
            <v-card-text>{{ movie.description }}</v-card-text>
        </v-card>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';
import MovieDTO from '../../dto/movie/movie.dto';


const { movie } = defineProps<{
    movie: MovieDTO
}>()

const router = useRouter()

const redirectToMovie = () => {
    router.push(`/movies/${movie.id}`);
}

</script>

<style scoped>
/* Add your custom styles here */
</style>