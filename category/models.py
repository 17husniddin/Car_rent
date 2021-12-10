from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.IntegerField(default=True)
    image = models.ImageField()
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey('Category', related_name="carpage", on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Category(models.Model):
        name = models.CharField(max_length=300)

        def __str__(self):
              return self.name