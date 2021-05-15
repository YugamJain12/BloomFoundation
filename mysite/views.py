from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'index.html')

def events(request):
    return render(request,'events.html')

def about(request):
	return render(request,'about.html')

def contact(request):
	return render(request,'contact.html')

def donate(request):
	return render(request,'donate.html')