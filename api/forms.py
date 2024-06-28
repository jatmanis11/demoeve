from django import forms
from heff.models import Match, Team, Player, PlayerScore

class MatchSelectionForm(forms.Form):
    selected_match = forms.ModelChoiceField(queryset=Match.objects.all(), label='Select Match')
    print(selected_match)
class TeamSelectionForm(forms.Form):
    selected_team = forms.ModelChoiceField(queryset=Team.objects.all(), label='Select Team')
    print(selected_team)
    def __init__(self, *args, match=None, **kwargs):
        super().__init__(*args, **kwargs)
        print(match.name,"weewewewewew")
        print(Team.objects.filter(match_pp=match.id))
        if match:
            # Assuming 'match' is a ForeignKey field on the Team model
            self.fields['selected_team'].queryset = Team.objects.filter(match_pp=match)
class PlayerScoreForm(forms.Form):
    score = forms.IntegerField(label='Score')
    class Meta:
        model = PlayerScore
        fields = ['player_id', 'score'] 
    def __init__(self, *args, **kwargs):
        player_id = kwargs.pop('player_id', None)
        super().__init__(*args, **kwargs)
        if player_id:
            self.player_id = player_id

    def save_score(self):
        score = self.cleaned_data['score']
        player = Player.objects.get(id=self.player_id)
        # Create or update PlayerScore instance for the selected match
        # Example logic:
        # player_score, created = PlayerScore.objects.get_or_create(player=player, match=self.match)
        # player_score.score += score
        # player_score.save()