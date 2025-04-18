from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book

@receiver(post_save, sender=Book)
def book_post_save(sender, instance, **kwargs):
    print("[SIGNAL] Signal started. Raising exception to test transaction...")
    raise Exception("Oops! Signal failed intentionally.")
