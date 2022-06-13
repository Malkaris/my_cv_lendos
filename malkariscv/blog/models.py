from django.db import models

# Create your models here.
class Blog(models.Model):

    blog_title = models.CharField(max_length=200, verbose_name='Название блога')
    blog_image = models.ImageField(upload_to='sliderimg/', null=True)
    blot_text = models.TextField(verbose_name='Текст для блога')
    blog_css = models.CharField(max_length=200, null=True, default='-', verbose_name='CSS класс')

    def __str__(self):
        return self.blog_title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'