from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html');

def about(request):
    return render(request, 'about.html');

def question(request):
    return render(request, 'question.html');

def instructions(request):
    return render(request, 'instructions.html');

def communication(request):
    return render(request, 'communication.html');

def loginPage(request):
    return render(request, 'login.html');

def signup(request):
    return render(request, 'signup.html');

def biodata(request):
    return render(request, 'biodata.html');