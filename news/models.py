from django.db import models
from datetime import datetime


class New(models.Model):
    title = models.CharField(max_length=100, unique_for_date='posted',verbose_name='Title')
    description = models.TextField(verbose_name='Short text')
    content = models.TextField(verbose_name='Text')
    posted = models.DateTimeField(default=datetime.now(),db_index=True, verbose_name='Public date')

    class Meta:
        ordering = ['-posted']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
