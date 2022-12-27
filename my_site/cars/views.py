from django.shortcuts import render,redirect
from django.urls import reverse
from . forms import ReviewForm


# Create your views here.
def rental_review(request):
    #POST REQUEST --> FORM FILLED IN --> THANK YOU!
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        #check if form is valid and redirect
        if form.is_valid():
            #dictionary view in console
            print(form.cleaned_data)
            #will save the data in the DB
            form.save()
            return redirect(reverse('cars:thank_you'))

    #ELSE, RENDER FORM  
    else:
        form = ReviewForm()
    return render(request,'cars/rental_review.html',context={'form':form}) #pass the form as the context#

def thank_you(request):
    return render(request,'cars/thank_you.html')