# Generated by Django 4.1.7 on 2023-02-22 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flixter', '0008_movie_date_movie_image_movie_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='categories',
        ),
        migrations.AddField(
            model_name='movie',
            name='emsId',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='movie',
            name='tags',
        ),
        migrations.AlterField(
            model_name='topten',
            name='emsId',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='topten',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='upcoming',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.AddField(
            model_name='movie',
            name='tags',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='topten',
            name='tags',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='upcoming',
            name='tags',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
