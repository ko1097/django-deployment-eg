from django.shortcuts import render


def index(request):
    return render(request,'basic/index.html')

def middle(request):
    return render(request,'basic/middle.html')

def final(request):
    return render(request,'basic/final.html')

# Create your views here.
