from django.urls import path

from .views import BookListView, BookCreateView, BookEditView, BookListToDeleteView, BookListToEdit, BookDeleteView, \
    BorrowerListView, BorrowerCreateView, BookListToLendView, BookLendView, AuthorCreateView, BookListToReturn, \
    return_book, BookListToRate, RateBookView

app_name = "library"

urlpatterns = [
    # author
    path("author-create/", AuthorCreateView.as_view(), name="author_create"),
    # book
    path("book-list/", BookListView.as_view(), name="book_list"),
    path("book-list-to-edit/", BookListToEdit.as_view(), name="book_list_to_edit"),
    path("book-list-to-delete/", BookListToDeleteView.as_view(), name="book_list_to_delete"),
    path("book-create/", BookCreateView.as_view(), name="book_create"),
    path("book-update/<int:pk>/", BookEditView.as_view(), name="book_update"),
    path("book-delete/<int:pk>/", BookDeleteView.as_view(), name="book_delete"),
    path("book-list-to-rate/", BookListToRate.as_view(), name="book_list_to_rate"),
    path("book-rate/<int:pk>/", RateBookView.as_view(), name="book_rate"),
    # borrower
    path("borrower-list/", BorrowerListView.as_view(), name="borrower_list"),
    path("borrower-create/", BorrowerCreateView.as_view(), name="borrower_create"),
    # library
    path("library-list-to-lend/", BookListToLendView.as_view(), name="library_list_to_lend"),
    path("library-lend-book/<int:pk>", BookLendView.as_view(), name="library_lend_book"),
    path("library-list-to-return/", BookListToReturn.as_view(), name="library_list_to_return"),
    path("library-return-book/<int:pk>", return_book, name="library_return_book"),
]
