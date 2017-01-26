# coding= utf-8
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.db import models

from main import settings
from main.choices import DOCUMENT_CHOICES, DOCUMENT_STATUS


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='post', verbose_name=_('Пользователь'))
    title = models.CharField(max_length=90, verbose_name=_('Заголовок'), blank=True, null=True)
    text = models.TextField(verbose_name=_('Текст'), blank=True, null=True)
    created_date = models.DateTimeField(verbose_name=_('Дата создание'), auto_now=True, blank=True, null=True)
    edited_at = models.CharField(verbose_name=_('Кем редактирован'), max_length=50, blank=True, null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _('Запись')
        verbose_name_plural = _('Записи')


class Region(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Название'))

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Регион')
        verbose_name_plural = _('Регионы')


class Document(models.Model):
    post = models.ForeignKey(Post, related_name='document_post', verbose_name=_('Запись'))
    type = models.CharField(choices=DOCUMENT_STATUS, max_length=50, verbose_name=_('Тип'))
    is_active = models.BooleanField(verbose_name=_('Активность'), default=False)
    type_document = models.CharField(choices=DOCUMENT_CHOICES, max_length=100, verbose_name=_('Вид документа'))
    place = models.ForeignKey(Region, verbose_name=_('Регион'), related_name='document_region')

    def __unicode__(self):
        return self.post.title

    class Meta:
        verbose_name = _('Документ')
        verbose_name_plural = _('Документы')