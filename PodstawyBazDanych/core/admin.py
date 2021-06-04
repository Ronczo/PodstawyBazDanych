from django.contrib import admin
from .models import Book, Borrower, Lendment, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Book Admin"""

    fields = ("title", "is_lent", "genre", "author")

@admin.register(Borrower)
class BorrowerAdmin(admin.ModelAdmin):
    """Borrower Admin"""

    fields = ("full_name", "type")

@admin.register(Lendment)
class LendmentAdmin(admin.ModelAdmin):
    """Borrower Admin"""

    fields = ("borrower", "book")


@admin.register(Author)
class LendmentAdmin(admin.ModelAdmin):
    """Borrower Admin"""

    fields = ("full_name",)

