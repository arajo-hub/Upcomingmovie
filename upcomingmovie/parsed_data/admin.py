from django.contrib import admin
from parsed_data.models import parsed_movie
from movie.models import new_movie

admin.site.register(parsed_movie)
admin.site.register(new_movie)
