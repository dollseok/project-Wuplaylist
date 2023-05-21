from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns =[
    path('detail/<int:user_id>/',views.get_user_detail, name='user_detail'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('profile/<str:username>/follow/', views.follow, name='follow'),
]