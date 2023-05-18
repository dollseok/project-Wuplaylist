from rest_framework import serializers
from .models import Movie, Article, Comment_article, Comment_movie

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title','overview','genres', 'poster_path',)

class CommentMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment_movie
        fields = '__all__'
        read_only_fields=('movie',)
        
class MovieSerializer(serializers.ModelSerializer):
    comment_set = CommentMovieSerializer(many=True, read_only=True)
    class Meta:
        model= Movie
        fields = '__all__'
        # read_only_fields = ('user',)


        
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id','title','content')

class CommentArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment_article
        fields = '__all__'
        read_only_fields = ('article',)


class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentArticleSerializer(many=True,read_only=True)
    class Meta:
        model= Article
        fields = '__all__'
        # read_only_fields = ('user',)