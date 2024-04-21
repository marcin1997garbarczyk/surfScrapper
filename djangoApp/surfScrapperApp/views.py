from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')
def registerForm(request):
    return render(request, 'registerForm.html')