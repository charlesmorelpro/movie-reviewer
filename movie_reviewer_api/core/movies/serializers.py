from rest_framework import serializers
from django.db.models import Avg

from core.actors.models import Actor
from core.actors.serializers import ActorSerializer
from core.movies.models import Movie
from core.reviews.models import Review
from core.reviews.serializers import ReviewSerializer


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("id", "title", "description")


class MovieDetailsSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    reviews = ReviewSerializer(many=True)
    rate = serializers.SerializerMethodField()

    def get_rate(self, obj):
        reviews = Review.objects.filter(movie=obj).aggregate(Avg('grade'))
        return reviews['grade__avg']

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "actors", "reviews", "rate")
        depth = 1


class MovieUpdateSerializer(serializers.ModelSerializer):
    actors = serializers.PrimaryKeyRelatedField(many=True, queryset=Actor.objects.all())

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "actors")
        depth = 1

    def update(self, instance, validated_data):
        actors_data = validated_data.pop("actors", [])
        instance = super().update(instance, validated_data)
        instance.actors.set(actors_data)
        return instance
