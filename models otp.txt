from django.db import models
from django.contrib.auth.models import AbstractUser
from account.manager import UserManager
from datetime import timedelta
from django.utils import timezone

class User(AbstractUser):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    phone = models.CharField(
        max_length=20,
        blank=True, 
        unique=True
    )

    avatar = models.ImageField(
        upload_to='static',
        blank=True,
        null=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['first_name', 'username']

class OTPCode(models.Model):
    class Meta:
        verbose_name = 'OTPCode'
        verbose_name_plural = 'OTPCodes'

    email = models.EmailField()
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.expired_at:
            self.expired_at = timezone.now() + timedelta(minutes=5)
        super().save(*args, **kwargs)

    def is_expired(self):
        return timezone.now() > self.expired_at
    
    def __str__(self):
        return self.email
    