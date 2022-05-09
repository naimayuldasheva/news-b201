from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=140)
    image = models.ImageField(blank=True, null=True)
    url = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('show_category', kwargs={
            'category_id':self.pk
        })

    class Meta:
        verbose_name_plural = "Категории"
        ordering = ['-id']
        

class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="news/", blank=True, null=True)
    description = models.TextField()
    url = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Новости"
        ordering = ['-id']


class SocialSidebar(models.Model):
    link_address = models.CharField(
        max_length=255,
        help_text="ссылка на ресурс, например ссылка на инстаграм: https://www.instagram.com/mbcstudio_org/"
    )
    