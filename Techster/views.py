from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'Techster/home.html')
def contact(request):
    return render(request, 'Techster/contactus.html')
def about(request):
    return render(request, 'Techster/aboutus.html')
def industries(request):
    return render(request, 'Techster/industries.html')
