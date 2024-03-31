from rest_framework import routers
from .views import PlayerView, GameView

router_hazvir = routers.DefaultRouter()

router_hazvir.register('players',PlayerView,'get-players')
router_hazvir.register('games',GameView,'get-games')

urlpatterns = router_hazvir.urls
