"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from news.views import news_views, show_category, news_detail, category_news

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', news_views, name="homepage"),
    path('category/', show_category, name="show_category"),
    path('category/<int:id>', category_news, name='category_news'),
    path('detail/<int:id>', news_detail, name='news_detail')
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)