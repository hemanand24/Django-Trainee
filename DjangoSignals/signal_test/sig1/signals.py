import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book

@receiver(post_save, sender=Book)
def simulate_long_task(sender, instance, **kwargs):
    print("Signal started. Sleeping 5 seconds...")
    time.sleep(5)
    print("Signal finished.")