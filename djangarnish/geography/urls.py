from django.urls import path, include
from . import views

urlpatterns = [
    path('countries/', views.country_list, name='country_list'),
    path('countries/add/', views.country_create, name='country_create'),
    path('countries/<int:pk>/edit/', views.country_update, name='country_update'),
    path('countries/<int:pk>/delete/', views.country_delete, name='country_delete'),

    path('cities/', views.city_list, name='city_list'),
    path('cities/add/', views.city_create, name='city_create'),
    path('cities/<int:pk>/edit/', views.city_update, name='city_update'),
    path('cities/<int:pk>/delete/', views.city_delete, name='city_delete'),
]

