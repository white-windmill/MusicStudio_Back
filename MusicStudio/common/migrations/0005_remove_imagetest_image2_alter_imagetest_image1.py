# Generated by Django 4.0.3 on 2022-03-25 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_imagetest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagetest',
            name='image2',
        ),
        migrations.AlterField(
            model_name='imagetest',
            name='image1',
            field=models.ImageField(upload_to='img/'),
        ),
    ]
