# Generated by Django 2.2.9 on 2020-01-17 07:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('counterpart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='counterpart_relation_set', to=settings.AUTH_USER_MODEL)),
                ('me', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='me_relation_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(related_name='followers', through='members.Relation', to=settings.AUTH_USER_MODEL),
        ),
    ]
