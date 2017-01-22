# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, _user_has_perm, \
    _user_has_module_perms
from django.utils.translation import ugettext_lazy as _

from assistant.models import Region


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, username and password.
        """
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email))

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(verbose_name=_('Имя'), max_length=30, blank=True)
    last_name = models.CharField(verbose_name=_('Фамилия'), max_length=30, blank=True)
    email = models.EmailField(verbose_name=_('Эл. адрес'), unique=True)
    date_joined = models.DateTimeField(_('Дата регистрации'), auto_now_add=True)
    is_active = models.BooleanField(verbose_name=_('Активен'), default=True)
    is_staff = models.BooleanField(verbose_name=_('Администратор'), default=False)
    region = models.ForeignKey(Region, verbose_name=_('Регион'), related_name='user_region', blank=True, null=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        # Active superusers have all permissions.
        if self.is_active and self.is_superuser:
            return True

        # Otherwise we need to check the backends.
        return _user_has_perm(self, perm, obj)

    def has_perms(self, perm_list, obj=None):
        for perm in perm_list:
            if not self.has_perm(perm, obj):
                return False
        return True

    def has_module_perms(self, app_label):
        if self.is_active and self.is_superuser:
            return True

        return _user_has_module_perms(self, app_label)

    @property
    def is_admin(self):
        return self.is_staff

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')
