from django.db import models

# Create your models here.
class Movie(models.Model):

    title = models.TextField()
    poster_path = models.TextField()
    vote_count = models.IntegerField()
    vote_average = models.IntegerField()
    backdrop_path=models.TextField()
    genre_ids=models.JSONField()
    
    