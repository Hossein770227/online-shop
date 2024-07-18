from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

class Product(models.Model):
    title = models.CharField(_("title"), max_length=50)
    description = models.TextField(_("description"))
    short_description = models.CharField(_("short description"), blank=True, max_length=200)
    price = models.PositiveIntegerField(_("price"))
    image = models.ImageField(_("image"), upload_to='cover/', default=True)
    price_with_discount = models.PositiveIntegerField(_("price with discount"), blank=True, null=True)
    active = models.BooleanField(_("active"), default=True)
    date_time_created = models.DateTimeField(_("date time created"), auto_now_add=True)

    class Meta:
        verbose_name = _('products')
        verbose_name_plural = _('products')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("products:product_detail", args=[self.pk])
    

class Comment(models.Model):
    SCORE_CHOICES = (
        ('1',_('very bad')),
        ('2',_(' bad')),
        ('3',_('normal')),
        ('4',_('good')),
        ('5',_('perfect')),
    )

    author = models.ForeignKey(get_user_model(), verbose_name=_("author"), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_("product"), on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(_("text comment"))
    score = models.CharField(choices=SCORE_CHOICES, max_length=2)
    active = models.BooleanField(_("active"), default=True)
    date_time_created = models.DateTimeField(_("date time created"), auto_now_add=True)

    def __str__(self):
        return f'{self.author} : {self.text}'