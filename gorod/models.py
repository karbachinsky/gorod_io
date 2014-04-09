from django.db import models
from django.contrib.auth.models import User

#from tinymce.models import HTMLField
from ckeditor.fields import RichTextField

import validators


class City(models.Model):
    """ City class """
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    add_date = models.DateTimeField()
    wallpaper = models.ImageField(max_length=255, upload_to='wallpapers/', default='')

    def __unicode__(self):
        return self.name


class CityInfo(models.Model):
    """ Module About or city info """
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    text = RichTextField(max_length=25000)


class ArticleRubric(models.Model):
    """ ArticleRubric class """
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    """ Article class """
    title = models.CharField(max_length=255)
    add_date = models.DateTimeField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    rubric = models.ForeignKey(ArticleRubric, default=1)
    user = models.ForeignKey(User) 
    picture = models.ImageField(max_length=255, upload_to='pictures/', default='', blank=True)
    #text = models.TextField()
    text = RichTextField()
    #text = HTMLField()

    def __unicode__(self):
        return self.title


class Organization(models.Model):
    """ City organization class """
    add_date = models.DateTimeField()
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    logo = models.ImageField(max_length=255, upload_to='organizations/', default='', blank=True)
    user = models.ForeignKey(User)
    description = RichTextField(max_length=10000)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    web_site = models.URLField(blank=True)
    map_link = models.CharField(blank=True, max_length=255)

    def __unicode__(self):
        return self.name


