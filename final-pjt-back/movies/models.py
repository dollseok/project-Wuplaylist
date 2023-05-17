from django.db import models

# Create your models here.
class Movie(models.Model):

    movie_id = models.IntegerField()
    title = models.TextField()
    released_date = models.DateField()
    poster_path = models.TextField()
    vote_count = models.IntegerField()
    vote_average = models.IntegerField()
    overview = models.TextField()
    genres=models.JSONField()
    # backdrop_path=models.TextField()