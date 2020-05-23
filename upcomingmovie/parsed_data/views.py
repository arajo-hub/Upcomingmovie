from django.views.generic import DetailView
from parsed_data import models

class movieDetailView(DetailView):
    context_object_name='movie_detail'
    model=models.parsed_movie
    template_name='parsed_data/modal.html'
