from django.db import models
from django.db.models import Sum

class Match(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    #class_instance = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='objects')
    def __str__(self):
        return self.name
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    match_pp = models.ManyToManyField(Match, related_name='teams_participated', blank=True)

    def update_matches_participation(self):
        from django.db.models import Count

        # Get all matches where at least one player from this team participated
        participated_matches = Match.objects.filter(players__team=self).annotate(num_players=Count('players')).filter(num_players__gt=0)

        # Clear current participation and set new participation
        self.matches_participated.clear()
        self.matches_participated.add(*participated_matches)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.update_matches_participation()
    def match_scores(self):
        match_scores = PlayerScore.objects.filter(player__team=self).values('match__name').annotate(team_score=Sum('score')).order_by('match__name')
        return match_scores
    """def total_score(self):
        return sum(player.total_tournament_score() for player in self.players.all())
    """
    def team_match_score(self):
        return sum(player.match_scores() for player in self.players.all())

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
    def match_scores(self):
        return self.scores.all()

    def total_tournament_score(self):
        return self.scores.aggregate(total=Sum('score'))['total'] or 0

    def __str__(self):
        return f"{self.player_name} ({self.ign})"



class PlayerScore(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='scores')
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='scores')
    score = models.IntegerField()
    
    class Meta:
        unique_together = ('player', 'match')

    def __str__(self):
        return f"{self.player.player_name} - {self.match.name} - {self.score}"

"""class MatchScore(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='match_scores')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='match_scores')
    score = models.IntegerField()

    class Meta:
        unique_together = ('match', 'team')

    def __str__(self):
        return f"{self.match.name} - {self.team.name} - {self.score}" """