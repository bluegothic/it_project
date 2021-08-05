# Generated by Django 3.1.5 on 2021-08-05 19:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='author_id',
            field=models.CharField(default='Moon', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='choice1',
            field=models.CharField(default='cola', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='choice2',
            field=models.CharField(default='coco', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='choice3',
            field=models.CharField(default='water', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='context',
            field=models.CharField(default='Which one would you buy?', max_length=512),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='count1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='count2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='count3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='posttime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
