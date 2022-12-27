from django.shortcuts import render
#to import a generic template view class,formview
from django.views.generic import TemplateView,FormView,CreateView,ListView,DetailView,UpdateView,DeleteView
#reverselazy to use as successurl
from django.urls import reverse_lazy
#import the formview
from classroom.forms import ContactForm
#import the models for the view
from classroom.models import Teacher


# Create your views here.
""" def home_view(request):
    return render(request,'classroom/home.html')
 """

#to use a template view class
class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'


#model classbasedview create
class TeacherCreateView(CreateView):
    #connect to the model
    model = Teacher
    #the template looks for model_form.html in the app and creates the form 
    #to choose specific fields
    #fields = ['first_name','last_name']
    fields = "__all__"
    success_url = reverse_lazy('classroom:thank_you')

#model classbasedview list
class TeacherListView(ListView):
    model = Teacher
    #to overwrite the query set(Teacher.objects.all()), for example:
    queryset = Teacher.objects.order_by('first_name')
    #to change the use of object_list
    context_object_name = "teacher_list"

class TeacherDetailView(DetailView):
    #looks for a specific template model_detail.html
    model = Teacher
    # searches by PK and sends the teacher

class TeacherUpdateView(UpdateView):
    #shares the createview model and the model_form.html too!! --- PK
    model = Teacher
    fields = "__all__"
    success_url = reverse_lazy('classroom:list_teacher')

class TeacherDeleteView(DeleteView):
    #sends back form with a single confirm delete button
    #model_confirm_delete.html
    model = Teacher
    success_url = reverse_lazy('classroom:list_teacher')




#formview template
class ContactFormView(FormView):
    #connects the form to the formview and the templatename
    form_class = ContactForm 
    template_name = 'classroom/contact.html'
    #success url? actual URL, not the template.html
    #success_url = "/classroom/thank_you"
    #or use reverse lazy
    success_url = reverse_lazy('classroom:thank_you')
    #what to do with the form?
    def form_valid(self,form):
        print(form.cleaned_data)
        #or specific value
        print(form.cleaned_data['name'])
        return super().form_valid(form)


