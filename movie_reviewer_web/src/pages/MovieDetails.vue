<template>
    <div v-if="store.state.selectedMovie">
            <div class="d-flex justify-space-between">
                <div class="d-flex">
                    <h1 class="text-h4 mb-4 w-75">{{ store.state.selectedMovie.title }}</h1>
                    <v-rating v-if="store.state.selectedMovie.rate" v-model="store.state.selectedMovie.rate" half-increments readonly></v-rating>
                </div>
                <v-btn variant="outlined" @click="redirectToEditPage">
                    éditer
                </v-btn>
            </div>
            <div class="d-flex ga-2 mb-4">
                <v-chip v-for="(actor, index) in store.state.selectedMovie.actors" :key="index">{{ actor.full_name }}</v-chip>
            </div>
            <v-card v-if="!store.state.selectedMovie.rate" variant="tonal" class="mb-4 pa-4">
                Ce film n'a pas encore de revue. Soyez le premier à donner votre avis !
            </v-card>
            <p>{{ store.state.selectedMovie.description }}</p>
            <div class="d-flex align-center justify-center my-16">
                <v-rating v-model="rating" half-increments hover class="mr-4"></v-rating>
                <v-btn variant="outlined" @click="addReview">Ajouter une review</v-btn>
            </div>
            <div class="text-center">
                <router-link to="/" class="text-decoration-none text-black font-weight-medium">Revenir à l'accueil</router-link>
            </div>
        </div>
</template>

<script setup lang="ts">
import axios from "axios";
import { ref } from "vue";
import { onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useStore } from "vuex";

const store = useStore();
const route = useRoute();
const router = useRouter();

onMounted(async () => {
    await store.dispatch("fetchMovieDetails", route.params.id);
});

const rating = ref(null);

const addReview = async () => {
    if (rating) {
        await axios.post('http://localhost:8000/reviews/', {
            movie: store.state.selectedMovie.id,
            grade: rating.value,
        })
        await store.dispatch("fetchMovieDetails", store.state.selectedMovie.id);
    }
};

const redirectToEditPage = () => {
    router.push({
        path: `/movies/${route.params.id}/edit`
    })
}

</script>

<style scoped>
</style>