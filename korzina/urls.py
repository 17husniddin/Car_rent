from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('product', ProductViewSet)
router.register('category', CategoryViewSet)
router.register('cardItem', CardItemViewSet)
router.register('card', CardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]