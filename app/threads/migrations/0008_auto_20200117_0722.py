# Generated by Django 2.2.9 on 2020-01-17 07:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('threads', '0007_auto_20200117_0317'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostLike',
            new_name='ThreadLike',
        ),
    ]
