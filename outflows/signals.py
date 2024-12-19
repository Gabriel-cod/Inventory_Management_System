from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Outflow


@receiver(post_save, sender=Outflow)
def outflow_post_save(sender, instance, created, *args, **kwargs):
    if created:
        product = instance.product
        product.quantity -= instance.quantity
        product.save()
