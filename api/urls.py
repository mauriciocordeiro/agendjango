from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'api/pessoas', views.PessoaViewSet)
router.register(r'api/enderecos', views.EnderecoViewSet)
router.register(r'api/telefones', views.TelefoneViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
# urlpatterns = router.urls