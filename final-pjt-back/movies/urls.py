from django.urls import path
from . import views

app_name = 'movies'
urlpatterns =[
    # 영화 데이터 조회
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    
    # 게시글 CRUD url
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    
    # 게시글 댓글 CRUD url
    path('comments_article/<int:comment_pk>/', views.comment_article_detail),
    path('articles/<int:article_pk>/comments_article/', views.comment_article_create),

    # 영화 댓글 CRUD url
    path('comments_movie/<int:comment_pk>/', views.comment_movie_detail),
    path('movies/<int:movie_pk>/comments_movie/', views.comment_movie_create),
]   