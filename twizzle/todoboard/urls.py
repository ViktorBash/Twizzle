from django.contrib import admin
from django.urls import path
from .views import home, HomeView, BoardDetail, delete_item
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='todoboard-home'),
    path('board/<int:pk>/', BoardDetail.as_view(), name="board-detail"),
    path('board/<int:pk>/delete-item/<int:itempk>/', views.delete_item, name="delete-item"),
]
