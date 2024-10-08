from rest_framework import generics
from .models import Bookmark
from .serializers import BookmarkSerializer

class BookmarkListCreate(generics.ListCreateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

class BookmarkRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
