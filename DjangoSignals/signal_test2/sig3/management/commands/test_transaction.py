from django.core.management.base import BaseCommand
from sig3.models import Book
import threading

class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            print(f"[CALLER] Creating book in thread ID: {threading.get_ident()}")
            Book.objects.create(title="Transactional Test Book")
        except Exception as e:
            print(f"[CALLER] Caught exception: {e}")
        
        # Check if book got saved anyway
        if Book.objects.filter(title="Transactional Test Book").exists():
            print("[CALLER] Book was saved — signal DID NOT rollback transaction.")
        else:
            print("[CALLER] Book was NOT saved — signal DID rollback transaction ✅")
