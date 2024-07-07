<template>
    <div class="home">
        <v-row class="mb-8">
            <v-col v-for="(movie, index) in store.state.movies" :key="index" cols="12" sm="6" md="4">
                <movie-card :movie="movie"></movie-card>
            </v-col>
        </v-row>
        <v-pagination v-model="page" :length="pageCount" @click="handlePageChange"></v-pagination>
    </div>
</template>

<script setup lang="ts">
import MovieCard from "../components/cards/MovieCard.vue";
import { ref } from "vue";
import { computed } from "vue";
import { onMounted } from "vue";
import { useStore } from "vuex";

const store = useStore()
const page = ref(1)

onMounted(() => {
    store.dispatch('fetchMovies', 1)
})

const pageCount = computed(() => {
    const fullPages = Math.floor(store.state.movieCount / 5)
    const hasRemainder = store.state.movieCount % 5 > 0
    return fullPages + (hasRemainder ? 1 : 0)
})

const handlePageChange = () => {
    store.dispatch('fetchMovies', page.value)
}
</script>

<style scoped>
</style>