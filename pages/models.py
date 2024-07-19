from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

class CallUs(models.Model):
    # user = models.ForeignKey(get_user_model() , on_delete=models.CASCADE)
    email = models.EmailField(_("email"), max_length=254, blank=True, null=True)
    message = models.TextField(_("message"))
    date_time_created = models.DateTimeField(_("date time created "),auto_now_add=True)
    
    
    class Meta:
        verbose_name = _('user message')
        verbose_name_plural = _('user message')

    def __str__(self):
        return self.message
    
