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
    

class Article(models.Model):
    
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
