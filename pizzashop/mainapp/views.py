from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html')

def basket_page(request):
    return render(request, 'mainapp/basket_page.html')