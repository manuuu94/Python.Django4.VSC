from django.shortcuts import render
#import models
from . import models

# Create your views here.
def list_patients(request):
    #takes on the request and the template name as well as the context you are passing
    all_patients = models.Patient.objects.all()
    #creates a context list (must be a dictionary)
    #depending on the key of the dictionary is that is called in the html!
    context_list={'patients':all_patients}
    return render(request,'office/list.html',context=context_list)
