from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'enseignant'),
        (2, 'étudiant'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)

    def __str__(self):
        return self.username


# Create your models here.
