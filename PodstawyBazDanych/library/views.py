from django.db.models import Count, Max, Avg
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView

from core.models import Book, Borrower, Author
from library.forms import LendBookForm, RateBookForm


class BookListView(ListView):
    """Book list view"""

    context_object_name = "books"
    model = Book
    template_name = "book/list.html"
    queryset = Book.objects.all().select_related("author")

    def get_context_data(self, *, object_list=None, **kwargs):
        """Add additional context data"""

        ctx = super().get_context_data()
        message_to_teacher = "W tym widoku wyświetlam wszystkie książki"
        sql = """
        -SELECT "core_book"."id", "core_book"."title", "core_book"."authors", "core_book"."is_lent"
        FROM "core_book", ||
        czyli SELECT * FROM core_book;
        """
        ctx.update({"message": message_to_teacher, "sql": sql})
        return ctx


class BookCreateView(CreateView):
    """Book create view"""

    fields = ("title", "is_lent", "author", "genre")
    model = Book
    template_name = "book/create.html"

    def get_success_url(self):
        """Redirect after creation"""

        return reverse("library:book_list")

    def get_context_data(self, *, object_list=None, **kwargs):
        """Add additional context data"""

        ctx = super().get_context_data()
        message_to_teacher = "W tym dodaję rekord do tabeli core_book"
        sql = """
        -INSERT INTO "core_book" ("title", "authors", "is_lent") VALUES ('asdd', 'asdd', false)
        RETURNING "core_book"."id"; 
        """
        ctx.update({"message": message_to_teacher, "sql": sql})
        return ctx


class AuthorCreateView(CreateView):
    """Author create view"""

    fields = ("full_name",)
    model = Author
    template_name = "author/create.html"

    def get_success_url(self):
        """Redirect after creation"""

        return reverse("core:home")

    def get_context_data(self, *, object_list=None, **kwargs):
        """Add additional context data"""

        ctx = super().get_context_data()
        message_to_teacher = "W tym widoku dodaję rekord do tabeli core_author"
        sql = """
        -INSERT INTO "core_author" ("full_name") VALUES ('Adam Mickiewicz') RETURNING "core_author"."id";
        """
        ctx.update({"message": message_to_teacher, "sql": sql})
        return ctx


class BookListToEdit(ListView):
    """Book to edit list view"""

    context_object_name = "books"
    model = Book
    template_name = "book/list_to_edit.html"
    queryset = Book.objects.filter(is_lent=False).select_related("author")

    def get_context_data(self, *, object_list=None, **kwargs):
        """Add additional context data"""

        ctx = super().get_context_data()
        message_to_teacher = (
            "W tym widoku wyświetlam wszystkie książki do edycji (książka nie może być wypożyczona)"
        )
        sql = """
        -SELECT "core_book"."id", "core_book"."title", "core_book"."author_id", "core_book"."is_lent",
         "core_book"."genre", "core_author"."id", "core_author"."full_name" FROM "core_book" 
         INNER JOIN "core_author" ON ("core_book"."author_id" = "core_author"."id") 
         WHERE NOT "core_book"."is_lent";
        """
        ctx.update({"message": message_to_teacher, "sql": sql})
        return ctx


class BookEditView(UpdateView):
    """Book edit view"""

    fields = ("title", "author", "is_lent", "genre")
    model = Book
    template_name = "book/update.html"

    def get_success_url(self):
        """redirect after successful edition"""

        return reverse("library:book_list")

    def get_context_data(self, *, object_list=None, **kwargs):
        """Add additional context data"""

        ctx = super().get_context_data()
        message_to_teacher = "W tym edytuję rekord z tabeli core_book"
        sql = """
        -UPDATE "core_book" 
        SET "title" = 'W pustyni i w puszczy', "author_id" = 1, "is_lent" = false, "genre" = 'FICTION' 
        WHERE "core_book"."id" = 1;
        """
        ctx.update({"message": message_to_teacher, "sql": sql})
        return ctx


