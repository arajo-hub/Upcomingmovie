from django.views.generic import TemplateView, ListView
from parsed_data import models

class mainView(TemplateView):
    template_name='main.html'

class movieListView(ListView):
    model=models.parsed_movie
    context_object_name='movies'
