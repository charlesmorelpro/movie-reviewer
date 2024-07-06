<script lang="ts">
import { onMounted } from 'vue';
import { useStore } from 'vuex';

export default {
  setup() {
    const store = useStore();

    onMounted(() => {
      store.dispatch('fetchMovies');
    });
  },
};
</script>

<template>
  <div>
    <h1 class="text-h3 text-center py-6">Movie Reviewer</h1>
    <v-container>
      <router-view />
    </v-container>
  </div>
</template>

<style scoped>
</style>
