# Generated by Django 5.0.6 on 2024-11-03 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0003_remove_baseuserprofile_displayable_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofilewriter',
            name='subscribers_counter',
        ),
    ]
