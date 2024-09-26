# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import Movies
# # manual Api with django
# # Create your views here.

# # All Elements
# def movies_list(request):
#     movies = Movies.objects.all()
#     data = {"movies": list(movies.values())}
#     return JsonResponse(data)

# # Individual Elements
# def movie_details(request, pk):
#     movie = Movies.objects.get(pk=pk)
#     data = {"title": movie.title, "description": movie.description, "active": movie.active}
#     return JsonResponse(data)