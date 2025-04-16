from django.core.management.base import BaseCommand
from sig1.models import Book
import datetime

class Command(BaseCommand):
   
    def handle(self, *args, **kwargs):
        print(f"[{datetime.datetime.now()}] Before saving Book")
        Book.objects.create(title="Synchronous Signal Test")
        print(f"[{datetime.datetime.now()}] After saving Book")