from rest_framework import routers
from .views import VotacionView, VotoDelPublicoView

router_granConexion = routers.DefaultRouter()

router_granConexion.register('votacion',VotacionView,'get-votacion')
router_granConexion.register('voto',VotoDelPublicoView,'post-voto')

urlpatterns = router_granConexion.urls
