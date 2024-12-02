# Generated by Django 5.0.2 on 2024-02-29 11:09

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PostTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_image', models.ImageField(default='story_fis/default_story.jpeg', upload_to='story_fis/')),
                ('post_title', models.CharField(default='No Name', max_length=50)),
                ('post_text', models.TextField()),
                ('post_description', models.CharField(default='No Description', max_length=100)),
                ('comments_count', models.PositiveBigIntegerField(default=0)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('likes_count', models.PositiveBigIntegerField(default=0)),
                ('dislikes_count', models.PositiveBigIntegerField(default=0)),
                ('views_counter', models.PositiveBigIntegerField(default=0)),
                ('creator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.userprofilewriter')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Stories.postgenre')),
                ('tags', models.ManyToManyField(to='Stories.posttags')),
            ],
        ),
        migrations.CreateModel(
            name='UserLikedPosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posts', models.ManyToManyField(to='Stories.post')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.userprofilereader')),
            ],
        ),
        migrations.CreateModel(
            name='UserViewedPosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posts', models.ManyToManyField(to='Stories.post')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.userprofilereader')),
            ],
        ),
    ]
