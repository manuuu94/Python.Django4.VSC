from django.urls import path
#import the view
from . import views

urlpatterns = [
    path('',views.list_patients,name='list_patients')
]