from django.contrib import admin
from .models import Customer, Vendor, SalesOrder, SalesOrderItems, PurchaseOrder, PurchaseOrderItems, ShipAddress

# Register your models here.
admin.site.register(Customer)
admin.site.register(Vendor)
admin.site.register(SalesOrder)
admin.site.register(SalesOrderItems)
admin.site.register(PurchaseOrder)
admin.site.register(PurchaseOrderItems)
admin.site.register(ShipAddress)




