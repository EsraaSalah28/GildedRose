"""GildRose URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from GildRose.gildrose.views import show,index

urlpatterns = [
    path('admin/', admin.site.urls),
#Index Route
#localhost:8000/route
path('', index),

#Create Contact Route
#localhost:8000/create
path('create', views.create),

#Show/List Contacts
#localhost:8000/show
path('show',views.show),
]
