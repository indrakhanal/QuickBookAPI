# Generated by Django 4.1.6 on 2023-03-02 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0015_alter_customer_email_alter_customer_timecreated_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShipAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ListID', models.TextField(blank=True, null=True)),
                ('ShipAddress', models.TextField(blank=True, null=True)),
                ('Category', models.TextField(blank=True, null=True)),
            ],
        ),
    ]