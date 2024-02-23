from django.db import models
from players.models import Players


class Achievements(models.Model):
    id = models.AutoField(primary_key=True)
    player = models.ForeignKey(Players, on_delete=models.CASCADE)
    achievement_name = models.CharField(max_length=255)
    achievement_description = models.TextField()
    date_achieved = models.DateField()

    def __str__(self):
        return f"{self.player.name}'s achievement: {self.achievement_name}"

    class PlayerRanking(models.Model):
        id = models.AutoField(primary_key=True)
        player = models.ForeignKey(Players, on_delete=models.CASCADE)
        ranking_points = models.IntegerField()

        def __str__(self):
            return f"{self.player.name}'s ranking points: {self.ranking_points}"
