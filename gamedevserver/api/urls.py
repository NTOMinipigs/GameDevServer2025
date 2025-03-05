from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

from .views import UserViewSet, LogsViewSet, ShopsViewSet

router = DefaultRouter()
router.register(r'players', UserViewSet, basename="user")
router.register(r'logs', LogsViewSet, basename="logs")

players_router = NestedDefaultRouter(router, r'players', lookup="name")
players_router.register(r'shops', ShopsViewSet, basename="player-shops")
players_router.register(r'logs', LogsViewSet, basename="player-logs")

shoplogs_router = NestedDefaultRouter(players_router, r'shops', lookup="shop")
shoplogs_router.register(r'logs', LogsViewSet, basename="shop-logs")

urlpatterns = [
    path('', include(router.urls)),
    path('', include(players_router.urls)),
    path('', include(shoplogs_router.urls)),
]
