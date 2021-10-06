from calendar import calendar

from django import forms
from .models import *
from phonenumber_field.formfields import PhoneNumberField

class feedbackForm(forms.Form):
    name = forms.CharField(max_length=50, label='ФИО', widget=forms.TextInput({'class' : 'class="u-border-2 u-border-grey-75 u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle', 'placeholder' : 'Иванов Иван Иванович'}))
    email = forms.EmailField(label='E-mail', widget=forms.TextInput({'class' : 'u-border-2 u-border-grey-75 u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle', 'placeholder' : 'Ivanov@mail.ru'}))
    prof = forms.ModelChoiceField(queryset=Product.objects.all(), empty_label='Выберите программу обучения', widget=forms.Select({'class' : 'u-border-2 u-border-grey-75 u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle'}))
    birth = forms.DateField(label='Дата рождения', widget=forms.TextInput({'class' : 'u-border-2 u-border-grey-75 u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle', 'type' : 'date'}))
    phone = PhoneNumberField(required=True, label='Номер телефона', widget=forms.TextInput({'class': "u-border-2 u-border-grey-75 u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle", 'placeholder' : '+79000000000'}))