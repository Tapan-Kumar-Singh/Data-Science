# Generated by Django 4.1.4 on 2023-01-03 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_articlesource_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=30)),
                ('topic', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=60)),
                ('short_description', models.CharField(max_length=500)),
                ('highlight', models.TextField(blank=True)),
                ('body', models.TextField(blank=True)),
                ('link', models.SlugField(blank=True, max_length=250, null=True)),
                ('authors', models.CharField(max_length=60)),
                ('location', models.CharField(max_length=60)),
                ('add_to', models.CharField(max_length=60)),
                ('published', models.CharField(max_length=60)),
                ('meta_title', models.TextField()),
                ('meta_description', models.TextField()),
                ('article_source', models.CharField(max_length=50)),
            ],
        ),
    ]
