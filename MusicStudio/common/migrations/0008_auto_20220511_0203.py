# Generated by Django 3.2.13 on 2022-05-11 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_playlist_playlistimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='articlepic1',
            field=models.ImageField(default='', upload_to='img/'),
        ),
        migrations.AddField(
            model_name='article',
            name='articlepic2',
            field=models.ImageField(default='', upload_to='img/'),
        ),
        migrations.AddField(
            model_name='article',
            name='articlepic3',
            field=models.ImageField(default='', upload_to='img/'),
        ),
    ]
