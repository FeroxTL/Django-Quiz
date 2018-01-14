from django.db import models


class LogEntry(models.Model):
    ip = models.GenericIPAddressField(null=True)
    url = models.URLField(blank=True)
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '[{}, {}] {}'.format(self.date_create, self.ip or 'local', self.url)
