from django.forms import ModelForm, DateTimeInput
from records.models import Record


class AddRecord(ModelForm):
    class Meta:
        model = Record
        fields = ('city', 'datetime', 'c_value')
        widgets = {
            'datetime': DateTimeInput(attrs={'type': 'datetime'})
        }


class GetRecord(ModelForm):
    class Meta:
        model = Record
        fields = ('city', 'datetime')
        widgets = {
            'datetime': DateTimeInput(attrs={'type': 'datetime'})
        }
