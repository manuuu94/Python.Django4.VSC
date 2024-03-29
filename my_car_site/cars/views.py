from django.shortcuts import render,redirect
from django.urls import reverse
from . import models
# Create your views here.
def list(request):
    all_cars = models.Car.objects.all()
    context = {'all_cars':all_cars}
    return render(request,'cars/list.html',context=context)

def add(request):
    #check if there is a POST request
    #can be used to check the POST and print it: 
    #print(request.POST)
    if request.POST:
        brand = request.POST['brand']
        year = int(request.POST['year'])
        models.Car.objects.create(brand=brand,year=year)
        #asks to redirect to the app name cars name list. defined in urls.py within the app. 
        return redirect(reverse('cars:list'))
    else:
        return render(request,'cars/add.html')


def delete(request):
    if request.POST:
        pk = request.POST['pk']
        try:
            models.Car.objects.get(pk=pk).delete()
            return redirect(reverse('cars:list'))
        except:
            print('PK not found!')
            return redirect(reverse('cars:list'))
    else:        
        return render(request,'cars/delete.html')