from django.db import models

from products.models import AppModel, Product
from users.models import CustomUser


class Order(AppModel):
    total_price = models.IntegerField()

    STATUS_LIST = (
        (
            "Pending",
            "Pending",
        ),  # The order has been received but not yet processed or confirmed.
        (
            "Confirmed",
            "Confirmed",
        ),  # The order has been confirmed and is being processed.
        (
            "Shipped",
            "Shipped",
        ),  # The items have been shipped to the courier or shipping address.
        (
            "Delivered",
            "Delivered",
        ),  # The items have been received by the customer.
        (
            "Cancelled",
            "Cancelled",
        ),  # The customer or seller has cancelled the order before shipping.
        (
            "On Hold",
            "On Hold",
        ),  # There might be issues or constraints causing a delay in the order.
        (
            "Returned",
            "Returned",
        ),  # Items have been returned by the customer.
        (
            "Completed",
            "Completed",
        ),  # The order has been completed, items received, and transaction finalized.
        (
            "Failed",
            "Failed",
        ),  # The order failed to process or experienced delivery failure.
    )
    status = models.CharField(
        max_length=30,
        choices=STATUS_LIST,
    )
    user_id = models.ForeignKey(
        CustomUser,
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f"{self.id}. {self.total_price} | {self.status}"


class OrderItem(AppModel):
    item_total = models.IntegerField()
    # TODO: search the compatible field for price per pieces in context order items for order model
    price_per_pcs = models.IntegerField()
    product_id = models.OneToOneField(
        Product,
        null=True,
        on_delete=models.SET_NULL,
    )
    order_id = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.id}. Item total = {self.item_total} | Product: {self.product_id}"
