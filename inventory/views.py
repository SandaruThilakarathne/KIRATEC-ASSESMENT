from re import sub
from django.shortcuts import render
from rest_framework import viewsets, filters
from django.views.generic import TemplateView

from inventory.models import Inventory

from inventory.serializers import InventorySerializer

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class Inventories(TemplateView):
    template_name = 'inventories.html'


def single_inventory(request, id):
    inventory = Inventory.objects.filter(id=id).first()
    supplier = []
    if inventory:
        for item in  inventory.supplier.all():
            supplier.append(item.name)

    data = {
        "name": inventory.name,
        "description": inventory.description, 
        "note":  inventory.note,
        "stock": inventory.stock,
        "availability": inventory.availability,
        "supplier": ','.join(supplier)
    }
    context={
    'inventory':data
    }
    return render(request, "single-inventory.html", context)