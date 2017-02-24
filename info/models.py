from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Ім’я')
    mail = models.EmailField(verbose_name='Поштова скринька')
    mesage = models.TextField(verbose_name='Повідомлення')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ('Зв’язок')
        verbose_name_plural = ('Зв’язки')