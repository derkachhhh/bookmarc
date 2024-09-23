from django.contrib import admin
from django.urls import path, include  # Додайте include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),  # Підключення URL-адрес з вашого додатку
]
