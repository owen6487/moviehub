from django.shortcuts import render

def home(request):
    return render(request, 'movies/home.html')

def list_movies(request):
    return render(request, 'movies/list.html')

def movie_details(request):
    return render(request, 'movies/details.html')

