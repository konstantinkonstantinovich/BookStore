"""BookStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf.urls.static import static

from store.views import UserProfile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/user/', UserProfile.as_view(), name='user-detail'),
    path('', RedirectView.as_view(url='/store/', permanent=True)),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
