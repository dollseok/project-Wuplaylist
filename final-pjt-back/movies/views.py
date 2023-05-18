from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MovieSerializer

from .models import *

import requests
import json

# 데이터 파일 제이슨으로 받기
# 현재는 고정, 업데이트가 필요할 수도 있음
# 런서버 할 때(프로그램이 시작될 때) 자동으로 업데이트가 되긴 함
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

# @api_view(['GET'])
# def movies_list(request):
#     if request.method == 'GET':   
#         return