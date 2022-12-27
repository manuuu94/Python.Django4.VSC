#connect path and to the view in the folder
from django.urls import path
from . import views

#create list called urlpatterns (always called like this)
#this is connected to the project url.py file and defines where these fall into
#url path, view connects to a function or view, kwargs, name a url to reference it elsewhere in django

urlpatterns = [

    #path('',views.simple_view),
    #path('sports/',views.sports_view),
    #path('finance/',views.finance_view),

#to dynamically send a "topic" or variable from the dictionary or a def to use a path converter
    path('<int:num_page>',views.num_page_view),
    #name a path to just call by its name in the views
    path('<topic>/',views.news_view,name='topic-page'),
    path('<int:num1>/<int:num2>',views.add_view),
    path('',views.simple_view)
]