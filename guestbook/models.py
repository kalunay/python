from django.db import models


class Guestbook(models.Model):
    user = models.CharField(max_length = 20, verbose_name = 'Users')
    posted = models.DateTimeField(auto_now_add = True, db_index = True, verbose_name = 'Public')
    content = models.TextField(verbose_name = 'Content')

    class Meta:
        ordering = ['-posted']
        verbose_name = 'запись гостевой книги'
        verbose_name_plural = 'записи гостевой книги'