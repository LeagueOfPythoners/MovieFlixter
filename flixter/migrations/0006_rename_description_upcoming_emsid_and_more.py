# Generated by Django 4.1.7 on 2023-02-22 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flixter', '0005_remove_topten_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='upcoming',
            old_name='description',
            new_name='emsId',
        ),
        migrations.RemoveField(
            model_name='upcoming',
            name='file',
        ),
        migrations.AddField(
            model_name='upcoming',
            name='date',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='upcoming',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
    ]