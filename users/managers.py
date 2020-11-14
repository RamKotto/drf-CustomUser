from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Кастомная модель менеджера пользователей
    с уникальным e-mail идентификатором для аутентификации пользователей,
    вместо username.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Создание и сохранение пользователя с полученным e-mail и паролем.
        """
        if not email:
            raise ValueError(_('e-mail должен быть установлен'))
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Создаем и схраняем SuperUser с полученными e-mail и паролем.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('SuperUser должен быть "is_staff = True"'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('SuperUser должен быть "is_superuser = True"'))
        return self.create_user(email, password, **extra_fields)
