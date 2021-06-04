
from django.forms import ModelForm

from core.models import Lendment


class LendBookForm(ModelForm):
    class Meta:
        model = Lendment
        fields = ["book", "borrower"]