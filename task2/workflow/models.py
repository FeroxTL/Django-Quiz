# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Procedure(models.Model):
    """
    Процедура, проводимая сотрудниками АЭС
    """
    name = models.CharField(
        'Название',
        max_length=300
    )

    class Meta:
        verbose_name = 'процедура'
        verbose_name_plural = 'процедуры'

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class ProcedureExecution(models.Model):
    """
    Процедура, выполненная сотрудником АЭС
    """
    employee = models.ForeignKey(
        User,
        verbose_name='Сотрудник',
        related_name='procedure_executions'
    )
    procedure = models.ForeignKey(
        Procedure,
        verbose_name='Процедура',
        related_name='executions'
    )
    date_create = models.DateField(
        'Дата создания',
        default=now
    )
    datetime_create = models.DateTimeField(
        'Дата и время создания',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'выполненная процедура'
        verbose_name_plural = 'выполненные процедуры'
        unique_together = (('employee', 'procedure', 'date_create'),)
        ordering = ('-datetime_create',)

    def __str__(self):
        return '{}: {} ({})'.format(self.date_create, self.employee, self.procedure)
