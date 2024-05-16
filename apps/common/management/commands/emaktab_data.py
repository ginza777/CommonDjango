from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Custom management command to load data into the database."""
    def handle(self, *args, **options):
        help='This is a custom command'