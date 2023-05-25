import requests
import json
from django.core.exceptions import ObjectDoesNotExist
from .models import *

# 데이터 파일 제이슨으로 받기
# 현재는 고정, 업데이트가 필요할 수도 있음
# 런서버 할 때(프로그램이 시작될 때) 자동으로 업데이트가 되긴 함

def save_movie_data(total_data):
    print('이건되나')
    for data in total_data:
        try:
            movie = Movie.objects.filter(movie_id=data['fields']['movie_id'])
        except ObjectDoesNotExist:
            movie = Movie(
                movie_id=data['fields']['movie_id'],
                title=data['fields']['title'],
                released_date=data['fields']['released_date'],
                poster_path=data['fields']['poster_path'],
                vote_count=data['fields']['vote_count'],
                vote_average=data['fields']['vote_average'],
                overview=data['fields']['overview'],
                genres=data['fields']['genres']
            )
            movie.save()




def get_movies_data():
    total_data = []

    for i in range(1,8):
        url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=ko-KR&page={i}&sort_by=popularity.desc"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0YjNlM2FhNjVlOTZlOTVjN2Y0MWZmMDdmY2NkMzAxYiIsInN1YiI6IjYzZDMxYTM4NWEwN2Y1MDA5ZTk4MDM0YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.svzZx8RMTp1kjkBzxbvcOuoduFUJjduTqyQf-ufCBfo"
        }

        response = requests.get(url, headers=headers).json()

        for movie in response['results']:
            if movie.get('release_date', ''):
                poster_url = f"https://image.tmdb.org/t/p/w300{movie['poster_path']}"
            
                fields = {
                    'movie_id': movie['id'],
                    'title' : movie['title'], 
                    'released_date': movie['release_date'],
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
                # poster_path 링크 누락된 부분 수정하고 데이터에 넣어주기 
                data['fields']['poster_path'] = poster_url
                
                total_data.append(data)

    save_movie_data(total_data)
    print('데이터 저장')

def save_genre_data(total_genre):
    for data in total_genre:
        try:
            genre = Genre.objects.filter(genre_id = data['fields']['genre_id'])
        except ObjectDoesNotExist:
            genre = Genre(
                genre_id = data['fields']['genre_id'],
                genre_name = data['fields']['genre_name'],
            )
            genre.save()

def get_genres_data():
    # genres_data = []
    url = "https://api.themoviedb.org/3/genre/movie/list?language=ko"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0YjNlM2FhNjVlOTZlOTVjN2Y0MWZmMDdmY2NkMzAxYiIsInN1YiI6IjYzZDMxYTM4NWEwN2Y1MDA5ZTk4MDM0YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.svzZx8RMTp1kjkBzxbvcOuoduFUJjduTqyQf-ufCBfo"
    }

    response = requests.get(url, headers=headers).json()
    
    total_genre=[]
    
    for genre in response['genres']:
        fields= {
            'genre_id': genre['id'],
            'genre_name':genre['name'],
        }
        data = {
            'fields':fields
        }
        
        total_genre.append(data)
    
    save_genre_data(total_genre)
    print('장르 저장')

from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta

def start():

    scheduler = BackgroundScheduler()
    scheduler.add_job(get_genres_data, 'interval', hours=1, start_date=datetime.now())
    scheduler.add_job(get_movies_data, 'interval', hours=1, start_date=datetime.now())
    
    # # 시작할 때는 바로 저장
    scheduler.add_job(get_genres_data, 'date', run_date=datetime.now())
    scheduler.add_job(get_movies_data, 'date', run_date=datetime.now())
    # # 후에는 네시간에 한번
    # scheduler.add_job(get_movies_data, 'interval', hours=4, start_date=datetime.now() +timedelta(hours=4))
    
    scheduler.start()
    