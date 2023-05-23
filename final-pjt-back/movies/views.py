from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import *

from .models import *



# # 데이터 파일 제이슨으로 받기
# # 현재는 고정, 업데이트가 필요할 수도 있음
# # 런서버 할 때(프로그램이 시작될 때) 자동으로 업데이트가 되긴 함

# from django.core.exceptions import ObjectDoesNotExist

# def save_movie_data(total_data):
#     print('이건되나')
#     for data in total_data:
#         try:
#             movie = Movie.objects.get(movie_id=data['fields']['movie_id'])
#         except ObjectDoesNotExist:
#             movie = Movie(
#                 movie_id=data['fields']['movie_id'],
#                 title=data['fields']['title'],
#                 released_date=data['fields']['released_date'],
#                 poster_path=data['fields']['poster_path'],
#                 vote_count=data['fields']['vote_count'],
#                 vote_average=data['fields']['vote_average'],
#                 overview=data['fields']['overview'],
#                 genres=data['fields']['genres']
#             )
#             movie.save()


# import requests
# import json

# def get_movie_datas():
#     total_data = []

#     for i in range(1,20):
#         url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=ko-KR&page={i}&sort_by=popularity.desc"

#         headers = {
#             "accept": "application/json",
#             "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0YjNlM2FhNjVlOTZlOTVjN2Y0MWZmMDdmY2NkMzAxYiIsInN1YiI6IjYzZDMxYTM4NWEwN2Y1MDA5ZTk4MDM0YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.svzZx8RMTp1kjkBzxbvcOuoduFUJjduTqyQf-ufCBfo"
#         }

#         response = requests.get(url, headers=headers).json()

#         for movie in response['results']:
#             if movie.get('release_date', ''):
#                 poster_url = f"https://image.tmdb.org/t/p/w300{movie['poster_path']}"
            
#                 fields = {
#                     'movie_id': movie['id'],
#                     'title' : movie['title'], 
#                     'released_date': movie['release_date'],
#                     'vote_count':movie['vote_count'],
#                     'vote_average': movie['vote_average'],
#                     'overview': movie['overview'],
#                     'poster_path': movie['poster_path'],
#                     'genres': movie['genre_ids']
#                 }
#                 data = {
#                     'pk' : movie['id'],
#                     'model': 'movies.movie',
#                     'fields': fields
#                 }
#                 # poster_path 링크 누락된 부분 수정하고 데이터에 넣어주기 
#                 data['fields']['poster_path'] = poster_url
                
#                 total_data.append(data)

#     save_movie_data(total_data)
#     print('데이터 저장')
        


# Create your views here.

@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def article_list(request):
    if request.method == 'GET':   
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            serializer.save(user=request.user)
            print(serializer.data)
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

@api_view(['GET','POST'])
def comment_list_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    
    # 게시물의 댓글 조회
    if request.method == 'GET':
        comments = article.comment_article_set.all()
        serializer = CommentArticleSerializer(comments, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CommentArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)



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
   
    
# 영화 댓글 CRUD views
@api_view(['GET','POST'])
def comment_list_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    if request.method == 'GET':
        comments = movie.comment_movie_set.all()
        serializer = CommentMovieSerializer(comments, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CommentMovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user)
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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_article(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)

        if article.like_user.filter(pk=request.user.pk).exists():
            article.like_user.remove(request.user)
            
        else:
            article.like_user.add(request.user)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_comment_article(request, comment_pk):
    print('함수호출?')
    print(request.user)
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment_article, pk=comment_pk)

        if comment.like_user.filter(pk=request.user.pk).exists():
            comment.like_user.remove(request.user)
            
        else:
            comment.like_user.add(request.user)
        serializer = CommentArticleSerializer(comment)
        return Response(serializer.data)