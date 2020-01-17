from django.db import models

# Create your models here.
from members.models import User


class Thread(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(
        'Tag', verbose_name='해시태그 목록', related_name='threads', blank=True,
    )
    like_users = models.ManyToManyField(User, through='PostLike', related_name='like_threads_set', )
    threads = models.ManyToManyField(
        'self', related_name='ThreadOrigin', symmetrical=False, blank=True, null=True,
    )


class Tag(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class PostLike(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class Image(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='threads/image')
