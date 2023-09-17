from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('donor/', views.display_donor, name='display_donor')
]