# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Vehicle(models.Model):
    """
    Транспортное средство
    """

    CATEGORY_CHOICES = [
        ('A', 'Мотоцикл'),
        ('B', 'Легковая'),
        ('C', 'Грузовая'),
        ('D', 'Автобус')
    ]

    name = models.CharField(
        'Название',
        max_length=300
    )
    category = models.CharField(
        'Категория',
        max_length=1,
        choices=CATEGORY_CHOICES
    )
    date_create = models.DateTimeField(
        'Дата создания',
        auto_now_add=True,
        editable=False,
        db_index=True
    )

    class Meta:
        verbose_name = 'транспортное средство'
        verbose_name_plural = 'транспортные средства'
        ordering = ('date_create',)

    def __str__(self):
        return self.name
