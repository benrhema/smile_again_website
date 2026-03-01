"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from impact import views  
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    # Added the missing paths that were causing the "NoReverseMatch" error
    path('team/', views.team, name='team'),
    path('partners/', views.partners, name='partners'),
    path('media/', views.media, name='media'),
    path('donate/', views.donate, name='donate'),

    # Placeholder paths for your dropdown links
    path('about/', views.home, name='about'), 
    path('programs/', views.home, name='programs'),
    path('volunteer/', views.home, name='volunteer'),
    path('events/', views.home, name='events'),
    path('news/', views.home, name='news'),
    path('contact/', views.home, name='contact'),
]

# CRITICAL for images
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    