"""text_utils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

#   COMMENTS BY ME

"""
# First of all django will go to url.py then search the endpoint if it matches then it will go to corresponding views.py file

1. index is a function in the python file views.py
2. . denotes importing from the same file
3. ('')--put the endpoint 

"""
# COMMENTS BY ME

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="views"),
    path('analyze',views.analyze,name="analyze"),

]
