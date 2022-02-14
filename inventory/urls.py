from rest_framework import routers
from inventory.views import InventoryViewSet, Inventories, single_inventory

from django.urls import path

router = routers.DefaultRouter()
router.register(r'api/inventory', InventoryViewSet)

urlpatterns = [
    path('inventory', Inventories.as_view(), name='inventory'),
    path('inventory/<int:id>', single_inventory, name='single_inventory'),
]

urlpatterns += router.urls