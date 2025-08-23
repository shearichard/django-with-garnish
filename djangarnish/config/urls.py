"""
URL configuration for config project.
"""

from django.contrib import admin
from django.urls import path, include
from config import views  # import the home view

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home page
    path('', views.home, name='home'),

    # Geography app URLs
    path('geography/', include('geography.urls')),
]

