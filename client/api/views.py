from rest_framework import viewsets
from client.models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import filters
from rest_framework.schemas import AutoSchema
from django_filters.rest_framework import DjangoFilterBackend
import coreapi
import coreschema
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from rest_framework.compat import coreapi
from django.shortcuts import get_object_or_404

class CustomerDetailView(viewsets.ModelViewSet):
    fields = '__all__'
    serializer_class = CustomerDataSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ListID', 'Name']
    queryset = Customer.objects.all()

    schema = AutoSchema(
        manual_fields=[
            coreapi.Field(
                "search",
                required=False,
                location='query',
                schema=coreschema.String(
                    title='Search',
                    description='Search by name or list_id',
                ),
            ),
        ]
    )

    def get_queryset(self, *args, **kwargs):
        name = self.request.GET.get("Name")
        list_id = self.request.GET.get("ListID")
        if name and list_id:
            qs =  Customer.objects.filter(Q(Status=False) & (Q(Name__icontains=name) | Q(ListID__icontains=list_id)))
        if name and not list_id:
            qs =  Customer.objects.filter(Q(Status=False) & Q(Name__icontains=name))
        if not name and list_id:
            qs =  Customer.objects.filter(Q(Status=False) & Q(ListID__icontains=list_id))
        if not name and not list_id:
            qs = Customer.objects.filter(Status=False)
        return qs


    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class VendorDetailView(viewsets.ModelViewSet):
    fields = '__all__'
    serializer_class = VendorrDataSerializer
    queryset = Vendor.objects.all()
   

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class SalesOrderDetailView(viewsets.ModelViewSet):
    fields = '__all__'
    serializer_class = SalesOrderDataSerializer
    queryset = SalesOrder.objects.all()
   

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class SalesOrderItemsDetailView(viewsets.ModelViewSet):
    fields = '__all__'
    serializer_class = SalesOrderItemsDataSerializer
    queryset = SalesOrderItems.objects.all()
   

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    

class PurchaseOrderDetailView(viewsets.ModelViewSet):
    fields = '__all__'
    serializer_class = PurchaseOrderDataSerializer
    queryset = PurchaseOrder.objects.all()
   

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    

class PurchaseOrderItemsDetailView(viewsets.ModelViewSet):
    fields = '__all__'
    serializer_class = PurchaseOrderItemsDataSerializer
    queryset = PurchaseOrderItems.objects.all()
   

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    

class ItemInventoryDetailView(viewsets.ModelViewSet):
    fields = '__all__'
    serializer_class = ItemInventoryDataSerializer
    queryset = ItemInventory.objects.all()
   

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    

class InvoiceDetailView(viewsets.ModelViewSet):
    fields = '__all__'
    serializer_class = InvoiceDataSerializer
    queryset = Invoice.objects.all()
   

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
        

class GetAllCostumerList(generics.ListAPIView):
    """
    API to return all list of costumer data
    """
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ListID', 'Name']
    serializer_class = GetAllCostumerListSerializer
    

    def get_queryset(self, *args, **kwargs):
        name = self.request.GET.get("Name")
        list_id = self.request.GET.get("ListID")
        if name and list_id:
            qs =  Customer.objects.filter((Q(Name__icontains=name) | Q(ListID__icontains=list_id))).order_by("Name")
        if name and not list_id:
            qs =  Customer.objects.filter(Q(Name__icontains=name)).order_by("Name")
        if not name and list_id:
            qs =  Customer.objects.filter(Q(ListID__icontains=list_id)).order_by("Name")
        if not name and not list_id:
            qs  = Customer.objects.filter(Status=False)
        return qs

class ShipAddressCreateView(generics.CreateAPIView):
    queryset = ShipAddress.objects.all()
    serializer_class = ShipAddressSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    

class ShipAddressDeleteView(generics.DestroyAPIView):
    queryset = ShipAddress.objects.all()
    serializer_class = ShipAddressSerializer
    filter_backends = [DjangoFilterBackend]
    lookup_fields  = ('ListID', 'Category')

    def get_object(self):
        queryset = self.get_queryset()
        filter_kwargs = {}
        for field in self.lookup_fields:
            if field in self.kwargs:
                filter_kwargs[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj

class ShipAddressListView(generics.ListAPIView):
    queryset = ShipAddress.objects.all()
    serializer_class = ShipAddressSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Status']

    def get_queryset(self):
        status = self.request.GET.get('Status')
        if status == 'True':
            qs  = ShipAddress.objects.filter(Status=True)
        if status == 'False':
            qs = ShipAddress.objects.filter(Status=False)
        else:
            qs = ShipAddress.objects.all()
        return qs



    



