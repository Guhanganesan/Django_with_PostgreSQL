"""Employee URL Configuration

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
from django.urls import path, include
from .api.router import router
from rest_framework.authtoken import views as auth_views
from .views import verify_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('tutorial', include('tutorial.urls')),
    path("google_sso/", include("django_google_sso.urls", namespace="django_google_sso")),
    path("accounts/", include("django.contrib.auth.urls")),  # new
    ######################## Token ###########################
    path('api/', include(router.urls)),  # Includes /api/users/ endpoint
    path('api-token-auth/', auth_views.obtain_auth_token, name='api-token-auth'),  # Token generation endpoint
    path('verify-token', verify_token, name='verify_token')
]
