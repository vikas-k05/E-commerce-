# Generated by Django 4.0.5 on 2022-10-15 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_customer_order_orderitem_shippingaddress_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='price',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
