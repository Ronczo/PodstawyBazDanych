
from django.forms import ModelForm

from core.models import Lendment, Rating


class LendBookForm(ModelForm):
    class Meta:
        model = Lendment
        fields = ["book", "borrower"]


class RateBookForm(ModelForm):
    class Meta:
        model = Rating
        fields = ["rate", "book"]