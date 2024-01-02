# Generated by Django 4.2.8 on 2024-01-02 04:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0002_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="order_status",
            new_name="status",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="order_total_price",
            new_name="total_price",
        ),
        migrations.RenameField(
            model_name="orderitem",
            old_name="order_item_total",
            new_name="item_total",
        ),
        migrations.RenameField(
            model_name="orderitem",
            old_name="order_price_per_pcs",
            new_name="price_per_pcs",
        ),
    ]
