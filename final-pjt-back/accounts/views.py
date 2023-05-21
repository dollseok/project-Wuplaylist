from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

# # Create your views here.

@api_view(['GET'])
def profile(request, username):
    if request.method == 'GET':
        person = get_user_model().objects.get(username=username)
        serializer = UserSerializer(person)
        return Response(serializer.data)

@api_view(['GET'])
def get_user_detail(request, user_id):
    try:
        user = get_user_model().objects.get(pk=user_id)
        response_data = {
            'username': user.username,
        }
        print(response_data)
        return JsonResponse(response_data)
    except get_user_model().DoesNotExist:
        return JsonResponse({'error':'User not found'}, status=404)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request, username):
    if request.method == 'POST':
        person = get_user_model().objects.get(username=username)
        serializer = UserSerializer(person)

        if serializer.is_valid():
            if person != request.user:
                if person.followers.filter(pk=request.user.pk).exists():
                    person.followers.remove(request.user)
                else:
                    person.followers.add(request.user)
            return Response()