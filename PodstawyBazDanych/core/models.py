from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Author(models.Model):
    """Author Model"""

    full_name = models.CharField(max_length=512, blank=False, null=False)

    def __str__(self):
        return f"{self.full_name}"


class Book(models.Model):
    """Book model"""

    class BookGenres(models.TextChoices):
        """Borrower types"""

        UNSET = "UNSET", "--unset--"
        CRIME = "CRIME", "kryminał"
        ROMANCE = "ROMANCE", "romans"
        FICTION = "FICTION", "fikcja"

    title = models.CharField(max_length=512, blank=False, null=False)
    author = models.ForeignKey(
        Author, blank=False, null=False, on_delete=models.CASCADE, related_name="book"
    )
    is_lent = models.BooleanField(default=False, blank=False, null=False)
    genre = models.CharField(
        max_length=30,
        choices=BookGenres.choices,
        blank=False,
        null=False,
        default=BookGenres.UNSET,
    )

    def __str__(self):
        return f"{self.title} - {self.author}"


class Borrower(models.Model):
    """Borrower model"""

    class BorrowerTypes(models.TextChoices):
        """Borrower types"""

        UNSET = "UNSET", "--unset--"
        LEARNER = "LEARNER", "uczeń"
        STUDENT = "STUDENT", "student"
        PENSIONER = "PENSIONER", "emeryt"
        WORKER = "WORKER", "pracownik"

    type = models.CharField(
        max_length=30,
        choices=BorrowerTypes.choices,
        blank=False,
        null=False,
        default=BorrowerTypes.UNSET,
    )

    full_name = models.CharField(max_length=512, blank=False, null=False)

    def __str__(self):
        return f"{self.full_name} - {self.type}"


class Lendment(models.Model):
    """Lendment model"""

    borrower = models.ForeignKey(
        Borrower, blank=False, null=False, on_delete=models.PROTECT, related_name="lendment"
    )
    book = models.ForeignKey(
        Book, blank=False, null=False, on_delete=models.PROTECT, related_name="lendment"
    )

    def __str__(self):
        return f"{self.book} borrowed by {self.borrower}"

class Rating(models.Model):
    """Rating model"""

    rate = models.PositiveSmallIntegerField(default=3, validators=[MinValueValidator(0), MaxValueValidator(5)])
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="rating")

    def __str__(self):
        return f"{self.rate} - {self.book}"