import { createRouter, createWebHistory } from "vue-router";
import Home from "../pages/Home.vue";
import MovieDetails from "../pages/MovieDetails.vue";
import MovieEdit from "../pages/MovieEdit.vue"

const routes = [
    { path: '/', component: Home },
    { path: '/movies/:id', component: MovieDetails },
    { path: '/movies/:id/edit', component: MovieEdit }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router