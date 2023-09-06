from django.db import models

from core.models import TimeStampModel


class Category(TimeStampModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
