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

class Comment_article(models.Model):
    
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# class Comment_movie(models.Model):
    
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
#     content = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
