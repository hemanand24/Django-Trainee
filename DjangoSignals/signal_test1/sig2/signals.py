import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book

@receiver(post_save, sender=Book)
def check_thread(sender, instance, **kwargs):
    print(f"[SIGNAL] Running in thread ID: {threading.get_ident()}")
