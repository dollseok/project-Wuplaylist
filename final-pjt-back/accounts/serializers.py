from rest_framework import serializers
from django.contrib.auth import get_user_model


from movies.serializers import *

from .models import User


class UserSerializer(serializers.ModelSerializer):
    # followers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    article_set = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id','username', 'password', 'nickname', 'followings', 'followers', 'introduce', 'article_set',)
        read_only_fields = ('followings', 'followers',)
