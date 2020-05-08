from django.contrib import admin
from django.urls import path
from .views import HomeView, BoardDetail, delete_item, create_board, create_item, BoardDelete, BoardAddUser
from . import views

urlpatterns = [
    path('board/<int:pk>/delete/', views.BoardDelete.as_view(), name='board-delete'),
    path('', HomeView.as_view(), name='todoboard-home'),
    path('board/<int:pk>/', BoardDetail.as_view(), name="board-detail"),
    path('board/<int:pk>/delete-item/<int:itempk>/', views.delete_item, name="delete-item"),
    path('create-board/', views.create_board, name="create-board"),
    path('board/<int:pk>/create-item/', views.create_item, name='create-item'),
    path('board/<int:pk>/add-user/', views.BoardAddUser, name='add-user'),
    path('board/<int:pk>/add-user-email/', views.BoardAddUserEmail, name='add-user-email'),

]
