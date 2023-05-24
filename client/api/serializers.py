from rest_framework import serializers
from client.models import *
from rest_framework.response import Response
from rest_framework import status

class CustomerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields = '__all__'

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        return super().create(validated_data)
    
    def to_representation(self, instance):
        return super().to_representation(instance)
        


class VendorrDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vendor
        fields = '__all__'

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        return super().create(validated_data)


class SalesOrderDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=SalesOrder
        fields = '__all__'

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        return super().create(validated_data)


class SalesOrderItemsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=SalesOrderItems
        fields = '__all__'

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        return super().create(validated_data)
    


class PurchaseOrderDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=PurchaseOrder
        fields = '__all__'

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        return super().create(validated_data)
    

class PurchaseOrderItemsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=PurchaseOrderItems
        fields = '__all__'

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        return super().create(validated_data)
    
    

class ItemInventoryDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=ItemInventory
        fields = '__all__'

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        return super().create(validated_data)
    

    
class InvoiceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Invoice
        fields = '__all__'

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        return super().create(validated_data)
    

class GetAllCostumerListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields = '__all__'

    
    # Set filter_fields to be used by swagger
    def get_serializer(self, *args, **kwargs):
        serializer_class = super().get_serializer(*args, **kwargs)
        serializer_class.Meta.filter_fields = serializer_class.Meta.model.get_filter_fields()
        return serializer_class
    

class ShipAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipAddress
        fields = '__all__'

    def validate(self, attrs):
        address = attrs.get("ShipAddress") 
        category = attrs.get("Category")
        if ShipAddress.objects.filter(ShipAddress=address, Category=category).exists():
            raise serializers.ValidationError("This Data already exist")
        return super().validate(attrs)

    # Set filter_fields to be used by swagger
    def get_serializer(self, *args, **kwargs):
        serializer_class = super().get_serializer(*args, **kwargs)
        serializer_class.Meta.filter_fields = serializer_class.Meta.model.get_filter_fields()
        return serializer_class