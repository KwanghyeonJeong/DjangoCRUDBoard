# Generated by Django 2.1.15 on 2021-02-17 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answerreply',
            name='unique_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='unique_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reply',
            name='unique_number',
            field=models.IntegerField(default=0),
        ),
    ]
