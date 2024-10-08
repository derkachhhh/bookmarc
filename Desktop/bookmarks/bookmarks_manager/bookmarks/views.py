from django.shortcuts import render, redirect, get_object_or_404
from .models import Bookmark
from django.http import HttpResponse

# Відображення списку закладок
def bookmark_list(request):
    bookmarks = Bookmark.objects.all()
    return render(request, 'index.html', {'bookmarks': bookmarks})

# Відображення деталей конкретної закладки
def bookmark_detail(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)
    return render(request, 'bookmark_detail.html', {'bookmark': bookmark})

# Додавання нової закладки
def add_bookmark(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        url = request.POST.get('url')
        category = request.POST.get('category')
        favorite = request.POST.get('favorite') == 'on'
        Bookmark.objects.create(title=title, url=url, category=category, favorite=favorite)
        return redirect('bookmark-list')

    return render(request, 'add_bookmark.html')
# Редагування закладки
def edit_bookmark(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)
    if request.method == 'POST':
        bookmark.title = request.POST.get('title')
        bookmark.url = request.POST.get('url')
        bookmark.category = request.POST.get('category')
        bookmark.favorite = request.POST.get('favorite') == 'on'
        bookmark.save()
        return redirect('bookmark-list')

    return render(request, 'edit_bookmark.html', {'bookmark': bookmark})

# Видалення закладки
def delete_bookmark(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)
    if request.method == 'POST':
        bookmark.delete()
        return redirect('bookmark-list')
    return render(request, 'delete_confirmation.html', {'bookmark': bookmark})
