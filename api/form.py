from django.shortcuts import render, redirect
from heff.models import Match, Team, Player, PlayerScore
from .forms import MatchSelectionForm, TeamSelectionForm, PlayerScoreForm

def match_selection_view(request):
    if request.method == 'POST':
        match_form = MatchSelectionForm(request.POST)
        #print(match_form)
        if match_form.is_valid():
            selected_match = match_form.cleaned_data['selected_match']
            request.session['selected_match'] = selected_match.id
            return redirect('team_selection')
    else:
        match_form = MatchSelectionForm()
    return render(request, 'match_selection.html', {'match_form': match_form})

def team_selection_view(request):
    selected_match_id = request.session.get('selected_match')
    selected_match = Match.objects.get(id=selected_match_id)
    #print(selected_match)
    if request.method == 'POST':
        team_form = TeamSelectionForm(request.POST, match=selected_match)
        if team_form.is_valid():
            selected_team = team_form.cleaned_data['selected_team']
            request.session['selected_team'] = selected_team.id
            return redirect('player_scores')
    else:
        team_form = TeamSelectionForm(match=selected_match)
    return render(request, 'team_selection.html', {'team_form': team_form})

def player_scores_view(request):
    selected_match_id = request.session.get('selected_match')
    selected_team_id = request.session.get('selected_team')
    
    selected_match = Match.objects.get(id=selected_match_id)
    selected_team = Team.objects.get(id=selected_team_id)
    players = Player.objects.filter(team=selected_team)
    
    if request.method == 'POST':
        player_score_form = PlayerScoreForm(request.POST)
        if player_score_form.is_valid():
            player_id= 1
            player_id = player_score_form.cleaned_data['player_id']
            score = player_score_form.cleaned_data['score']
            
            # Save or update player score for the selected match
            player = Player.objects.get(id=player_id)
            player_score, created = PlayerScore.objects.get_or_create(player=player, match=selected_match)
            player_score.score += score
            player_score.save()
            return redirect('player_scores')
    else:
        player_score_form = PlayerScoreForm()
    
    return render(request, 'player_scores.html', {
        'selected_match': selected_match,
        'selected_team': selected_team,
        'players': players,
        'player_score_form': player_score_form,
    })
