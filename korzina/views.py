from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.http import JsonResponse

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CardItemViewSet(viewsets.ModelViewSet):
    queryset = CardItem.objects.all()
    serializer_class = CardItemSerializer

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


@api_view(['POST'])
def add_cart(request):
    data = request.data

    user_id = data["user_id"]
    user = get_user_model().objects.get(id=user_id)
    products = data["products"]
    card = None
    result = {}
    try:
        card = Card.objects.get(user=user)
    except Card.DoesNotExist:
        card = Card.objects.create(user=user)
    result = {}
    result["user_id"] = user_id
    result["cart_id"] = card.id
    result["cart_items"] = []

    for product in products:
        product_id = product["product_id"]
        total = product["total"]

        product = Product.objects.get(id=product_id)
        try:
            card_item = CardItem.objects.get(product=product, card=card)
            card_item.total = total

        except CardItem.DoesNotExist:
            card_item = CardItem.objects.create(
                product=product,
                card=card,
                total=total
            )
        card_item.save()
        result["cart_items"].append({"id": card_item.id, "total": card_item.total, "product": card_item.product.id})
    return JsonResponse(result)