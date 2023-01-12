from django.db import models


# Create your models here.
class UserRoll(models.Model):
    role_name = models.CharField(max_length=30)

    def __str__(self):
        return self.role_name


class Language(models.Model):
    language_name = models.CharField(max_length=30)

    def __str__(self):
        return self.language_name


class ArticleSource(models.Model):
    source_name = models.CharField(max_length=30)

    def __str__(self):
        return self.source_name


class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name


class AllUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_id = models.CharField(max_length=60)
    contact_number = models.CharField(max_length=60)
    roll = models.CharField(max_length=60)

    def __str__(self):
        return self.first_name


class Article(models.Model):
    language = models.CharField(max_length=30)
    image_one = models.ImageField(upload_to='images/', blank=True)
    image_two = models.ImageField(upload_to='images/', blank=True)
    topic = models.CharField(max_length=100)
    title = models.CharField(max_length=60)
    short_description = models.CharField(max_length=500)
    highlight = models.TextField(blank=True)
    body = models.TextField(blank=True)
    category = models.CharField(max_length=30, blank=True)
    link = models.SlugField(max_length=250, null=True, blank=True)
    authors = models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    add_to = models.CharField(max_length=60)
    published = models.CharField(max_length=60)
    meta_title = models.TextField()
    meta_description = models.TextField()
    article_source = models.CharField(max_length=50)

    def __str__(self):
        return self.topic



