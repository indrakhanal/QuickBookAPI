# Generated by Django 4.1.6 on 2023-02-23 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_customer_accountnumber_customer_balance_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('ListID', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('TimeCreated', models.CharField(blank=True, max_length=255, null=True)),
                ('TimeModified', models.CharField(blank=True, max_length=255, null=True)),
                ('EditSequence', models.CharField(blank=True, max_length=255, null=True)),
                ('Name', models.CharField(blank=True, max_length=255, null=True)),
                ('IsActive', models.CharField(blank=True, max_length=255, null=True)),
                ('ClassRefListID', models.CharField(blank=True, max_length=255, null=True)),
                ('ClassRefFullName', models.CharField(blank=True, max_length=255, null=True)),
                ('IsTaxAgency', models.CharField(blank=True, max_length=255, null=True)),
                ('CompanyName', models.CharField(blank=True, max_length=255, null=True)),
                ('Salutation', models.CharField(blank=True, max_length=255, null=True)),
                ('FirstName', models.CharField(blank=True, max_length=255, null=True)),
                ('MiddleName', models.CharField(blank=True, max_length=255, null=True)),
                ('LastName', models.CharField(blank=True, max_length=255, null=True)),
                ('VendorAddressAddr1', models.CharField(blank=True, max_length=255, null=True)),
                ('VendorAddressAddr2', models.CharField(blank=True, max_length=255, null=True)),
                ('VendorAddressAddr3', models.CharField(blank=True, max_length=255, null=True)),
                ('VendorAddressAddr4', models.CharField(blank=True, max_length=255, null=True)),
                ('VendorAddressAddr5', models.CharField(blank=True, max_length=255, null=True)),
                ('VendorAddressCity', models.CharField(blank=True, max_length=255, null=True)),
                ('VendorAddressState', models.CharField(blank=True, max_length=255, null=True)),
                ('VendorAddressProvince', models.CharField(blank=True, max_length=255, null=True)),
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
                ('ShipAddressPostalCode', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipAddressCountry', models.CharField(blank=True, max_length=255, null=True)),
                ('ShipAddressNote', models.CharField(blank=True, max_length=255, null=True)),
                ('Phone', models.CharField(blank=True, max_length=255, null=True)),
                ('AltPhone', models.CharField(blank=True, max_length=255, null=True)),
                ('Fax', models.CharField(blank=True, max_length=255, null=True)),
                ('Email', models.CharField(blank=True, max_length=255, null=True)),
                ('Cc', models.CharField(blank=True, max_length=255, null=True)),
                ('Contact', models.CharField(blank=True, max_length=255, null=True)),
                ('AltContact', models.CharField(blank=True, max_length=255, null=True)),
                ('NameOnCheck', models.CharField(blank=True, max_length=255, null=True)),
                ('AccountNumber', models.CharField(blank=True, max_length=255, null=True)),
                ('Notes', models.CharField(blank=True, max_length=255, null=True)),
                ('VendorTypeRefListID', models.CharField(blank=True, max_length=255, null=True)),
                ('VendorTypeRefFullName', models.CharField(blank=True, max_length=255, null=True)),
                ('TermsRefListID', models.CharField(blank=True, max_length=255, null=True)),
                ('TermsRefFullName', models.CharField(blank=True, max_length=255, null=True)),
                ('CreditLimit', models.CharField(blank=True, max_length=255, null=True)),
                ('VendorTaxIdent', models.CharField(blank=True, max_length=255, null=True)),
                ('IsVendorEligibleFor1099', models.CharField(blank=True, max_length=255, null=True)),
                ('IsVendorEligibleForT4A', models.CharField(blank=True, max_length=255, null=True)),
                ('OpenBalance', models.CharField(blank=True, max_length=255, null=True)),
                ('OpenBalanceDate', models.CharField(blank=True, max_length=255, null=True)),
                ('BillingRateRefListID', models.CharField(blank=True, max_length=255, null=True)),
                ('BillingRateRefFullName', models.CharField(blank=True, max_length=255, null=True)),
                ('PrefillAccount1RefListID', models.CharField(blank=True, max_length=255, null=True)),
                ('PrefillAccount1RefFullName', models.CharField(blank=True, max_length=255, null=True)),
                ('PrefillAccount2RefListID', models.CharField(blank=True, max_length=255, null=True)),
                ('PrefillAccount2RefFullName', models.CharField(blank=True, max_length=255, null=True)),
                ('PrefillAccount3RefListID', models.CharField(blank=True, max_length=255, null=True)),
                ('PrefillAccount3RefFullName', models.CharField(blank=True, max_length=255, null=True)),
                ('ExternalGUID', models.CharField(blank=True, max_length=255, null=True)),
                ('BusinessNumber', models.CharField(blank=True, max_length=255, null=True)),
                ('SalesTaxCodeRefListID', models.CharField(blank=True, max_length=255, null=True)),
                ('SalesTaxCodeRefFullName', models.CharField(blank=True, max_length=255, null=True)),
                ('SalesTaxCountry', models.CharField(blank=True, max_length=255, null=True)),
                ('IsSalesTaxAgency', models.CharField(blank=True, max_length=255, null=True)),
                ('SalesTaxReturnRefListID', models.CharField(blank=True, max_length=255, null=True)),
                ('SalesTaxReturnRefFullName', models.CharField(blank=True, max_length=255, null=True)),
                ('CurrencyRefListID', models.CharField(blank=True, max_length=255, null=True)),
                ('CurrencyRefFullName', models.CharField(blank=True, max_length=255, null=True)),
                ('CrudStatus', models.CharField(blank=True, max_length=255, null=True)),
                ('SyncStatus', models.CharField(blank=True, max_length=255, null=True)),
                ('ModifiedTimeLocal', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]