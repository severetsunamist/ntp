"""
URL configuration for ntproperties project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from realestate import views
from django.conf.urls.static import static
from realestate.views import ComapnyCardView


urlpatterns = [
    path('admin', admin.site.urls),
    path('login', views.login_view, name='login'),
    path('', views.dashboard_view, name='dashboard'),
    path('listing', views.listing_view, name='listing'),
    path('block_search', views.block_search_view, name='block_search'),
    path('map', views.map_view, name='map'),
    path('create_property', views.create_property_view, name='create_property'),
    path('create_block', views.create_block_view, name='create_block'),
    path('create_company', views.create_company_view, name='create_company'),
    path('create_companycard', ComapnyCardView.as_view(template_name="create_companycard.html"), name='create_companycard'),
    path('create_contact', views.create_contact_view, name='create_contact'),
    path('create_request', views.create_request_view, name='create_request'),
    path('create_deal', views.create_deal_view, name='create_deal'),
    path('create_agreement', views.create_agreement_view, name='create_agreement'),
    path('create_several', views.create_several_view, name='create_several'),
    path('block/<int:pk>', views.block_view, name='block_view'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
