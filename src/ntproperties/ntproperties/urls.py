"""ntproperties URL Configuration

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
from listing.views import home_view
from listing.views import property_create_view, block_create_view, company_create_view, companycard_create_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('createproperty', property_create_view),
    path('createblock', block_create_view),
    path('createcompany', company_create_view),
    path('createcompanycard', companycard_create_view),
]
