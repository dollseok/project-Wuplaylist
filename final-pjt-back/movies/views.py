from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import *

from .models import *



# 데이터 파일 제이슨으로 받기
# 현재는 고정, 업데이트가 필요할 수도 있음
# 런서버 할 때(프로그램이 시작될 때) 자동으로 업데이트가 되긴 함

import requests
import json

def get_movie_datas():
    total_data = []

    for i in range(1,20):
        url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=ko-KR&page={i}&sort_by=popularity.desc"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0YjNlM2FhNjVlOTZlOTVjN2Y0MWZmMDdmY2NkMzAxYiIsInN1YiI6IjYzZDMxYTM4NWEwN2Y1MDA5ZTk4MDM0YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.svzZx8RMTp1kjkBzxbvcOuoduFUJjduTqyQf-ufCBfo"
        }

        response = requests.get(url, headers=headers).json()

        for movie in response['results']:
            if movie.get('release_date', ''):
                fields = {
                    'movie_id': movie['id'],
                    'title' : movie['title'], 
                    'released_date': movie['release_date'],
                    'poster_path':movie['poster_path'],
                    'vote_count':movie['vote_count'],
                    'vote_average': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'genres': movie['genre_ids']
                }
                data = {
                    'pk' : movie['id'],
                    'model': 'movies.movie',
                    'fields': fields
                }

                total_data.append(data)

        with open("movies/fixtures/movie_data.json", "w", encoding="utf-8") as w:
            json.dump(total_data, w, indent="\t", ensure_ascii=False)
        
    print('데이터 저장')
        

get_movie_datas()


# Create your views here.

@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':   
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    if request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# 게시글 댓글 CRUD views

@api_view(['GET', 'PUT', 'DELETE'])
def comment_article_detail(request, comment_pk):
    comment = get_object_or_404(Comment_article, pk=comment_pk)
    
    if request.method == 'GET':
        serializer = CommentArticleSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CommentArticleSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST'])
def comment_article_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
# 영화 댓글 CRUD views
@api_view(['POST'])
def comment_movie_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = CommentMovieSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def comment_movie_detail(request, comment_pk):
    comment = get_object_or_404(Comment_movie, pk=comment_pk)
    
    if request.method == 'GET':
        serializer = CommentMovieSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CommentMovieSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
    