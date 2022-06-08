from django.db import models


class StatusCrm(models.Model):
    Status_name = models.CharField(max_length=200, verbose_name='Название статуса')

    def __str__(self):
        return self.Status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class AboutSettings(models.Model):
    about_title = models.CharField(max_length=200, verbose_name='Заголовок абзаца')
    about_text = models.TextField(verbose_name='Текст абзаца')

    def __str__(self):
        return self.about_title

    class Meta:
        verbose_name = 'Страничка обо мне'
        verbose_name_plural = 'Странички обо мне'

class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=15, verbose_name='Телефон')
    order_telegram_id = models.CharField(max_length=200, null=True, blank=True, verbose_name='Ссылка на ваш телеграм')
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class CommentCrm(models.Model):
    comment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заявка')
    comment_text = models.TextField(verbose_name='Текст комментария')
    comment_dt = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

# class AmcSettings(models.Model):
#     amc_titleS = models.CharField(max_length=200, verbose_name='Заголовок' )
#     amc_text = models.TextField(verbose_name='Текст заголовка')
#
#     def __str__(self):
#         return self.amc_text
#
#     class Meta:
#         verbose_name = 'Информацию о себе'
#         verbose_name_plural = 'Информация о себе'