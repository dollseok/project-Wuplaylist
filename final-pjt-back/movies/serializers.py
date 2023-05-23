from rest_framework import serializers
from .models import Movie, Article, Comment_article, Comment_movie, Genre

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        # fields = ('title','overview','genres', 'poster_path', 'like_user')

class CommentMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment_movie
        fields = '__all__'
        # read_only_fields=('movie', 'user', 'like_user')
        
class MovieSerializer(serializers.ModelSerializer):
    comment_movie_set = CommentMovieSerializer(many=True, read_only=True)
    class Meta:
        model= Movie
        fields = '__all__'
        # read_only_fields = ('user', 'like_user')
        
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', 'like_user')

class CommentArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment_article
        fields = '__all__'
        read_only_fields = ('article', 'user', 'like_user')

from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('__all__')

class ArticleSerializer(serializers.ModelSerializer):
    comment_article_set = CommentArticleSerializer(many=True,read_only=True)
    # user = UserSerializer(many=True)
    
    class Meta:
        model= Article
        fields = '__all__'
        read_only_fields = ('user', 'like_user',)
        

# 장르 시리얼라이저

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'