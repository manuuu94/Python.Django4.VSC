from django.urls import path
from . import views

#to name the urls. registers the app namespace.
app_name = 'my_app'

urlpatterns = [
    path('example2/',views.example2_view, name = 'example2'),
    path('',views.example_view, name = 'example'),
    path('variable/',views.variable_view, name = 'variable')
]

