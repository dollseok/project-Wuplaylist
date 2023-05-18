from rest_framework import serializers
from .models import Movie, Article

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id','title','content')

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model= Article
        fields = '__all__'
        # read_only_fields = ('user',)