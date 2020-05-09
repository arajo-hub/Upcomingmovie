from django.db import models
from datetime import datetime

class new_movie(models.Model):
    title=models.CharField(unique=True, max_length=256)
    date=models.DateField(default=datetime.now())
