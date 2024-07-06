<template>
    <div v-if="store.state.selectedMovie">
        <div class="d-flex justify-space-between mb-4">
            <div class="w-50">
                <h1 class="text-h4 mb-4">{{ store.state.selectedMovie.title }}</h1>
                <v-rating v-model="store.state.selectedMovie.rate" half-increments readonly></v-rating> ({{ store.state.selectedMovie.rate }})
                <v-card v-if="!store.state.selectedMovie.rate" variant="tonal" class="mb-4 pa-4">
                    Ce film n'a pas encore de revue. Soyez le premier à donner votre avis !
                </v-card>
                <p class="mb-4">{{ store.state.selectedMovie.description }}</p>
                <div class="d-flex">
                    <v-rating v-model="rating" half-increments hover></v-rating>
                    <v-btn @click="addReview">Ajouter une review</v-btn>
                </div>
            </div>
            <v-btn>
                éditer
            </v-btn>
        </div>
    </div>
</template>

<script setup lang="ts">
import axios from "axios";
import { ref } from "vue";
import { onMounted } from "vue";
import { useRoute } from "vue-router";
import { useStore } from "vuex";

const store = useStore();

onMounted(async () => {
    const route = useRoute();
    await store.dispatch("fetchMovieDetails", route.params.id);
});

const rating = ref(null);

const addReview = async () => {
    console.log(rating)
    if (rating) {
        await axios.post('http://localhost:8000/reviews/', {
            movie: store.state.selectedMovie.id,
            grade: rating.value,
        })
        await store.dispatch("fetchMovieDetails", store.state.selectedMovie.id);
    }
};

</script>

<style scoped>
</style>