class BookListToDeleteView(ListView):
    """Book to edit list view"""

    context_object_name = "books"
    model = Book
    template_name = "book/list_to_delete.html"
    queryset = Book.objects.filter(is_lent=False).select_related("author")

    def get_context_data(self, *, object_list=None, **kwargs):
        """Add additional context data"""

        ctx = super().get_context_data()
        message_to_teacher = "W tym widoku wyświetlam wszystkie książki do usunięcia (książka nie może być wypożyczona)"

        sql = """
        -SELECT "core_book"."id", "core_book"."title", "core_book"."author_id", "core_book"."is_lent",
         "core_book"."genre", "core_author"."id", "core_author"."full_name" 
         FROM "core_book" INNER JOIN "core_author" ON ("core_book"."author_id" = "core_author"."id") 
         WHERE NOT "core_book"."is_lent";
        """
        ctx.update({"message": message_to_teacher, "sql": sql})
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
        message_to_teacher = "W tym widoku usuwam rekord z bazy core_book"
        sql = """
        SQL z ORM: DELETE FROM "core_book" WHERE "core_book"."id" IN (11);
        """
        ctx.update({"message": message_to_teacher, "sql": sql})
        return ctx


class BorrowerListView(ListView):
    """Borrower list view"""

    context_object_name = "borrowers"
    model = Borrower
    template_name = "borrower/list.html"
    queryset = Borrower.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        """Add additional context data"""

        ctx = super().get_context_data()
        message_to_teacher = "W tym widoku wyświetlam wszystkich czytelników"

        sql = """
        -SELECT "core_borrower"."id", "core_borrower"."type", "core_borrower"."full_name" FROM "core_borrower";
        """
        ctx.update({"message": message_to_teacher, "sql": sql})
        return ctx


class BorrowerCreateView(CreateView):
    """Borrower create view"""

    fields = ("full_name", "type")
    model = Borrower
    template_name = "borrower/create.html"

    def get_success_url(self):
        """Redirect user after creation"""

        return reverse("library:borrower_list")

    def get_context_data(self, *, object_list=None, **kwargs):
        """Add additional context data"""

        ctx = super().get_context_data()
        message_to_teacher = "W tym widoku dodaję rekord do tabeli core_borrower"
        sql = """
        -INSERT INTO "core_borrower" ("type", "full_name")
        VALUES ('PENSIONER', 'Robert Malinowski') RETURNING "core_borrower"."id";
        """
        ctx.update({"message": message_to_teacher, "sql": sql})
        return ctx


class BookListToLendView(ListView):
    """Book list to lend view"""

    context_object_name = "books"
    model = Book
    template_name = "library/list_to_lend.html"
    queryset = Book.objects.filter(is_lent=False).select_related("author")

    def get_context_data(self, *, object_list=None, **kwargs):
        """Add additional context data"""

        ctx = super().get_context_data()
        message_to_teacher = """
        W tym widoku pobieram listę dostępnych książek do wypożyczenia (książka nie może być wypożyczona
        """
        sql = """
        -SELECT "core_book"."id", "core_book"."title", "core_book"."author", "core_book"."is_lent" 
        FROM "core_book" WHERE NOT "core_book"."is_lent";
        """

        ctx.update({"message": message_to_teacher, "sql": sql})
        return ctx


