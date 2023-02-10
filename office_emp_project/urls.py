"""office_emp_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path
from emp_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.employee_view,name='index'),
    path('all_emp/',views.all_emp,name='all_emp'),
    path('add_emp/',views.add_emp,name='add_emp'),
    path('del_emp/',views.del_emp,name='del_emp'),
    path('del_emp/<int:emp_id>',views.del_emp,name='del_emp'),
    path('filter_emp/',views.filter_emp),
]
