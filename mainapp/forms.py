from calendar import calendar

from django import forms
from .models import *


class feedbackForm(forms.Form):
    name = forms.CharField(max_length=50, label='ФИО')
    email = forms.EmailField(label='E-mail', required=False)
    prof = forms.ModelChoiceField(queryset=Product.objects.all(), label='Выберите программу обучения', empty_label='Не выбрано')
    birth = forms.DateField(input_formats=['%d.%m.%Y'], label='Дата рождения', required=False)
    phone = forms.IntegerField(label='Номер телефона')