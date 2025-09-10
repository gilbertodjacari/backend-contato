from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContatoViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register(r'contatos', ContatoViewSet, basename='contato')

schema_view = get_schema_view(
   openapi.Info(
      title="API de Contatos",
      default_version='v1',
      description="API para gerenciamento de formulários de contato",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
