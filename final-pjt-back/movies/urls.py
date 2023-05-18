from django.urls import path
from . import views

app_name = 'movies'
urlpatterns =[
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail)
    
]