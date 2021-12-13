from django.db import models


class Car_date(models.Model):
    date =  models.DateField(auto_now_add=True)
    time_from = models.TimeField()
    time_to = models.TimeField()
    product = models.CharField(max_length=200)
# Create your models here.

    def __str__(self) -> str:
        return self.date