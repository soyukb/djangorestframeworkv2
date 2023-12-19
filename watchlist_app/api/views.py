from rest_framework.response import Response
from rest_framework.decorators import api_view
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer

@api_view()
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    print(movies)
    print(serializer.data)
    return Response(serializer.data)

@api_view()
def movie_detail(request, pk):
    movie = Movie.objects.get(pk = pk)
    serializer = MovieSerializer(movie)
    print(movie)
    print(serializer)
    return Response(serializer.data)
    
