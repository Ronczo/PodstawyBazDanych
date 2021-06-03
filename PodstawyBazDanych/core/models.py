from django.db import models


class Book(models.Model):
    """Book model"""

    title = models.CharField(max_length=512, blank=False, null=False)
    authors = models.CharField(max_length=512, blank=False, null=False)
    is_lent = models.BooleanField(default=False, blank=False, null=False)

    def __str__(self):
        return f"{self.title} - {self.authors}"


class Borrower(models.Model):
    """Borrower model"""

    full_name = models.CharField(max_length=512, blank=False, null=False)


class BorrowerType(models.Model):
    """Borrower type model"""

    class BorrowerTypes(models.TextChoices):
        """Borrower types"""

        UNSET = "UNSET", "--unset--"
        LEARNER = "LEARNER", "learner"
        STUDENT = "STUDENT", "student"
        PENSIONER = "PENSIONER", "pensioner"
        WORKER = "WORKER", "worker"

    name = models.CharField(
        max_length=30,
        choices=BorrowerTypes.choices,
        blank=False,
        null=False,
        default=BorrowerTypes.UNSET,
    )
    borrower = models.ForeignKey(
        Borrower, blank=False, null=False, on_delete=models.PROTECT, related_name="borrower_type"
    )


class Lendment(models.Model):
    """Lendment model"""

    borrower = models.ForeignKey(
        Borrower, blank=False, null=False, on_delete=models.PROTECT, related_name="lendment"
    )
    book = models.ForeignKey(
        Book, blank=False, null=False, on_delete=models.PROTECT, related_name="lendment"
    )
