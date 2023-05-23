from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    # username은 가입 시 아이디와 같다
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    introduce = models.TextField(null=True)
    nickname = models.CharField(max_length=30)
    
    
