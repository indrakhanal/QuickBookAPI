# Generated by Django 4.1.6 on 2023-02-09 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TimeCreated', models.DateTimeField(auto_created=True)),
                ('ListID', models.CharField(max_length=20)),
                ('TimeModified', models.DateTimeField(blank=True, null=True)),
                ('EditSequence', models.CharField(blank=True, max_length=150, null=True)),
                ('Name', models.CharField(blank=True, max_length=40, null=True)),
                ('FullName', models.CharField(blank=True, max_length=100, null=True)),
                ('IsActive', models.BooleanField(default=False)),
                ('CompanyName', models.CharField(blank=True, max_length=150, null=True)),
                ('Salutation', models.CharField(blank=True, max_length=20, null=True)),
                ('FirstName', models.CharField(blank=True, max_length=40, null=True)),
                ('MiddleName', models.CharField(blank=True, max_length=40, null=True)),
                ('LastName', models.CharField(blank=True, max_length=40, null=True)),
                ('JobTitle', models.CharField(blank=True, max_length=40, null=True)),
                ('BillAddressAddr1', models.CharField(blank=True, max_length=200, null=True)),
                ('BillAddressAddr2', models.CharField(blank=True, max_length=200, null=True)),
                ('BillAddressAddr3', models.CharField(blank=True, max_length=200, null=True)),
                ('BillAddressAddr4', models.CharField(blank=True, max_length=200, null=True)),
                ('BillAddressAddr5', models.CharField(blank=True, max_length=200, null=True)),
                ('BillAddressCity', models.CharField(blank=True, max_length=200, null=True)),
                ('BillAddressState', models.CharField(blank=True, max_length=200, null=True)),
                ('BillAddressProvince', models.CharField(blank=True, max_length=200, null=True)),
                ('BillAddressCountry', models.CharField(blank=True, max_length=200, null=True)),
                ('BillAddressPostalCode', models.CharField(blank=True, max_length=200, null=True)),
                ('BillAddressNote', models.CharField(blank=True, max_length=200, null=True)),
                ('BillAddressBlockAddr1', models.CharField(blank=True, max_length=200, null=True)),
                ('BillAddressBlockAddr2', models.CharField(blank=True, max_length=200, null=True)),
                ('BillAddressBlockAddr3', models.CharField(blank=True, max_length=200, null=True)),
                ('BillAddressBlockAddr4', models.CharField(blank=True, max_length=200, null=True)),
                ('BillAddressBlockAddr5', models.CharField(blank=True, max_length=200, null=True)),
                ('ShipAddressAddr1', models.CharField(blank=True, max_length=200, null=True)),
                ('ShipAddressAddr2', models.CharField(blank=True, max_length=200, null=True)),
                ('ShipAddressAddr3', models.CharField(blank=True, max_length=200, null=True)),
                ('ShipAddressAddr4', models.CharField(blank=True, max_length=200, null=True)),
                ('ShipAddressAddr5', models.CharField(blank=True, max_length=200, null=True)),
                ('ShipAddressCity', models.CharField(blank=True, max_length=200, null=True)),
                ('ShipAddressState', models.CharField(blank=True, max_length=200, null=True)),
                ('ShipAddressProvince', models.CharField(blank=True, max_length=200, null=True)),
                ('ShipAddressCountry', models.CharField(blank=True, max_length=200, null=True)),
                ('ShipAddressPostalCode', models.CharField(blank=True, max_length=200, null=True)),
                ('ShipAddressNote', models.CharField(blank=True, max_length=200, null=True)),
                ('ShipAddressBlockAddr1', models.CharField(blank=True, max_length=200, null=True)),
                ('ShipAddressBlockAddr2', models.CharField(blank=True, max_length=200, null=True)),
                ('ShipAddressBlockAddr3', models.CharField(blank=True, max_length=200, null=True)),
                ('ShipAddressBlockAddr4', models.CharField(blank=True, max_length=200, null=True)),
                ('ShipAddressBlockAddr5', models.CharField(blank=True, max_length=200, null=True)),
                ('Phone', models.CharField(blank=True, max_length=20, null=True)),
                ('AltPhone', models.CharField(blank=True, max_length=20, null=True)),
                ('Fax', models.CharField(blank=True, max_length=20, null=True)),
                ('Email', models.EmailField(blank=True, max_length=254, null=True)),
                ('Cc', models.CharField(blank=True, max_length=20, null=True)),
                ('Contact', models.CharField(blank=True, max_length=40, null=True)),
                ('AltContact', models.CharField(blank=True, max_length=20, null=True)),
                ('CrudStatus', models.CharField(blank=True, max_length=20, null=True)),
                ('SyncStatus', models.CharField(blank=True, max_length=20, null=True)),
                ('ModifiedTimeLocal', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]