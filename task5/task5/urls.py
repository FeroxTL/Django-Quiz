from django.conf.urls import url
from django.contrib import admin

from task5.views import EntryListView


urlpatterns = [
    url(r'^$', EntryListView.as_view()),
    url(r'^admin/', admin.site.urls),
]
