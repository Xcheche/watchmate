from watchlist_app.api.serializers import MoviesSerializer
from watchlist_app.models import Movies
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def movies_list(request):
    movies = Movies.objects.all()
    # Many=True once getting multiple objects
    serializer = MoviesSerializer(movies, many=True)
    return  Response(serializer.data)

@api_view(['GET'])
def movie_details(request, pk):
    movie = Movies.objects.get(pk=pk)
    serializer = MoviesSerializer(movie)
    return Response(serializer.data)