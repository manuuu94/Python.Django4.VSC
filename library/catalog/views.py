from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Book,Author,BookInstance,Genre,Language
#class based view
from django.views.generic import CreateView,DetailView,ListView
#decorators (required to login to access X page) @login_required in the function
from django.contrib.auth.decorators import login_required
#mixins for class based views to require to authenticate first
from django.contrib.auth.mixins import LoginRequiredMixin
#model form for the userclass. dealing with the form to apply it into a classbasedview
from django.contrib.auth.forms import UserCreationForm

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

#classbasedview
#mixin
class BookCreate(LoginRequiredMixin,CreateView): #model_form.html the default is to go to the BookDetail page (create view below)
    model = Book
    fields = '__all__'

#classbasedview
class BookDetail(DetailView):
    model = Book

#functionbasedview
@login_required
def my_view(request):
    return render(request,'catalog/my_view.html')


class SignUpView(CreateView):
    #overwrites the form class with the usercreationform we imported
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'catalog/signup.html'


class CheckedOutBookByUserView(LoginRequiredMixin,ListView):
    #list all instances but filter by current user session
    model = BookInstance
    template_name = 'catalog/profile.html'
    paginate_by = 5 #5 book instances per page

    def get_queryset(self):
        #query that filters out that the borrower is equals to the request user.
        return BookInstance.objects.filter(borrower=self.request.user)