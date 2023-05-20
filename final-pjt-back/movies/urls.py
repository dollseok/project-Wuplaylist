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
    # 게시글 댓글 상세 조회, 수정, 삭제 
    path('comments_article/<int:comment_pk>/', views.comment_article_detail),
    # 게시글 댓글 리스트 조회, 생성
    path('articles/<int:article_pk>/comments_article/', views.comment_list_article),
    

    # 영화 댓글 CRUD url
    # 영화 댓글 상세 조회, 수정, 삭제
    path('comments_movie/<int:comment_pk>/', views.comment_movie_detail),
    # 영화 댓글 리스트 조회, 생성
    path('movies/<int:movie_pk>/comments_movie/', views.comment_list_movie),
    
]   