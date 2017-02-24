from django.db import models
from django.contrib.auth.models import User
from gallery.models import Album


class Post(models.Model):
    title = models.CharField(max_length=30, verbose_name="Титул")
    content = models.TextField(verbose_name="Вміст")
    published_date = models.DateTimeField(auto_created=True, verbose_name="Дата публікації")
    album = models.ForeignKey(Album, verbose_name="Альбом")
    user = models.ForeignKey(User, verbose_name="Автор")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Повідомлення"
        verbose_name_plural = "Повідомлення"


class Comment(models.Model):
    content = models.TextField(verbose_name="Вміст")
    published_date = models.DateTimeField(auto_created=True, verbose_name="Дата публікації")
    post = models.ForeignKey(Post, verbose_name="Пост")

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"
