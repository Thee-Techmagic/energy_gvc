# signal to create payment amount of 200 once customer is created
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Customer, Payment

@receiver(post_save, sender=Customer)
def create_payment_amount(sender, instance, created, **kwargs):
    if created:
        Payment.objects.create(customer=instance, amount=200)

        