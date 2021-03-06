# Generated by Django 3.2.13 on 2022-05-26 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0009_alter_playlist_musicid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='articlepic1',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='article',
            name='articlepic2',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='article',
            name='articlepic3',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='musicid',
            field=models.ForeignKey(default='-1', on_delete=django.db.models.deletion.DO_NOTHING, to='common.music'),
        ),
    ]
