from django import forms

from services.models import Service
from users.forms import StyleFormMixin


class ServiceForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'


