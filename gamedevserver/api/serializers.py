from rest_framework import serializers
from .models import User, Logs, Shops, Game


class BaseMeta:
    model = None
    fields = '__all__'
    extra_kwargs = {
        'game': {'required': False}
    }

class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta(BaseMeta):
        model = User



class LogsSerializer(serializers.ModelSerializer):
    class Meta(BaseMeta):
        model = Logs


class ShopsSerializer(serializers.ModelSerializer):
    class Meta(BaseMeta):
        model = Shops
        extra_kwargs = {
            'game': {'required': False},
            'user': {'required': False}
        }
