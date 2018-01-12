# -*- coding: utf-8 -*-
from django.views.generic import ListView

from vehicle.models import Vehicle


class VehicleListView(ListView):
    template_name = 'vehicle_list.html'
    queryset = Vehicle.objects.all()
