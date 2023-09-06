from django.db import models

from core.models import TimeStampModel


class Tag(TimeStampModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="user")
    name = models.CharField(max_length=255)
