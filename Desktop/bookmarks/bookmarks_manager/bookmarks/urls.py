from django.urls import path
from .views import BookmarkListCreate, BookmarkRetrieveUpdateDestroy

urlpatterns = [
    path('bookmarks/', BookmarkListCreate.as_view(), name='bookmark-list-create'),
    path('bookmarks/<int:pk>/', BookmarkRetrieveUpdateDestroy.as_view(), name='bookmark-detail'),
]
