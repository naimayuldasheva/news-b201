from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=140)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Категории"


class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="news/", blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Новости"