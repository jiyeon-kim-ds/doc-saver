from django.db import models

from core.models import TimeStampModel


class Article(models.Model, TimeStampModel):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=1024)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    content = models.TextField()
    summary = models.CharField(max_length=255)
    category_id = models.ForeignKey('articles.Category', models.SET_NULL, blank=True, null=True,)
    tag_id = models.ForeignKey('articles.Tag', models.SET_NULL, blank=True, null=True, )
    is_read = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    tags = models.ManyToManyField("articles.Tag", db_table="articles_tags", db_constraint=True)


class Category(models.Model, TimeStampModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class Tag(models.Model, TimeStampModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    