from django.contrib import admin
from .models import Book, Borrower


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Book Admin"""

    fields = ("title", "authors", "is_lent")

@admin.register(Borrower)
class BorrowerAdmin(admin.ModelAdmin):
    """Borrower Admin"""

    fields = ("full_name", "type")

