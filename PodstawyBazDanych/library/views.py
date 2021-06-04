from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

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
        W tym widoku wyświetlam wszystkie książki ||
        SQL z ORM: SELECT "core_book"."id", "core_book"."title", "core_book"."authors", "core_book"."is_lent"
         FROM "core_book", ||
        czyli SELECT * FROM core_book;
        """
        ctx.update({"message": message_to_teacher})
        return ctx


class BookCreateView(CreateView):
    """Book create view"""

    fields = ("title", "authors", "is_lent")
    model = Book
    template_name = "book/create.html"

    def get_success_url(self):
        """Add additional context data"""

        return reverse("library:book_list")

    def get_context_data(self, *, object_list=None, **kwargs):
        """Add additional context data"""

        ctx = super().get_context_data()
        message_to_teacher = """
        W tym dodaję rekord do tabeli core_book ||
        SQL z ORM: INSERT INTO "core_book" ("title", "authors", "is_lent") VALUES ('asdd', 'asdd', false)
        RETURNING "core_book"."id"; args=('asdd', 'asdd', False)
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
        """Add additional context data"""

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

    fields = ("title", "authors", "is_lent")
    model = Book
    template_name = "book/update.html"

    def get_success_url(self):
        """redirect after successful edition"""

        return reverse("library:book_list")

    def get_context_data(self, *, object_list=None, **kwargs):
        """Add additional context data"""

        ctx = super().get_context_data()
        message_to_teacher = """
        W tym edytuję rekord z tabeli core_book ||
        SQL z ORM: UPDATE "core_book" SET "title" = 'Tytuł 122', "authors" = 'Autor 12222', "is_lent" = true
         WHERE "core_book"."id" = 1; args=('Tytuł 122', 'Autor 12222', True, 1)
        """
        ctx.update({"message": message_to_teacher})
        return ctx


class BookListToDeleteView(ListView):
    """Book to edit list view"""

    context_object_name = "books"
    model = Book
    template_name = "book/list_to_delete.html"
    queryset = Book.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        """Add additional context data"""

        ctx = super().get_context_data()
        message_to_teacher = """
        W tym widoku wyświetlam wszystkie książki do usunięcia
        SELECT "core_book"."id", "core_book"."title", "core_book"."authors", "core_book"."is_lent" FROM "core_book",
        czyli SELECT * FROM core_book;
        """
        ctx.update({"message": message_to_teacher})
        return ctx


class BookDeleteView(DeleteView):
    """Book delete view"""

    model = Book
    context_object_name = "book"
    template_name = "book/delete.html"

    def get_success_url(self):
        """redirect after successful edition"""

        return reverse("library:book_list_to_delete")

    def get_context_data(self, *, object_list=None, **kwargs):
        """Add additional context data"""

        ctx = super().get_context_data()
        message_to_teacher = """
        W tym widoku usuwam rekord z bazy core_book ||
        SQL z ORM: DELETE FROM "core_book" WHERE "core_book"."id" IN (11); args=(11,)
        """
        ctx.update({"message": message_to_teacher})
        return ctx