class BookLendView(FormView):
    """Book list to lend view"""

    template_name = "library/lend_book_form.html"
    form_class = LendBookForm

    def get_context_data(self, *, object_list=None, **kwargs):
        """Add additional context data"""

        ctx = super().get_context_data()
        message_to_teacher = """
        W tym widoku wypożyczam ksiażkę dodając rekord do bazy tabeli (książka i czytelnik)
        """
        sql = """
        -INSERT INTO "core_lendment" ("borrower_id", "book_id") VALUES (5, 4) RETURNING "core_lendment"."id"
        """
        sql2 = """
        -SELECT core_book"."id", "core_book"."title", "core_book"."authors", "core_book"."is_lent" FROM "core_book"
         WHERE "core_book"."id" = 8 - INICJACJA FORMULARZA
        """
        ctx.update({"message": message_to_teacher, "sql": sql, "sql2": sql2})
        return ctx

    def get_initial(self):
        """ Return the initial data to use for form """

        pk = self.kwargs.get("pk")
        book = Book.objects.get(pk=pk)
        initial = {"book": book}
        return initial

    def get_success_url(self):
        """Redirect user after creation"""

        return reverse("core:home")

    def form_valid(self, form):
        """Adds extra logic to save form"""
        pk = self.kwargs.get("pk")
        book = Book.objects.get(pk=pk)
        if form.is_valid():
            book.is_lent = True
            book.save()
            lendment = form.save(commit=False)
            lendment.book = book
            lendment.save()

        return super().form_valid(form)


class BookListToReturn(ListView):
    """Book list to return view"""

    model = Book
    template_name = "library/list_to_return_book.html"
    queryset = Book.objects.filter(is_lent=True).select_related("author")
    context_object_name = "books"

    def get_context_data(self, *, object_list=None, **kwargs):
        """Add additional context data"""

        ctx = super().get_context_data()
        message_to_teacher = "W tym widoku wczytuję książki, które są aktualnie wypożyczone"
        sql = """
        -SELECT "core_book"."id", "core_book"."title", "core_book"."author_id", "core_book"."is_lent", 
        "core_book"."genre", "core_author"."id", "core_author"."full_name" 
        FROM "core_book" INNER JOIN "core_author" ON ("core_book"."author_id" = "core_author"."id") 
        WHERE "core_book"."is_lent";
        """
        ctx.update({"message": message_to_teacher, "sql": sql})
        return ctx


def return_book(request, pk):
    """Return book view"""

    template_name = "library/return_book.html"
    book = Book.objects.get(pk=pk)
    message_to_teacher = "Zwracamy ksiązkę, zmieniajać flage is_lent"
    sql = """
    -UPDATE "core_book" SET "title" = 'Szkoła tańca', "author_id" = 1, "is_lent" = false, "genre" = 'ROMANCE'
     WHERE "core_book"."id" = 3;
    """
    context = {"book": book, "message": message_to_teacher, "sql": sql}

    if request.method == "POST":
        if "return" in request.POST:
            book.is_lent = False
            book.save()
            return redirect("core:home")

    return render(request, template_name, context)


class BookListToRate(ListView):
    """Book list to rate view"""

    model = Book
    context_object_name = "books"
    template_name = "book/list_to_rate.html"
    queryset = Book.objects.all().select_related("author")

    def get_context_data(self, *, object_list=None, **kwargs):
        """Add additional context data"""

        ctx = super().get_context_data()
        message_to_teacher = "Pobieram listę wszystkich książek do oceny"
        sql = """
        -SELECT "core_book"."id", "core_book"."title", "core_book"."author_id", "core_book"."is_lent", "core_book"."genre",
         "core_author"."id", "core_author"."full_name" FROM "core_book" 
         INNER JOIN "core_author" ON ("core_book"."author_id" = "core_author"."id");
        """
        ctx.update({"message": message_to_teacher, "sql": sql})
        return ctx


