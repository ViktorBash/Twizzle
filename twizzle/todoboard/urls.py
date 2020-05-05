from django.contrib import admin
from django.urls import path
from .views import home, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='todoboard-home'),
]