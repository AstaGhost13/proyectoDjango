from django.shortcuts import render

def home(request):
    return render(request, "dashboard/base.html")
def index(request):
    return render(request, 'index.html') 
