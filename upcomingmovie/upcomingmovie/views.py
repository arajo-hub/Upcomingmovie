from django.views.generic import ListView, DetailView
from parsed_data import models

class movieListView(ListView):
    model=models.parsed_movie
    context_object_name='movies'

class movieDetailView(DetailView):
    context_object_name='movie_detail'
    model=models.parsed_movie
    template_name='parsed_data/parsed_movie_list.html'
