from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    """
    사용자 모델로 쓰입니다.
    """
    img_profile = models.ImageField('프로필이미지', blank=True, upload_to='user_profile_image/')
    name = models.CharField('이름', max_length=100)
    following = models.ManyToManyField('self', through='Relation', related_name='followers', symmetrical=False, )


class Relation(models.Model):
    me = models.ForeignKey(User, related_name='me_relation_set', on_delete=models.CASCADE)
    counterpart = models.ForeignKey(User, related_name='counterpart_relation_set', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)