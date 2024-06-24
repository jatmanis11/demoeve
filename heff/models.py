from django.db import models
from django.db.models import Sum


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def total_score(self):
        return sum(player.total_tournament_score() for player in self.players.all())

    def player_list(self):
        return ", ".join(player.player_name for player in self.players.all())

    def __str__(self):
        return self.name

class Player(models.Model):
    player_name = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    uid = models.CharField(max_length=50, unique=True)
    ign = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=15)
    college_name = models.CharField(max_length=100)

    def total_tournament_score(self):
        return self.scores.aggregate(total=Sum('score'))['total'] or 0

    def __str__(self):
        return f"{self.player_name} ({self.ign})"

class Match(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.name

class PlayerScore(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='scores')
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='scores')
    score = models.IntegerField()

    class Meta:
        unique_together = ('player', 'match')

    def __str__(self):
        return f"{self.player.player_name} - {self.match.name} - {self.score}"
