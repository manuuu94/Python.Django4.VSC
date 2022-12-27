from django.shortcuts import render
#import to display a HttpResponse
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello this is a view example in my app")


