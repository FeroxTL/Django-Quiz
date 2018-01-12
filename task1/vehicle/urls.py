from django.conf.urls import url
from django.contrib import admin

from vehicle.views import VehicleListView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', VehicleListView.as_view()),
]
