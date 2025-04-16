from django.core.management.base import BaseCommand
from sig2.models import Book
import threading

class Command(BaseCommand):
    help = 'Check if signal runs in same thread'

    def handle(self, *args, **kwargs):
        print(f"[CALLER] Running in thread ID: {threading.get_ident()}")
        Book.objects.create(title="Thread Test Book")
