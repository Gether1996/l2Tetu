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
from viewer.views import homepage, account, logout_view, donate, success, fail, checkout, \
    transfer_coins, custom_login, news
from accounts.views import registration, password_reset_request, password_reset_confirm, password_reset_confirm_post, \
    password_reset_success

urlpatterns = [
    path('', homepage, name='homepage'),
    path('admin/', admin.site.urls),
    path('news/', news, name='news'),
    path('custom_login/', custom_login, name='custom_login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/', registration, name='registration'),
    path('accounts/profile/', account, name='account'),
    path('logout/', logout_view, name='logout'),
    path('', include('paypal.standard.ipn.urls')),
    path('donate/', donate, name='donate'),
    path('donate/checkout/', checkout, name='checkout'),
    path('paypal/ipn/', donate, name='paypal_ipn'),
    path('success/', success, name='success'),
    path('fail/', fail, name='fail'),
    path('transfer_coins/', transfer_coins, name='transfer_coins'),
    path('captcha/', include('captcha.urls')),
    path('password_reset_request/', password_reset_request, name='password_reset_request'),
    path('reset/<str:token>/', password_reset_confirm, name='password_reset_confirm'),
    path('password_reset_confirm_post/', password_reset_confirm_post, name='password_reset_confirm_post'),
    path('password_reset_success/<str:user_id>/', password_reset_success, name='password_reset_success'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
