from django.db import models


class Tanks(models.Model):
    id = models.AutoField(primary_key=True)
    tank_name = models.CharField(max_length=255)
    tank_type = models.CharField(max_length=50)
    tank_description = models.TextField()
    damage_points = models.IntegerField()
    armor_points = models.IntegerField()
    speed = models.FloatField()
    cost = models.IntegerField()

    def __str__(self):
        return self.tank_name


# Create your models here.
