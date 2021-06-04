from django.urls import path

from .views import BookListView, BookCreateView, BookEditView, BookListToDeleteView, BookListToEdit, BookDeleteView

app_name = "library"

urlpatterns = [
    path("book-list/", BookListView.as_view(), name="book_list"),
    path("book-list-to-edit/", BookListToEdit.as_view(), name="book_list_to_edit"),
    path("book-list-to-delete/", BookListToDeleteView.as_view(), name="book_list_to_delete"),
    path("book-create/", BookCreateView.as_view(), name="book_create"),
    path("book-update/<int:pk>/", BookEditView.as_view(), name="book_update"),
    path("book-delete/<int:pk>/", BookDeleteView.as_view(), name="book_delete"),

]