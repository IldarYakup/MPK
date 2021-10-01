from django.http import HttpResponse, HttpResponseRedirect, BadHeaderError
from django.shortcuts import render
from .models import Product, ProductCategory
from django.contrib import messages, auth
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail


# Create your views here.

def main(request):
    return render(request, 'mainapp/index.html')

def courses(request):

    title = 'курсы'
    products = Product.objects.all()
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/courses.html', content)

def contact(request):
    return render(request, 'mainapp/contact.html')

def sees(request):
    return render(request, 'mainapp/sees.html')

def education(request):
    title = 'Обучение'
    products = Product.objects.all()
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/education.html', content)


def contactform(reguest):
    if reguest.method == 'POST':
        form = ContactForm(reguest.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            sender = form.cleaned_data['sender']
            copy = form.cleaned_data['copy']

            recepients = ['IldarYakup@gmail.com']
            # Если пользователь захотел получить копию себе, добавляем его в список получателей
            if copy:
                recepients.append(sender)
            send_mail(form.cleaned_data['subject'], form.cleaned_data['message'], 'DonicFur@yandex.ru', ['IldarYakup@gmail.com'])
            return HttpResponseRedirect('main')

    else:
        form = ContactForm()
    # Выводим форму в шаблон
    return render(reguest, 'contact.html', {'form': form, 'username': auth.get_user(reguest).username})