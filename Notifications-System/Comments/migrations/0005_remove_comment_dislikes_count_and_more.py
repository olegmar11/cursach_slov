# Generated by Django 5.0.6 on 2024-11-17 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0005_userprofilewriter_total_dislikes_counter'),
        ('Comments', '0004_alter_comment_creator_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='dislikes_count',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='likes_count',
        ),
        migrations.AddField(
            model_name='comment',
            name='dislikes',
            field=models.ManyToManyField(related_name='comm_dislikes', to='Authentication.baseuserprofile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(related_name='comm_likes', to='Authentication.baseuserprofile'),
        ),
    ]
