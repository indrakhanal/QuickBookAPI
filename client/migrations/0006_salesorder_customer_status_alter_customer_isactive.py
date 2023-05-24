# Generated by Django 4.1.6 on 2023-02-23 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_vendor'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesOrder',
            fields=[
                ('TxnID', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('TimeCreated', models.CharField(blank=True, max_length=255, null=True)),
                ('TimeModified', models.CharField(blank=True, max_length=255, null=True)),
                ('EditSequence', models.CharField(blank=True, max_length=255, null=True)),
                ('TxnNumber', models.CharField(blank=True, max_length=255, null=True)),
                ('CustomerRefListID', models.CharField(blank=True, max_length=255, null=True)),
                ('CustomerRefFullName', models.CharField(blank=True, max_length=255, null=True)),
                ('ClassRefListID', models.CharField(blank=True, max_length=255, null=True)),
                ('ClassRefFullName', models.CharField(blank=True, max_length=255, null=True)),
                ('TemplateRefListID', models.CharField(blank=True, max_length=255, null=True)),
                ('TemplateRefFullName', models.CharField(blank=True, max_length=255, null=True)),
                ('TxnDate', models.CharField(blank=True, max_length=255, null=True)),
                ('TxnDateMacro', models.CharField(blank=True, max_length=255, null=True)),
                ('RefNumber', models.CharField(blank=True, max_length=255, null=True)),
                ('BillAddressAddr1', models.CharField(blank=True, max_length=255, null=True)),
                ('BillAddressAddr2', models.CharField(blank=True, max_length=255, null=True)),
                ('BillAddressAddr3', models.CharField(blank=True, max_length=255, null=True)),
                ('BillAddressAddr4', models.CharField(blank=True, max_length=255, null=True)),
                ('BillAddressAddr5', models.CharField(blank=True, max_length=255, null=True)),
                ('BillAddressCity', models.CharField(blank=True, max_length=255, null=True)),
                ('BillAddressState', models.CharField(blank=True, max_length=255, null=True)),
                ('BillAddressProvince', models.CharField(blank=True, max_length=255, null=True)),
                ('BillAddressPostalCode', models.CharField(blank=True, max_length=255, null=True)),
                ('BillAddressCountry', models.CharField(blank=True, max_length=255, null=True)),
                ('BillAddressNote', models.CharField(blank=True, max_length=255, null=True)),
                ('BillAddressBlockAddr1', models.CharField(blank=True, max_length=255, null=True)),
                ('BillAddressBlockAddr2', models.CharField(blank=True, max_length=255, null=True)),
                ('BillAddressBlockAddr3', models.CharField(blank=True, max_length=255, null=True)),
                ('BillAddressBlockAddr4', models.CharField(blank=True, max_length=255, null=True)),
                ('BillAddressBlockAddr5', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipAddressAddr1', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipAddressAddr2', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipAddressAddr3', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipAddressAddr4', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipAddressAddr5', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipAddressCity', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipAddressState', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipAddressProvince', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipAddressPostalCode', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipAddressCountry', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipAddressNote', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipAddressBlockAddr1', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipAddressBlockAddr2', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipAddressBlockAddr3', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipAddressBlockAddr4', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipAddressBlockAddr5', models.CharField(blank=True, max_length=255, null=True)),
                ('PONumber', models.CharField(blank=True, max_length=255, null=True)),
                ('TermsRefListID', models.CharField(blank=True, max_length=255, null=True)),
                ('TermsRefFullName', models.CharField(blank=True, max_length=255, null=True)),
                ('DueDate', models.CharField(blank=True, max_length=255, null=True)),
                ('SalesRepRefListID', models.CharField(blank=True, max_length=255, null=True)),
                ('SalesRepRefFullName', models.CharField(blank=True, max_length=255, null=True)),
                ('FOB', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipDate', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipMethodRefListID', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipMethodRefFullName', models.CharField(blank=True, max_length=255, null=True)),
                ('Subtotal', models.CharField(blank=True, max_length=255, null=True)),
                ('ItemSalesTaxRefListID', models.CharField(blank=True, max_length=255, null=True)),
                ('ItemSalesTaxRefFullName', models.CharField(blank=True, max_length=255, null=True)),
                ('SalesTaxPercentage', models.CharField(blank=True, max_length=255, null=True)),
                ('SalesTaxTotal', models.CharField(blank=True, max_length=255, null=True)),
                ('TotalAmount', models.CharField(blank=True, max_length=255, null=True)),
                ('CurrencyRefListID', models.CharField(blank=True, max_length=255, null=True)),
                ('CurrencyRefFullName', models.CharField(blank=True, max_length=255, null=True)),
                ('ExchangeRate', models.CharField(blank=True, max_length=255, null=True)),
                ('TotalAmountInHomeCurrency', models.CharField(blank=True, max_length=255, null=True)),
                ('IsManuallyClosed', models.CharField(blank=True, max_length=255, null=True)),
                ('IsFullyInvoiced', models.CharField(blank=True, max_length=255, null=True)),
                ('Memo', models.CharField(blank=True, max_length=255, null=True)),
                ('CustomerMsgRefListID', models.CharField(blank=True, max_length=255, null=True)),
                ('CustomerMsgRefFullName', models.CharField(blank=True, max_length=255, null=True)),
                ('IsToBePrinted', models.CharField(blank=True, max_length=255, null=True)),
                ('IsToBeEmailed', models.CharField(blank=True, max_length=255, null=True)),
                ('IsTaxIncluded', models.CharField(blank=True, max_length=255, null=True)),
                ('CustomerSalesTaxCodeRefListID', models.CharField(blank=True, max_length=255, null=True)),
                ('CustomerSalesTaxCodeRefFullName', models.CharField(blank=True, max_length=255, null=True)),
                ('CustomerTaxCodeRefListID', models.CharField(blank=True, max_length=255, null=True)),
                ('CustomFieldOther', models.CharField(blank=True, max_length=255, null=True)),
                ('Tax1Total', models.CharField(blank=True, max_length=255, null=True)),
                ('Tax2Total', models.CharField(blank=True, max_length=255, null=True)),
                ('AmountIncludesVAT', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='Status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='IsActive',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
