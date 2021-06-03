from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from core.models import Book


class BookListView(ListView):
    """Book list view"""

    context_object_name = "books"
    model = Book
    template_name = "book/list.html"
    queryset = Book.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data()
        message_to_teacher = """
        W tym widoku wyświetlam wszystkie książki
        SELECT "core_book"."id", "core_book"."title", "core_book"."authors", "core_book"."is_lent" FROM "core_book",
        czyli SELECT * FROM core_book;
        """
        ctx.update({"message": message_to_teacher})
        return ctx


class BookCreateView(CreateView):
    """Book create view"""

    fields = ('title', 'authors', 'is_lent')
    model = Book
    template_name = "book/create.html"

    def get_success_url(self):
        return reverse("library:book_list")

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data()
        message_to_teacher = """
        W tym dodaję rekord do tabeli core_book 
        """
        ctx.update({"message": message_to_teacher})
        return ctx


class BookListToEdit(ListView):
    """Book to edit list view"""

    context_object_name = "books"
    model = Book
    template_name = "book/list_to_edit.html"
    queryset = Book.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data()
        message_to_teacher = """
        W tym widoku wyświetlam wszystkie książki do edycji
        SELECT "core_book"."id", "core_book"."title", "core_book"."authors", "core_book"."is_lent" FROM "core_book",
        czyli SELECT * FROM core_book;
        """
        ctx.update({"message": message_to_teacher})
        return ctx

class BookEditView(UpdateView):
    """Book edit view"""

    fields = ('title', 'authors', 'is_lent')
    model = Book
    template_name = "book/update.html"

    def get_success_url(self):
        return reverse("library:book_list")
