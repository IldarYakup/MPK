from django.shortcuts import render
from .models import Product, ProductCategory


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




