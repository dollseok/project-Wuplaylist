from django.urls import path
from . import views

app_name = 'movies'
urlpatterns =[
    path('articles/', views.article_list),

    
]