"""
URL configuration for mybankingproject project.

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


from banking.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
     path('', index, name='index'),
    path('create_account/', create_account, name='create_account'),
    path('login/', login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('withdraw/', withdraw, name='withdraw'),
    path('deposit/', deposit, name='deposit'),
    path('change_pin/', change_pin, name='change_pin'),
]

