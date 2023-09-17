from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup_page, name='signup_page'),
    path('tac/', views.signup_user, name='signup_user'),
    path('termsandconditions/',views.display_tac, name='display_tac'),
    path('dashboard/', views.login_view, name='login_view'),
]