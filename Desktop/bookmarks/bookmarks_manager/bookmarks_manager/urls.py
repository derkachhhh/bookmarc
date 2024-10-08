from django.urls import path, include
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('bookmarks.urls')),
    path('admin/', admin.site.urls),
    path('bookmarks/', include('bookmarks.urls')),  # Підключення додатка
]

