# Generated by Django 4.1.6 on 2023-03-02 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0016_shipaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipaddress',
            name='Status',
            field=models.BooleanField(default=False),
        ),
    ]
