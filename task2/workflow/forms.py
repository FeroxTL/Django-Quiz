# -*- coding: utf-8 -*-
from django import forms

from workflow.models import ProcedureExecution


class ProcedureExecutionAdminForm(forms.ModelForm):
    class Meta:
        model = ProcedureExecution
        fields = (
            'employee',
            'procedure'
        )

    def _get_validation_exclusions(self):
        # Валидация полей вне зависимости от их наличия в Meta.fields
        exclude = super(ProcedureExecutionAdminForm, self)._get_validation_exclusions()
        exclude.remove('date_create')
        return exclude


class ProcedureExecutionForm(forms.ModelForm):
    class Meta:
        model = ProcedureExecution
        fields = (
            'procedure',
        )

    def _get_validation_exclusions(self):
        # Валидация полей вне зависимости от их наличия в Meta.fields
        exclude = super(ProcedureExecutionForm, self)._get_validation_exclusions()
        exclude.remove('date_create')
        exclude.remove('employee')
        return exclude
