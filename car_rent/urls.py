"""car_rent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from korzina.views import *
from contact.views import *
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from contact.views import *

from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from account.views import *
from django.contrib.auth import login
from account.views import RegisterAPI
from django.urls import path
from knox import views as knox_views
from account.views import LoginAPI
from django.contrib.auth import login
from account.views import RegisterAPI
from django.urls import path
from knox import views as knox_views
from account.views import LoginAPI
from django.urls import path
from car_picture.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = DefaultRouter()
router.register('aloqa', AloqaViewSet)
router.register('product', ProductViewSet)
router.register('category', CategoryViewSet)
router.register('cardItem', CardItemViewSet)
router.register('card', CardViewSet)
router.register('car_picture', Car_pictureViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
     path('', include(router.urls)),
     path('admin/',admin.site.urls),
     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
     path('register/', RegisterAPI.as_view(), name='register'),
     path('api/login/', LoginAPI.as_view(), name='login'),
     path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
     path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall')

]
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
