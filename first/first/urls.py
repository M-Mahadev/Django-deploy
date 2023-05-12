"""first URL Configuration

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
from django.contrib import admin
from django.urls import path
from firstapp import views


urlpatterns = [
 path('', views.index, name='index'),
 path('help', views.help, name='help'),
 path('2023/', views.year_current),
 path('<uuid:name>/', views.uuid_function),
 path('<int:year>/', views.year_function),
 path('<int:year>/<int:month>/', views.month_function),
 path('form', views.process_form),
 path('admin/', admin.site.urls),
 path('student/', views.process_form),
 path('studentnew/', views.get_student),
]
