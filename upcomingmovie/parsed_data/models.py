from django.db import models

class parsed_movie(models.Model):
    title=models.CharField(unique=True, max_length=256)
    date=models.CharField(max_length=256)

    def __str__(self):
            return self.title
