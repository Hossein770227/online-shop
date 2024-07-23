from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(_("full name"), max_length=150)
    email = models.EmailField(_("email"), max_length=254, blank=True, null=True)
    address= models.CharField(_("address"), max_length=700)
    order_notes = models.CharField(_("order notes"), max_length=500, blank=True)
    is_paid = models.BooleanField(_("is paid"), default=False)
    date_time_created = models.DateTimeField(_("date time created"), auto_now_add=True)
    date_time_modified = models.DateTimeField(_("date time modified"), auto_now=True)

    class Meta:
        verbose_name = _('orders')
        verbose_name_plural = _('orders')

    def __str__(self):
        return f'order {self.id}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name=_("order"), on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey("products.Product", verbose_name=_("product"), on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(_("quantity"), default=1)
    price = models.PositiveIntegerField(_("price"))

    class Meta:
        verbose_name = _('order item')
        verbose_name_plural = _('order item')

    def __str__(self):
        return f'order item {self.id} order {self.order}'