class RateBookView(FormView):
    """Rate book view"""

    form_class = RateBookForm
    template_name = "library/rate_book_form.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        """Add additional context data"""

        ctx = super().get_context_data()
        message_to_teacher = "Oceniam książkę dodająć rekord do tabeli core_rating"
        sql = """
        -INSERT INTO "core_rating" ("rate", "book_id") VALUES (3, 2) RETURNING "core_rating"."id"; 
        """
        ctx.update({"message": message_to_teacher, "sql": sql})
        return ctx

    def get_initial(self):
        """ Return the initial data to use for form """

        pk = self.kwargs.get("pk")
        book = Book.objects.get(pk=pk)
        initial = {"book": book}
        return initial

    def get_success_url(self):
        """Redirect user after creation"""

        return reverse("core:home")

    def form_valid(self, form):
        """Adds extra logic to save form"""

        pk = self.kwargs.get("pk")
        book = Book.objects.get(pk=pk)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.book = book
            rate.save()

        return super().form_valid(form)


class Statistics(View):
    def get(self, request):
        template_name = "library/statistics.html"

        books_amount = Book.objects.all().count()
        books_amount_sql = """-SELECT COUNT(*) AS "__count" FROM "core_book";"""
        borrowers_amount = Borrower.objects.all().count()
        borrowers_amount_sql = """-SELECT COUNT(*) AS "__count" FROM "core_borrower"; """
        authors_amount = Author.objects.all().count()
        authors_amount_sql = """-SELECT COUNT(*) AS "__count" FROM "core_author";"""
        top_3_author_by_number_of_books = Author.objects.annotate(num_books=Count("book")).order_by(
            "-num_books"
        )[:3]
        top_3_author_by_number_of_books_sql = """
        "core_author"."id", "core_author"."full_name", COUNT("core_book"."id") AS "num_books" 
        FROM "core_author" LEFT OUTER JOIN "core_book" ON ("core_author"."id" = "core_book"."author_id") 
        GROUP BY "core_author"."id" ORDER BY "num_books" DESC LIMIT 3;
        """
        average_book_rating = Book.objects.all().aggregate(Avg("rating__rate"))
        average_book_rating_sql = """-
        SELECT AVG("core_rating"."rate")
        AS "rating__rate__avg" FROM "core_book"
        LEFT OUTER JOIN "core_rating"
        ON ("core_book"."id" = "core_rating"."book_id");
        """
        book_with_avg_rate = (
            Book.objects.all()
            .filter(rating__rate__isnull=False)
            .annotate(avg_rate=Avg("rating__rate"))
        )
        books_with_avg_rate_sql = """-
        SELECT "core_book"."id", "core_book"."title", "core_book"."author_id",
         "core_book"."is_lent", "core_book"."genre",
         AVG("core_rating"."rate") AS "avg_rate" FROM "core_book" 
         INNER JOIN "core_rating" ON ("core_book"."id" = "core_rating"."book_id") WHERE "core_rating"."rate" 
         IS NOT NULL GROUP BY "core_book"."id";
         """
        book_with_highest_rate = (
            Book.objects.all()
            .filter(rating__rate__isnull=False)
            .annotate(avg_rate=Avg("rating__rate"))
            .order_by("-avg_rate")
            .first()
        )

        book_with_highest_rate_sql = """-
        SELECT "core_book"."id", "core_book"."title", "core_book"."author_id",
        "core_book"."is_lent", "core_book"."genre", 
        AVG("core_rating"."rate") AS "avg_rate" FROM "core_book" 
        INNER JOIN "core_rating" ON ("core_book"."id" = "core_rating"."book_id") 
        WHERE "core_rating"."rate" IS NOT NULL GROUP BY "core_book"."id" ORDER BY 
        "avg_rate" DESC LIMIT 1;
        """

        context = {
            "books_amount": books_amount,
            "books_amount_sql": books_amount_sql,
            "borrowers_amount": borrowers_amount,
            "borrowers_amount_sql": borrowers_amount_sql,
            "authors_amount": authors_amount,
            "authors_amount_sql": authors_amount_sql,
            "top_3_author_by_number_of_books": top_3_author_by_number_of_books,
            "top_3_author_by_number_of_books_sql": top_3_author_by_number_of_books_sql,
            "average_book_rating": average_book_rating["rating__rate__avg"],
            "average_book_rating_sql": average_book_rating_sql,
            "book_with_avg_rate": book_with_avg_rate,
            "book_with_avg_rate_sql": books_with_avg_rate_sql,
            "book_with_highest_rate": book_with_highest_rate,
            "book_with_highest_rate_sql": book_with_highest_rate_sql,

        }
        return render(request, template_name, context)
