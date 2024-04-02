from rest_framework import routers
from .views import PlayerView, GameView, PlayerInGameView

router_hazvir = routers.DefaultRouter()

router_hazvir.register('players',PlayerView,'get-players')
router_hazvir.register('games',GameView,'get-games')
router_hazvir.register('players-in-game',PlayerInGameView,'get-players-in-game')

urlpatterns = router_hazvir.urls
