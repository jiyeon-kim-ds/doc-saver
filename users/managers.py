from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not username:
            raise ValueError("User must have a first name")

        user = self.model(
            email=self.normalize_email(email)
        )

        user.username = username
        user.set_password(password)
        user.save(using=self._db)

        return user
