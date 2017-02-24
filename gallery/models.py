from django.db import models
from django.contrib.auth.models import User


class Type(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=250)
    type = models.ForeignKey(Type)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбоми"


class Limn(models.Model):
    image = models.ImageField(upload_to="grafity")
    description = models.CharField(blank=True, max_length=100)
    ty_pe = models.ForeignKey(Type)
    album = models.ForeignKey(Album)
    user = models.ForeignKey(User, verbose_name="Автор")
    published_date = models.DateTimeField(auto_created=True, verbose_name="Дата")

    def __str__(self):
        return self.description