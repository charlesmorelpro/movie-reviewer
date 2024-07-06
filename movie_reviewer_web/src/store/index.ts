import { createStore } from "vuex";
import axios from "axios";
import DetailedMovieDTO from "../dto/movie/detailed-movie.dto";
import MovieDTO from "../dto/movie/movie.dto";

interface State {
    movies: MovieDTO[];
    nextUrl: string | null;
    prevUrl: string | null;
    selectedMovie: DetailedMovieDTO | null;

}

export default createStore({
    state: {
        movies: [] as MovieDTO[],
        nextUrl: null as string | null,
        prevUrl: null as string | null,
        selectedMovie: null as DetailedMovieDTO | null
    } as State,
    mutations: {
        setMovies(state, movies) {
            state.movies = movies;
        },
        setNextUrl(state, url) {
            state.nextUrl = url;
        },
        setPrevUrl(state, url) {
            state.prevUrl = url;
        },
        setSelectedMovie(state, movie) {
            state.selectedMovie = movie;
        }
    },
    actions: {
        async fetchMovies({ commit }) {
            const response = await axios.get('http://localhost:8000/movies');
            const data = response.data;
            commit('setMovies', data.results);
            commit('setNextUrl', data.next);
            commit('setPrevUrl', data.previous);
        },
        async fetchMovieDetails({ commit }, id) {
            const response = await axios.get(`http://localhost:8000/movies/${id}`);
            const data = response.data;
            commit('setSelectedMovie', data);
        }
    },
    getters: {
        getMovies(state) {
            return state.movies;
        },
        getNextUrl(state) {
            return state.nextUrl;
        },
        getPrevUrl(state) {
            return state.prevUrl;
        },
        getSelectedMovie(state) {
            return state.selectedMovie;
        }
    }
})