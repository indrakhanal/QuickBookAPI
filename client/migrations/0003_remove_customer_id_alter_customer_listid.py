# Generated by Django 4.1.6 on 2023-02-12 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_alter_customer_listid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='id',
        ),
        migrations.AlterField(
            model_name='customer',
            name='ListID',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
