from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework.decorators import api_view

# # Create your views here.

@api_view(['GET'])
def profile(request, username):
    if request.method == 'GET':
        person = get_user_model().objects.get(username=username)
        serializer = UserSerializer(person)
        return Response(serializer.data)
    

@api_view(['GET'])
def follow(request, username):
    if request.method == 'GET':

        person = get_user_model().objects.get(username=username)
        serializer = UserSerializer(person)

        if serializer.is_valid():

            if person != request.user:
                if person.followers.filter(pk=request.user.pk).exists():
                    person.followers.remove(request.user)
                else:
                    person.followers.add(request.user)

            return Response(serializer.data)