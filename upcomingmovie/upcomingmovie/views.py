from django.views.generic import TemplateView, ListView
from parsed_data import models

class movieListView(ListView):
    model=models.parsed_movie
    context_object_name='movies'
