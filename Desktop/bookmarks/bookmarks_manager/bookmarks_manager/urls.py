from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_bookmarks(request):
    return redirect('/bookmarks/')

urlpatterns = [
    path('api/', include('bookmarks.urls')),
    path('admin/', admin.site.urls),
    path('bookmarks/', include('bookmarks.urls')),
    path('', redirect_to_bookmarks),
]
