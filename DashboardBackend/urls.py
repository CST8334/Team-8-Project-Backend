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
from Views.Creator import creator_views
from Views.Brand import brand_views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('creator/<int:pk>/', creator_views.CreatorDetails.as_view()),
    path('creator-ad-card/new', creator_views.CreatorMarketplace.as_view()),
    path('creator-ad-card/<int:creator_user_id>', creator_views.CreatorMarketplace.as_view()),
    path('creator-ad-card/<int:pk>/delete', creator_views.CreatorMarketplace.as_view()),
    path('new-creator/', creator_views.NewCreator.as_view()),
    path('new-brand-card/', brand_views.BrandAdCards.as_view()),
    path('brand-ad-cards/', brand_views.BrandAdCardsList.as_view()),
    path('login/', creator_views.LoginCreator.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
