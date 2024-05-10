from rest_framework import routers
from .views import PlayerView, GameView, PlayerInGameView, PostView

router_hazvir = routers.DefaultRouter()

router_hazvir.register('players',PlayerView,'get-players')
router_hazvir.register('games',GameView,'get-games')
router_hazvir.register('players-in-game',PlayerInGameView,'get-players-in-game')
router_hazvir.register('posts',PostView,'get-posts')

urlpatterns = router_hazvir.urls
