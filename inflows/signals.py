from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Inflow


@receiver(post_save, sender=Inflow)
def inflow_post_save(sender, instance, created, *args, **kwargs):
    if created:
        product = instance.product
        product.quantity += instance.quantity
        product.save()
