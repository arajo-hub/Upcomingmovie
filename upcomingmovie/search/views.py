from django.shortcuts import render
from parsed_data.models import parsed_movie
from django.db.models import Q

def searchMovie(request):
    movies=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        movies=parsed_movie.objects.all().filter(Q(title__contains=query))

    return render(request, 'search/search.html', {'query':query, 'movies':movies})
