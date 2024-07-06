<template>
    <div class="home">
        <v-row>
            <v-col v-for="(movie, index) in movies" :key="index" cols="12" sm="6" md="4">
                <movie-card :movie="movie"></movie-card>
            </v-col>
        </v-row>
    </div>
</template>

<script>
import MovieCard from '../components/cards/MovieCard.vue';
export default {
  components: { MovieCard },
    name: 'Home',
    computed: {
        movies() {
            return this.$store.state.movies;
        }
    },
}
</script>

<style scoped>
</style>