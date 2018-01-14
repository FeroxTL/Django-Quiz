# -*- coding: utf-8 -*-
from random import randint

from django.db.transaction import atomic
from django.views.generic import ListView

from task5.models import Entry


class EntryListView(ListView):
    template_name = 'entry.html'
    queryset = Entry.objects.all()

    @atomic
    def create_entries(self):
        for x in range(5):
            Entry.objects.create()

            if randint(0, 9) == 0:
                raise Exception()

    def get_context_data(self, **kwargs):
        try:
            self.create_entries()
            success = True
        except Exception:
            success = False

        kwargs.update({
            'success': success
        })

        return super(EntryListView, self).get_context_data(**kwargs)
