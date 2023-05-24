# Generated by Django 4.1.6 on 2023-02-24 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_salesorderitems_salesorder_status_vendor_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('TxnID', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('TimeCreated', models.CharField(blank=True, max_length=255, null=True)),
                ('TimeModified', models.CharField(blank=True, max_length=255, null=True)),
                ('EditSequence', models.CharField(blank=True, max_length=255, null=True)),
                ('TxnNumber', models.CharField(blank=True, max_length=255, null=True)),
                ('VendorRefListID', models.CharField(blank=True, max_length=255, null=True)),
                ('VendorRefFullName', models.CharField(blank=True, max_length=255, null=True)),
                ('ClassRefListID', models.CharField(blank=True, max_length=255, null=True)),
                ('ClassRefFullName', models.CharField(blank=True, max_length=255, null=True)),
                ('InventorySiteRefListID', models.CharField(blank=True, max_length=255, null=True)),
                ('InventorySiteRefFullName', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipToEntityRefListID', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipToEntityRefFullName', models.CharField(blank=True, max_length=255, null=True)),
                ('TemplateRefListID', models.CharField(blank=True, max_length=255, null=True)),
                ('TemplateRefFullName', models.CharField(blank=True, max_length=255, null=True)),
                ('TxnDate', models.CharField(blank=True, max_length=255, null=True)),
                ('TxnDateMacro', models.CharField(blank=True, max_length=255, null=True)),
                ('RefNumber', models.CharField(blank=True, max_length=255, null=True)),
                ('VendorAddressAddr1', models.CharField(blank=True, max_length=255, null=True)),
                ('VendorAddressAddr2', models.CharField(blank=True, max_length=255, null=True)),
                ('VendorAddressAddr3', models.CharField(blank=True, max_length=255, null=True)),
                ('VendorAddressAddr4', models.CharField(blank=True, max_length=255, null=True)),
                ('VendorAddressAddr5', models.CharField(blank=True, max_length=255, null=True)),
                ('VendorAddressCity', models.CharField(blank=True, max_length=255, null=True)),
                ('VendorAddressState', models.CharField(blank=True, max_length=255, null=True)),
                ('VendorAddressProvince', models.CharField(blank=True, max_length=255, null=True)),
                ('VendorAddressCounty', models.CharField(blank=True, max_length=255, null=True)),
                ('VendorAddressPostalCode', models.CharField(blank=True, max_length=255, null=True)),
                ('VendorAddressCountry', models.CharField(blank=True, max_length=255, null=True)),
                ('VendorAddressNote', models.CharField(blank=True, max_length=255, null=True)),
                ('VendorAddressBlockAddr1', models.CharField(blank=True, max_length=255, null=True)),
                ('VendorAddressBlockAddr2', models.CharField(blank=True, max_length=255, null=True)),
                ('VendorAddressBlockAddr3', models.CharField(blank=True, max_length=255, null=True)),
                ('VendorAddressBlockAddr4', models.CharField(blank=True, max_length=255, null=True)),
                ('VendorAddressBlockAddr5', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipAddressAddr1', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipAddressAddr2', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipAddressAddr3', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipAddressAddr4', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipAddressAddr5', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipAddressCity', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipAddressState', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipAddressProvince', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipAddressCounty', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipAddressPostalCode', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipAddressCountry', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipAddressNote', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipAddressBlockAddr1', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipAddressBlockAddr2', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipAddressBlockAddr3', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipAddressBlockAddr4', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipAddressBlockAddr5', models.CharField(blank=True, max_length=255, null=True)),
                ('TermsRefListID', models.CharField(blank=True, max_length=255, null=True)),
                ('TermsRefFullName', models.CharField(blank=True, max_length=255, null=True)),
                ('DueDate', models.CharField(blank=True, max_length=255, null=True)),
                ('ExpectedDate', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipMethodRefListID', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='AccountNumber',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='AltContact',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='AltPhone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Balance',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='BillAddressAddr1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='BillAddressAddr2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='BillAddressAddr3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='BillAddressAddr4',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='BillAddressAddr5',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='BillAddressBlockAddr1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='BillAddressBlockAddr2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='BillAddressBlockAddr3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='BillAddressBlockAddr4',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='BillAddressBlockAddr5',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='BillAddressCity',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='BillAddressCountry',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='BillAddressNote',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='BillAddressPostalCode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='BillAddressProvince',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='BillAddressState',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='BusinessNumber',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Cc',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='CompanyName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Contact',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='CreditCardInfoCreditCardAddress',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='CreditCardInfoCreditCardNumber',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='CreditCardInfoCreditCardPostalCode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='CreditCardInfoExpirationMonth',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='CreditCardInfoExpirationYear',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='CreditCardInfoNameOnCard',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='CreditLimit',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='CrudStatus',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='CurrencyRefFullName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='CurrencyRefListID',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='EditSequence',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='ExternalGUID',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Fax',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='FirstName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='FullName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='IsUsingCustomerTaxCode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='ItemSalesTaxRefFullName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='ItemSalesTaxRefListID',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='JobDesc',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='JobEnd',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='JobProjectedEnd',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='JobStart',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='JobStatus',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='JobTitle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='JobTypeRefFullName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='JobTypeRefListID',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='LastName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='ListID',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='MiddleName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='ModifiedTimeLocal',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='OpenBalance',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='PreferredDeliveryMethod',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='PreferredPaymentMethodRefFullName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='PreferredPaymentMethodRefListID',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='PriceLevelRefFullName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='PriceLevelRefListID',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='ResaleNumber',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='SalesRepRefFullName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='SalesRepRefListID',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='SalesTaxCodeRefFullName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='SalesTaxCodeRefListID',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='SalesTaxCountry',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Salutation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='ShipAddressAddr1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='ShipAddressAddr2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='ShipAddressAddr3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='ShipAddressAddr4',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='ShipAddressAddr5',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='ShipAddressBlockAddr1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='ShipAddressBlockAddr2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='ShipAddressBlockAddr3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='ShipAddressBlockAddr4',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='ShipAddressBlockAddr5',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='ShipAddressCity',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='ShipAddressCountry',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='ShipAddressNote',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='ShipAddressPostalCode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='ShipAddressProvince',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='ShipAddressState',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='SyncStatus',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='TaxCodeRefFullName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='TaxCodeRefListID',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='TaxRegistrationNumber',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='TermsRefFullName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='TotalBalance',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='salesorderitems',
            name='Desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
