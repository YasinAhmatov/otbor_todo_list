from django.db import models

# Create your models here.


class ToDo(models.Model):

    id =  models.AutoField(
        primary_key=True) 

    title = models.CharField(
        max_length=200,
        verbose_name='Название таска'
    )
    description = models.CharField(
        max_length=200,
        verbose_name='Описание'
    )
    completed = models.BooleanField(
        default=False,
        verbose_name='Статус операции'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создано'
    )
   
    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = "Таск"
        verbose_name_plural = "Таски"