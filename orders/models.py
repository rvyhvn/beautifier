from django.db import models

from products.models import AppModel, Product
from users.models import User

# from users.models import User


class Order(AppModel):
    order_total_price = models.IntegerField()

    ORDER_STATUS_LIST = (
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
    order_status = models.CharField(
        max_length=30,
        choices=ORDER_STATUS_LIST,
        default="",
    )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}. {self.order_total_price} | {self.order_status}"


class OrderItem(AppModel):
    order_item_total = models.IntegerField()
    order_price_per_pcs = (
        models.IntegerField()
    )  # TODO: search the compatible field for price per pieces in context order items for order model
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}. {self.order_item_total}"
