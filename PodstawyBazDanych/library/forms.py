
from django.forms import ModelForm, Select

from core.models import Lendment, Rating


class LendBookForm(ModelForm):
    class Meta:
        model = Lendment
        fields = ["book", "borrower"]


class RateBookForm(ModelForm):
    class Meta:
        model = Rating
        fields = ["rate", "book"]
        choices = (
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
        )

        widgets = {
            'rate': Select(choices=choices),
        }