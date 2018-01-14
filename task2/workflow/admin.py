from django.contrib import admin

from workflow.forms import ProcedureExecutionAdminForm
from workflow.models import Procedure, ProcedureExecution


class ProcedureExecutionAdmin(admin.ModelAdmin):
    form = ProcedureExecutionAdminForm
    list_display = (
        '__str__',
        'date_create'
    )


admin.site.register(Procedure)
admin.site.register(ProcedureExecution, ProcedureExecutionAdmin)
