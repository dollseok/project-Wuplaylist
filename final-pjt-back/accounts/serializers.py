from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import User

class UserSerializer(serializers.ModelSerializer):
    # followers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = get_user_model()
        fields = ('id','username', 'password', 'nickname', 'followings', 'followers', 'introduce',)
        read_only_fields = ('followings', 'followers',)
