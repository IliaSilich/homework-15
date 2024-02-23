from django.db import models
from django.utils import timezone
from Tanks.models import Tanks


class Players(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username


class PlayerVehicles(models.Model):
    id = models.AutoField(primary_key=True)
    player = models.ForeignKey(Players, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Tanks, on_delete=models.CASCADE)
    experience_points = models.IntegerField()

    def __str__(self):
        return f"{self.player.name}'s {self.vehicle.name}"
