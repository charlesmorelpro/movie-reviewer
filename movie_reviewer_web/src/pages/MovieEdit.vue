<template>
    <div class="d-flex justify-center">
        <v-sheet :width="800">
            <v-form v-if="store.state.selectedMovie" @submit.prevent="onSubmit">
                <v-text-field v-model="title" label="Titre du film"></v-text-field>
                <v-textarea v-model="description" label="Description"></v-textarea>
                <v-autocomplete v-model="movieActors" label="Acteurs" :items="actors" item-value="id" item-title="full_name" multiple chips closable-chips></v-autocomplete>
                <v-btn variant="outlined" type="submit" class="float-right">Modifier les informations</v-btn>
            </v-form>
        </v-sheet>
    </div>
</template>

<script setup lang="ts">
import { onMounted, ref, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useStore } from 'vuex';
import ActorDTO from '../dto/actor/actor.dto';

const route = useRoute();
const router = useRouter()
const store = useStore();
const title = ref(store.state.selectedMovie?.title || '');
const description = ref(store.state.selectedMovie?.description || '');
const actors = ref(store.state.actors || [] as ActorDTO[])
const movieActors = ref(store.state.selectedMovie?.actors.map((actor: ActorDTO) => actor.id) || [] as ActorDTO[])

onMounted(() => {
    if (!store.state.selectedMovie) {
        store.dispatch('fetchMovieDetails', route.params.id)
    }
    if (!store.state.actors) {
        store.dispatch('fetchActors')
    }
})

const onSubmit = async () => {
    const data = {
        id: route.params.id,
        title: title.value,
        description: description.value,
        actors: movieActors.value
    }
    await store.dispatch('updateMovie', data)
    router.push({ path: `/movies/${route.params.id}` })
}
watch(() => store.state.selectedMovie, (selectedMovie) => {
    if (selectedMovie) {
        title.value = selectedMovie.title;
        description.value = selectedMovie.description;
        movieActors.value = selectedMovie.actors.map((actor: ActorDTO) => actor.id)
    }
});
watch(() => store.state.actors, (actorsState: ActorDTO[]) => {
    if (actorsState) {
        actors.value = actorsState
    }
})

</script>