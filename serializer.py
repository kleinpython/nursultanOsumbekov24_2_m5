from rest_framework import serializers
from .models import Director, Movie, Review

#class DirectorSearializer(serializers.ModelSerializer):
#    class Meta:
#        model = Director
#        fields = ['name']

class Director_id_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id']

#class MovieSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Movie
#        fields = ['title', 'description', 'duration', 'director']

class Movie_id_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text', 'movie', 'stars']

class Review_id_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id']

class MovieSerializer(serializers.ModelSerializer):
    movie_reviews = ReviewSerializer(many=True)
    class Meta:
        model = Movie
        fields = ['title', 'description', 'duration', 'director', 'movie_reviews']

class DirectorSearializer(serializers.ModelSerializer):
    movie_count = MovieSerializer(many=True)
    class Meta:
        model = Director
        fields = ['name', 'movie_count']