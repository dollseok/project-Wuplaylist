from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns =[
    path('signup/', views.signup),
    # user detail을 가져오는 url
    path('detail/<int:user_id>/',views.get_user_detail, name='user_detail'),
    #  프로필 링크
    path('profile/<str:username>/', views.profile, name='profile'),
    # 팔로우 기능 
    path('profile/<str:username>/follow/', views.follow, name='follow'),
]