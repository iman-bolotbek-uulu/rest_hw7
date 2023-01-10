from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_sender = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

