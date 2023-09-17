# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('move_data/', views.move_data, name='move_data'),
]
