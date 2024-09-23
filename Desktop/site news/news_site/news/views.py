from django.shortcuts import render, get_object_or_404
from .models import News, Author

def home(request):
    latest_news = News.objects.order_by('-published_date')[:10]
    return render(request, 'news/home.html', {'latest_news': latest_news})

def news_list(request):
    all_news = News.objects.order_by('-published_date')
    return render(request, 'news/news_list.html', {'all_news': all_news})

def news_detail(request, new_id):
    news_item = get_object_or_404(News, id=new_id)
    return render(request, 'news/news_detail.html', {'news_item': news_item})

def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'news/authors_list.html', {'authors': authors})

def author_news(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    author_news_items = News.objects.filter(author=author).order_by('-published_date')
    return render(request, 'news/author_news.html', {'author': author, 'author_news_items': author_news_items})
