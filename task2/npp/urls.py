from django.conf.urls import url
from django.contrib import admin

from workflow.views import ProcedureExecutionListView, ProcedureExecutionCreateView

urlpatterns = [
    url(r'^$', ProcedureExecutionListView.as_view(), name='procedure-execution-list'),
    url(r'^procedure-execution-create/$', ProcedureExecutionCreateView.as_view(), name='procedure-execution-create'),
    url(r'^admin/', admin.site.urls),
]
