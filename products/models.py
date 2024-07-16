from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Product(models.Model):
    title = models.CharField(_("title"), max_length=50)
    description = models.TextField(_("description"))
    short_description = models.CharField(_("short description"), max_length=200)
    price = models.PositiveIntegerField(_("price"))
    price_with_discount = models.PositiveIntegerField(_("price with discount"), blank=True, null=True)
    active = models.BooleanField(_("active"), default=True)
    date_time_created = models.DateTimeField(_("date time created"), auto_now_add=True)

    class Meta:
        verbose_name = _('products')
        verbose_name_plural = _('products')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("product_detail", args=[self.pk])
    