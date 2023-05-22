from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):

    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

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
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment_article(models.Model):

    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comment_articles')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment_movie(models.Model):
    
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comment_movies')
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
