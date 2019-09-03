from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import validate_email


class User(AbstractUser):
    email = models.EmailField(('Email'), blank=True, null=True, unique=True, validators=[validate_email])
    modified_at = models.DateTimeField('modified at', default=timezone.now)