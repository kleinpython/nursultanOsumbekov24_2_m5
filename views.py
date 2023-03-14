from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from Afisha.models import Director, Movie, Review
from Afisha.serializer import DirectorSearializer, MovieSerializer, ReviewSerializer

@api_view(['GET', 'POST'])
def director_list_api_view(request):
    if request.method == 'GET':
        """LIST"""
        directors = Director.objects.all()
        serializer = DirectorSearializer(directors, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        """CREATE"""
        name = request.data.get('name')
        directors = Director.objects.create(name=name)
        return Response(data=DirectorSearializer(directors).data)
@api_view(['GET', 'PUT', 'DELETE'])
def director_id_list_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'СПЕЦИАЛЬНО ДЛЯ ТУПЫХ': "НЕ НЕСИ ХУЙНЮ"},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DirectorSearializer(director, many=False)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        director.name = request.data.get('name')
        return Response(data=DirectorSearializer(director).data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def movie_list_api_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
        return Response(data=MovieSerializer(movie).data,
                        status=status.HTTP_201_CREATED)
@api_view(['GET', 'PUT', 'DELETE'])
def movie_id_list_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'СПЕЦИАЛЬНО ДЛЯ ТУПЫХ': "НЕ НЕСИ ХУЙНЮ"},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director_id')
        return Response(data=MovieSerializer(movie).data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews)
    return Response(data=serializer.data)

@api_view(['GET'])
def review_id_list_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'СПЕЦИАЛЬНО ДЛЯ ТУПЫХ': "НЕ НЕСИ ХУЙНЮ"},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        review.text = request.data.get('text')
        review.movie_id = request.data.get('movie_id')
        review.stars = request.data.get('stars')
        return Response(data=ReviewSerializer(review).data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)