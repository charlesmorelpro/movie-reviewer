import ActorDTO from "../actor/actor.dto";
import ReviewDTO from "../review/review.dto";

export default interface DetailedMovieDTO {
    id: number;
    title: string;
    description: string;
    actors: ActorDTO[];
    reviews: ReviewDTO[];
    rate: number;
}