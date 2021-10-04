from django.shortcuts import render

from .forms import feedbackForm
from .models import Product


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


def feedback(request):
    if request.method == 'POST':
        form = feedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = feedbackForm()
    return render(request, 'mainapp/feedback.html', {'form': form})