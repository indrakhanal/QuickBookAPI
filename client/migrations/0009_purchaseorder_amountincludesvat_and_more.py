# Generated by Django 4.1.6 on 2023-02-24 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0008_purchaseorder_alter_customer_accountnumber_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='AmountIncludesVAT',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='CurrencyRefFullName',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='CurrencyRefListID',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='CustomFieldOther1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='CustomFieldOther2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='ExchangeRate',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='FOB',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='IsFullyReceived',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='IsManuallyClosed',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='IsTaxIncluded',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='IsToBeEmailed',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='IsToBePrinted',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='Memo',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='SalesTaxCodeRefFullName',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='SalesTaxCodeRefListID',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='ShipMethodRefFullName',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='Status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='Tax1Total',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='Tax2Total',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='TaxCodeRefFullName',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='TaxCodeRefListID',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='TotalAmount',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='TotalAmountInHomeCurrency',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='VendorMsg',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='salesorderitems',
            name='Status',
            field=models.BooleanField(default=False),
        ),
    ]
