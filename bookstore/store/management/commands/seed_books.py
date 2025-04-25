from django.core.management.base import BaseCommand
from store.models import Book

class Command(BaseCommand):
    help = 'Seed the database with sample books'

    def handle(self, *args, **kwargs):
        sample_books = [
            {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'description': 'A classic novel set in the Jazz Age.', 'price': 10.99, 'stock': 10},
            {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'description': 'A novel about racial injustice in the Deep South.', 'price': 8.99, 'stock': 15},
            {'title': '1984', 'author': 'George Orwell', 'description': 'A dystopian novel about totalitarianism.', 'price': 9.99, 'stock': 20},
            {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'description': 'A romantic novel about manners and marriage.', 'price': 7.99, 'stock': 12},
            {'title': 'Moby-Dick', 'author': 'Herman Melville', 'description': 'A novel about the quest for a giant white whale.', 'price': 11.99, 'stock': 8},
        ]

        for book_data in sample_books:
            book, created = Book.objects.get_or_create(title=book_data['title'], defaults=book_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Added book: {book.title}"))
            else:
                self.stdout.write(f"Book already exists: {book.title}")
