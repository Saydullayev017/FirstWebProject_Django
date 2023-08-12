from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text =models.TextField('Статья')
    date = models.DateTimeField('Дата Публикации')

    def _str_(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'



