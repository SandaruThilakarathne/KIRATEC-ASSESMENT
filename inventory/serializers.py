from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from inventory.models import Inventory, Supplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['name']


class InventorySerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(read_only=True, many=True)
    class Meta:
        model = Inventory
        fields = ['id', 'name', 'availability', 'supplier']