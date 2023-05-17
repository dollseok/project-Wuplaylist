from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MovieSerializer

from .models import *

import requests
import json

url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=true&language=ko-KR&page=1&sort_by=popularity.desc"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0YjNlM2FhNjVlOTZlOTVjN2Y0MWZmMDdmY2NkMzAxYiIsInN1YiI6IjYzZDMxYTM4NWEwN2Y1MDA5ZTk4MDM0YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.svzZx8RMTp1kjkBzxbvcOuoduFUJjduTqyQf-ufCBfo"
}

Movie_json_list = []
response = requests.get(url, headers=headers)

responsejson = (response.json())

print(responsejson['results'])
print(type(responsejson['results']))



# Create your views here.

@api_view(['GET'])
def movies_list(request):
    if request.method == 'GET':
        
        movies = responsejson['results']
        
        
        serializer = MovieSerializer(movies, many=True)
        # if serializer.is_valid():
        #     serializer.save()
        return Response(serializer.data)
