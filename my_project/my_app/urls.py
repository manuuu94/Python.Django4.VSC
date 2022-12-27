from django.urls import path
from . import views

urlpatterns = [
    #url path, view connects to a function or view, kwargs, name a url to reference it elsewhere in django
    path('',views.index,name='index')
]