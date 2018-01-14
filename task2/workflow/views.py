# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from workflow.forms import ProcedureExecutionForm
from workflow.models import ProcedureExecution


class ProcedureExecutionListView(ListView):
    """
    Список выполненных процедур
    """
    template_name = 'procedure_list.html'
    context_object_name = 'procedure_execution_list'

    def get_queryset(self):
        return self.request.user.procedure_executions.all().select_related('procedure')

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseForbidden(content='403 Forbidden')
        return super(ProcedureExecutionListView, self).get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs.update({
            'procedure_execution_form': ProcedureExecutionForm()
        })
        return super(ProcedureExecutionListView, self).get_context_data(**kwargs)


class ProcedureExecutionCreateView(LoginRequiredMixin, CreateView):
    """
    Отметка о выполнении процедуры
    """
    form_class = ProcedureExecutionForm
    template_name = 'procedure_execution_create_form.html'
    success_url = reverse_lazy('procedure-execution-list')

    def get_form_kwargs(self):
        user = self.request.user
        form_kwargs = super(ProcedureExecutionCreateView, self).get_form_kwargs()

        form_kwargs.update({
            'instance': ProcedureExecution(employee=user)
        })

        return form_kwargs
