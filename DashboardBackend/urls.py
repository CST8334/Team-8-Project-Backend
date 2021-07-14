"""DashboardBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework.urlpatterns import format_suffix_patterns
from dashboard.views import brand_views
#from dashboard.views import creator_views
from dashboard.views import ad_card_views
from Views.Creator import creator_views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('creators/', creator_views.CreatorList.as_view()),
    #path('creator/<int:pk>/', creator_views.CreatorDetails.as_view()),
    path('new-creator/', creator_views.NewCreator.as_view()),
    path('brands/', brand_views.BrandList.as_view()),
    path('brand/<int:pk>/', brand_views.BrandDetails.as_view()),
    path('adcards/', ad_card_views.AdCardList.as_view()),
    path('adcard/<int:pk>', ad_card_views.AdCardDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
