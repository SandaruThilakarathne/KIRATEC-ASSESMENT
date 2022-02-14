from django.contrib import admin
from inventory.models import Inventory, Supplier

# Register your models here.
class InventoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
            {'fields': 
                [
                    'name',
                    'description',
                    'note',
                    'stock',
                    'availability',
                    'supplier'
                ]
            }
        )
    ]

class SupplierAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
            {'fields': 
                [
                    'name'
                ]
            }
        )
    ]

admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Supplier, SupplierAdmin)