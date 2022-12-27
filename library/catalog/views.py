from django.shortcuts import render
from django.http import HttpResponse
from .models import Book,Author,BookInstance,Genre,Language
#class based view
from django.views.generic import CreateView,DetailView

# Create your views here.

def index(request):
    #return HttpResponse("Hello")
    #counts the totals
    num_books=Book.objects.all().count() 
    num_instances = BookInstance.objects.all().count()
    num_instances_avail = BookInstance.objects.filter(status__exact='a').count()
    #creates a dictionary with the values and sends them as context to a render request of index.html
    context = {
        'num_books':num_books,
        'num_instances':num_instances,
        'num_instances_avail':num_instances_avail
    }
    
    return render(request,'catalog/index.html',context=context)


class BookCreate(CreateView): #model_form.html 
    model = Book
    fields = '__all__'

class BookDetail(DetailView):
    model = Book