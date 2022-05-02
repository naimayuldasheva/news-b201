from django.shortcuts import render, get_object_or_404
from news.models import News, Category


def news_views(request):
    news_all = News.objects.all()
    category_all = Category.objects.all()
    context = {
        'news_all':news_all,
        'category_all':category_all,
    }
    return render(request, 'index.html', context)



def show_category(request, category_id):
    news_all = News.objects.filter(category_id=category_id)
    category_all = Category.objects.all()
    context = {
        'news_all':news_all,
        'category_all':category_all,
    }
    return render(request, 'news/category.html', context)


def news_detail(request, id):
    news = get_object_or_404(News, id=id)
    return render(request, 'news/news_detail.html', {'news': news})
