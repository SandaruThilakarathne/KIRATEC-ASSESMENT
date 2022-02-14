from django.test import TestCase

from inventory.models import Supplier, Inventory
from rest_framework.test import APIClient
from rest_framework import status

from django.test.client import Client
# Create your tests here.
class TestFunctionalities(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.viewclient = Client()
        self.suplier1 = Supplier.objects.create(name="test1")
        self.suplier2 = Supplier.objects.create(name="test2")
    
    def test_api_inventory(self):
        inventory = Inventory.objects.create(
            name = "test",
            description = "test",
            note = "test",
            stock = 12,
            availability = True
        )
        inventory.supplier.add(self.suplier1)
        inventory.supplier.add(self.suplier2)

        res = self.client.get("/api/inventory/")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_invenotry(self):
        inventory = Inventory.objects.create(
            name = "test",
            description = "test",
            note = "test",
            stock = 12,
            availability = True
        )
        inventory.supplier.add(self.suplier1)
        inventory.supplier.add(self.suplier2)

        res = self.viewclient.get("/inventory")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    

    def test_invenotry_id(self):
        inventory = Inventory.objects.create(
            name = "test",
            description = "test",
            note = "test",
            stock = 12,
            availability = True
        )
        inventory.supplier.add(self.suplier1)
        inventory.supplier.add(self.suplier2)

        res = self.viewclient.get(f"/inventory/{inventory.id}")
        self.assertEqual(res.status_code, status.HTTP_200_OK)