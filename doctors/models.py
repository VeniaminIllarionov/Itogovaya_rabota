from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=250, verbose_name='Имя')
    surname = models.CharField(max_length=250, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=250, verbose_name='Отчество')
    work_experience = models.IntegerField(default=0, verbose_name='Стаж работы')
    clinical = models.TextField(verbose_name='Клиника')
    specialization = models.CharField(max_length=250, verbose_name='Специализация')
    science = models.TextField(verbose_name='Ученая степень / Категория / Ученое звание')
    post = models.CharField(max_length=250, verbose_name='Должность')
    picture = models.ImageField(upload_to='services/', blank=True, null=True, verbose_name='Картинка')

    def __str__(self):
        return f'{self.name}.{self.surname}.{self.patronymic}'

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'
