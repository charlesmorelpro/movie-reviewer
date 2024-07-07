import { createStore } from "vuex";
import axios from "axios";
import DetailedMovieDTO from "../dto/movie/detailed-movie.dto";
import MovieDTO from "../dto/movie/movie.dto";
import ActorDTO from "../dto/actor/actor.dto";

interface State {
    movies: MovieDTO[] | null;
    nextUrl: string | null;
    prevUrl: string | null;
    selectedMovie: DetailedMovieDTO | null;
    actors: ActorDTO[] | null;
    movieCount: number;
}

export default createStore({
    state: {
        movies: null,
        nextUrl: null as string | null,
        prevUrl: null as string | null,
        selectedMovie: null as DetailedMovieDTO | null,
        actors: null,
        movieCount: 0
    } as State,
    mutations: {
        setMovies(state, movies) {
            state.movies = movies;
        },
        setSelectedMovie(state, movie) {
            state.selectedMovie = movie;
        },
        setActors(state, actors) {
            state.actors = actors;
        },
        setMovieCount(state, count) {
            state.movieCount = count;
        }
    },
    actions: {
        async fetchMovies({ commit }, page: number) {
            const response = await axios.get(`http://localhost:8000/movies/?page=${page}`);
            const data = response.data;
            commit('setMovies', data.results);
            commit('setMovieCount', data.count);
        },
        async fetchMovieDetails({ commit }, id) {
            const response = await axios.get(`http://localhost:8000/movies/${id}`);
            const data = response.data;
            commit('setSelectedMovie', data);
        },
        async fetchActors({commit}) {
            const response = await axios.get('http://localhost:8000/actors/');
            commit('setActors', response.data)
        },
        async updateMovie({dispatch}, data) {
            const { id, ...movieData} = data
            await axios.patch(`http://localhost:8000/movies/${id}/update/`, movieData);
            dispatch('fetchMovies', 1);
        }
    },
})