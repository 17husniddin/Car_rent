from django.db import models
from django.contrib.auth import get_user_model

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(default=True)
    image = models.ImageField(default=True)
    category = models.ForeignKey(Category, related_name='products', on_delete = models.PROTECT )

    def __str__(self) -> str:
        return self.name


class Card(models.Model):
    user = models.ForeignKey(get_user_model(), related_name="cards", on_delete=models.PROTECT, default=None)
    is_sold = models.BooleanField(default=False)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.username}: {self.added_date}"


class CardItem(models.Model):
    product = models.ForeignKey(Product, related_name="carditems", on_delete=models.PROTECT, default=None)
    total = models.IntegerField(default=1)
    card = models.ForeignKey(Card, related_name="carditems", on_delete=models.CASCADE, default=None)

    def __str__(self) -> str:
        return self.product.name