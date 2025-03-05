import uuid

from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, Logs, Shops, Game
from .serializers import UserSerializer, LogsSerializer, ShopsSerializer


class BaseViewSet(viewsets.ModelViewSet):
    model = None
    http_method_names = ['get', 'post', 'put', 'delete']


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    model = User

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data.copy()
        data["name"] = self.kwargs.get("pk")
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def get_queryset(self):
        game = Game.objects.get(uuid=self.kwargs.get("game_uuid"))
        return self.model.objects.filter(game=game)

    def perform_create(self, serializer):
        game = Game.objects.get(uuid=self.kwargs.get("game_uuid"))
        serializer.save(game=game)


class LogsViewSet(BaseViewSet):
    serializer_class = LogsSerializer
    model = Logs

    def get_queryset(self):
        username = self.kwargs.get("name_pk")
        shop_name = self.kwargs.get("shop_pk")
        if username:
            query_set = Logs.objects.filter(player_name=User.objects.get(name=self.kwargs.get("name_pk")))
            if shop_name:
                query_set.filter(shop_name=Shops.objects.get(name=shop_name))

            return query_set

        return Logs.objects.all()


class ShopsViewSet(BaseViewSet):
    serializer_class = ShopsSerializer
    model = Shops

    def get_queryset(self):
        return Shops.objects.filter(user=User.objects.get(name=self.kwargs.get("name_pk")))

    def perform_create(self, serializer):
        user = User.objects.get(name=self.kwargs.get("name_pk"))
        serializer.save(user=user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data.copy()
        data["name"] = self.kwargs.get("name_pk")
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)



class CreateGame(APIView):
    def post(self, request: Request):

        new_game_uuid = uuid.uuid4()
        game = Game()
        game.uuid = new_game_uuid
        game.save()
        return Response({"team_name": "some_team", "uuid": new_game_uuid})
