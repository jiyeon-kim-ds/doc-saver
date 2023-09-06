from django.db import models

from core.models import TimeStampModel


class Article(TimeStampModel):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=1024)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    content = models.TextField()
    summary = models.CharField(max_length=255)
    category_id = models.ForeignKey("categories.Category", models.SET_NULL, blank=True, null=True,)
    is_read = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    tags = models.ManyToManyField("tags.Tag", db_constraint=True, blank=True)
