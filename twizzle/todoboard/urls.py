from django.contrib import admin
from django.urls import path
from .views import home, HomeView, BoardDetail

urlpatterns = [
    path('', HomeView.as_view(), name='todoboard-home'),
    path('board/<int:pk>/', BoardDetail.as_view(), name="board-detail"),
]
