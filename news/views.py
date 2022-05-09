from django.shortcuts import render, get_object_or_404
from news.models import News, Category


def news_views(request):
    news_all = News.objects.all()
    news_slider = News.objects.all()[:3]
    world_news_slider = News.objects.filter(category='4')[:4]
    category_all = Category.objects.all()[:4]
    context = {
        'news_all':news_all,
        'news_slider':news_slider,
        'world_news_slider':world_news_slider,
        'category_all':category_all,    
    }
    return render(request, 'include/main.html', context)



def show_category(request):
    category_all = Category.objects.all()
    news_all = News.objects.all()
    context = {
        'category_all':category_all,
        'news_all':news_all,

    }
    return render(request, 'include/category.html', context)


def news_detail(request, id):
    news = get_object_or_404(News, id=id)
    return render(request, 'news/news_detail.html', {'news': news})


def category_news(request, id):
    category_all = Category.objects.all()
    news_all = News.objects.filter(category_id = id)
    context = {
        'category_all':category_all,
        'news_all':news_all,
    }
    return render(request, 'include/category.html', context)
