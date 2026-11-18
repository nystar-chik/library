from django.contrib.auth.models import UserManager as BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, phone, password=None, **extra_fields):

        user = self.model(
            phone=phone,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, phone, password=None, **extra_fields):

        user = self.create_user(
            phone=phone,
            password=password,
            **extra_fields
        )

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user