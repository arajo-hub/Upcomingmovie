from django.db import models

class parsed_movie(models.Model):
    title=models.CharField(unique=True, max_length=256)
    date=models.CharField(max_length=256)
    code=models.CharField(default='0000000000', max_length=10)

    def __str__(self):
            return self.title
