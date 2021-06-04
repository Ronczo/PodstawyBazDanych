from django.contrib import admin
from .models import Book, Borrower, Lendment, Author, Rating


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
    """Lendment Admin"""

    fields = ("borrower", "book")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Author Admin"""

    fields = ("full_name",)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Rating Admin"""

    fields = ("rate", "book")
