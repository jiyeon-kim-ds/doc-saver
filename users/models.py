from django.db                  import models
from django.db.models.fields    import BooleanField
from django.contrib.auth.models import AbstractBaseUser

from core.models    import TimeStampModel
from users.managers import UserManager


class User(AbstractBaseUser, TimeStampModel):
    username = models.CharField(max_length=255)
    email = models.EmailField(db_index=True, unique=True)
    is_active = BooleanField(default=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()
