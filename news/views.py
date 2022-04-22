from django.shortcuts import render
from news.models import News


def news_views(request):
    news_all = News.objects.all()
    return render(request, 'index.html', {'news_all':news_all})
# Create your views here.
