
from django.urls import path, include
from .views import *
from rest_framework import routers
router = routers.DefaultRouter()
router.register('v1/customer', CustomerDetailView, 'customer')
router.register('v1/vendor', VendorDetailView, 'vendor')
router.register('v1/sales-order', SalesOrderDetailView, 'sales-order')
router.register('v1/sales-order-item', SalesOrderItemsDetailView, 'sales-order-item')
router.register('v1/purchase-order', PurchaseOrderDetailView, 'purchase-order')
router.register('v1/purchase-order-item', PurchaseOrderItemsDetailView, 'purchase-order-item')
router.register('v1/item-inventory', ItemInventoryDetailView, 'item-inventory')
router.register('v1/invoice', InvoiceDetailView, 'invoice')



app_name = 'client'


urlpatterns = [
    path('', include(router.urls)),
    path('v1/all-customer/', GetAllCostumerList.as_view(), name="all-custome"),
    path('v1/shipaddress/', ShipAddressCreateView.as_view(), name="shipaddress"),
    path('v1/shipaddress/all/', ShipAddressListView.as_view(), name="shipaddress-all"),
    path('v1/shipaddress/<str:ListID>/<str:Category>/delete/', ShipAddressDeleteView.as_view(), name="shipaddress-delete"),
]