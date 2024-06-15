"""
URL configuration for Employee_Management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from Sites_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('view_employee/<int:pid>', view_employee, name='view_employee'),
    path('edit_employee/<int:pid>', edit_employee, name='edit_employee'),
    path('delete_employee/<int:pid>', delete_employee, name='delete_employee'),

]
