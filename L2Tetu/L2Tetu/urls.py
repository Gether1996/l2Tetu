"""
URL configuration for L2Tetu project.

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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from viewer.views import homepage, forum, registration, account, logout_view, donate
from paypal.standard.ipn import urls as paypal_urls

urlpatterns = [
    path('', homepage, name='homepage'),
    path('admin/', admin.site.urls),
    path('forum/', forum, name='forum'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/', registration, name='registration'),
    path('accounts/profile/', account, name='account'),
    path('logout/', logout_view, name='logout'),
    path('paypal/', include(paypal_urls)),
    path('donate/', donate, name='donate'),
    path('paypal/ipn/', donate, name='paypal_ipn'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
