from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookmark_list, name='bookmark-list'),  # Головна сторінка зі списком закладок
    path('<int:pk>/', views.bookmark_detail, name='bookmark-detail'),  # Деталі закладки
    path('add/', views.add_bookmark, name='add-bookmark'),  # Додавання нової закладки
    path('edit/<int:pk>/', views.edit_bookmark, name='edit-bookmark'),  # Редагування закладки
    path('delete/<int:pk>/', views.delete_bookmark, name='delete-bookmark'),  # Видалення закладки
]
