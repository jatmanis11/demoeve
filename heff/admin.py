from django.contrib import admin
from django.db.models import Sum
from .models import Player, Team, Match, PlayerScore#, MatchScore

class PlayerScoreInline(admin.TabularInline):
    model = PlayerScore
    extra = 1
"""class MatchScoreInline(admin.TabularInline):
    model = MatchScore
    extra = 1"""

class PlayerAdmin(admin.ModelAdmin):
    list_display = ("player_name",'team','ign', 'uid' ,"display_match_scores", 'total_tournament_score', 'email', 'phone_no', 'college_name')
    search_fields = ('ign', 'uid', 'email', 'team__name')
    inlines = [PlayerScoreInline]

    def display_match_scores(self, obj):
        match_scores = obj.match_scores()
        return ", ".join([f"{score.match.name}: {score.score}" for score in match_scores])
    display_match_scores.short_description = 'Match Scores'

    def total_tournament_score(self, obj):
        return obj.total_tournament_score()
    total_tournament_score.short_description = 'Total Tournament Score'

class PlayerInline(admin.TabularInline):
    model = Player
    extra = 1
    max_num = 6

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_score',"get_matches_participated", "player_list", "display_match_scores")
    inlines = [PlayerInline]
    def get_matches_participated(self, obj):
        return ", ".join([match.name for match in obj.match_pp.all()])

    get_matches_participated.short_description = 'Matches Participated'
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(total_score=Sum('players__scores__score'))
    def player_list(self, obj):
        return obj.player_list()
    player_list.short_description = 'Players'

    def display_match_scores(self, obj):
        match_scores = obj.match_scores()
        return "\n ".join([f"{score['match__name']}: {score['team_score']} " for score in match_scores])
    display_match_scores.short_description = 'Match Scores'


    def total_score(self, obj):
        return obj.total_score
    total_score.admin_order_field = 'total_score'
    total_score.short_description = 'Total Team Score'

class MatchAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    search_fields = ('name',)

class PlayerScoreAdmin(admin.ModelAdmin):
    list_display = ('player', 'match', 'score')
    search_fields = ('player__ign', 'match__name')
"""class matchscoreAdmin(admin.ModelAdmin):
    list_display= ("player","match")
"""
"""class MatchScoreAdmin(admin.ModelAdmin):
    list_display = ('match', 'team', 'score')
    search_fields = ('match__name', 'team__name')"""



admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(PlayerScore, PlayerScoreAdmin)
#admin.site.register(MatchScore, MatchScoreAdmin)