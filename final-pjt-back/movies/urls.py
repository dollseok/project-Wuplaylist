from django.urls import path
from . import views

app_name = 'movies'
urlpatterns =[
    path('movies/', views.movie_list),
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('articles/<int:article_pk>/comments/', views.comment_create),
]   