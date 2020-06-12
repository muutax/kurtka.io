from django.db import models

# Create your models here.

class Records(models.Model):
    create_date = models.DateTimeField(auto_now = True)
    second_name = models.CharField(max_length = 15, verbose_name = "Фамилия")
    first_name = models.CharField(max_length=15, verbose_name="Имя")
    patronymic = models.CharField(max_length=20, verbose_name="Отчество")
    date_of_receipt = models.CharField(max_length=10  , verbose_name="Год поступления")
    date_of_release = models.CharField(max_length=10, verbose_name="Год выпуска")
    the_lvl = models.CharField(max_length=15, verbose_name="Уровень образования")
    direction_of_study = models.CharField(max_length=50, verbose_name="Напрвление обучения")
    phone_number = models.CharField(max_length=11, verbose_name="Телефон")
    e_mail = models.CharField(max_length=20, verbose_name="Email")
    work = models.CharField(max_length=200, verbose_name="Место работы")
    life = models.CharField(max_length=200, verbose_name="Место жительства")

    def __str__(self):
        return '%s %s-%s' % (self.first_name, self.second_name, self.patronymic)

    class Meta:
        verbose_name = "запись"
        verbose_name_plural = "Записи"