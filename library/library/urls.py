"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
#to redirect from home to the app automatically
from django.views.generic import RedirectView

urlpatterns = [

    path('admin/', admin.site.urls),
    path('catalog/',include('catalog.urls')),
    #to redirect from ' ' to the actual app
    path('',RedirectView.as_view(url='catalog/')),
    path('accounts/',include('django.contrib.auth.urls')) #urls set up in the actual source code of django.
    #login,logout,password_change,password_change_done,password_reset,password_reset_done,password_reset_confirm,password_reset_complete 

]
