from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import feedbackForm
from .models import Product

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

def success(request):
    return render(request, 'mainapp/success.html')

def fail(request):
    return render(request, 'mainapp/fail.html')

def education(request):
    title = 'Обучение'
    if request.method == 'GET':
        form = feedbackForm()
    elif request.method == 'POST':
        form = feedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            prof = form.cleaned_data['prof']
            birth= form.cleaned_data['birth']
            phone= form.cleaned_data['phone']
            try:
                send_mail(f'Заявка на обучение', f'{name} ({email}) с датой рождения {birth} оставил заявку на обучение по специальности {prof}, номер телефона для связи {phone}',
                'IldarYakup@gmail.com', ['DonicFur@yandex.ru'])
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('success')
        else:
            return redirect('fail')
    products = Product.objects.all()
    content = {'title': title, 'products': products,'form': form}
    return render(request, 'mainapp/education.html', content)


def page_not_found_view(request, exception):
    return render(request, 'mainapp/404.html', status=404)
