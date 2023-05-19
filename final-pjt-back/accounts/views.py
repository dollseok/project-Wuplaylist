from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework.decorators import api_view

# # Create your views here.

# @api_view(['GET'])

# def follow(request, user_pk):
#     if request.method == 'GET':

#         person = get_user_model().objects.get(pk=user_pk)
#         print(person)
#         serializer = UserSerializer(data=request.data)

#         if serializer.is_valid():

#             if person != request.user:
#                 if person.followers.filter(pk=request.user.pk).exists():
#                     person.followers.remove(request.user)
#                 else:
#                     person.followers.add(request.user)
#             # print(serializer)
#             return Response(serializer.data)