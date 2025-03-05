from django.db import models


class Game(models.Model):
    _uuid = models.UUIDField(name="uuid")


class User(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.TextField(primary_key=True)
    resources = models.JSONField(null=True)


class Shops(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    name = models.TextField()
    resources = models.JSONField(null=True)


class Logs(models.Model):
    comment = models.TextField()
    player_name = models.ForeignKey(User, on_delete=models.CASCADE)
    shop_name = models.ForeignKey(Shops, on_delete=models.CASCADE, null=True)
    resources_changed = models.JSONField()
