# Generated by Django 4.0.4 on 2022-04-25 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_category_news_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='url',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='url',
            field=models.SlugField(null=True),
        ),
    ]
