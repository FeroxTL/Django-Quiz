# -*- coding: utf-8 -*-
from logging import Handler
from django.apps import apps
from django.core.exceptions import ImproperlyConfigured


class DBHandler(Handler):
    """
    Логгер для записи событий в бд
    """

    def __init__(self, model_name=''):
        super(DBHandler, self).__init__()

        if not model_name:
            raise ImproperlyConfigured('No model_name in DBHandler conf')

        self.model_name = model_name

    def emit(self, record):
        model_class = apps.get_model(self.model_name)

        try:
            request = record.request
            ip = request.META.get('REMOTE_ADDR')
            url = request.path
        except Exception:
            url = ''
            ip = None

        model_class.objects.create(ip=ip, url=url)
