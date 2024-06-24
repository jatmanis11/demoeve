from django.contrib import admin
from django.db.models import Sum
from .models import Player, Team, Match, PlayerScore

class PlayerScoreInline(admin.TabularInline):
    model = PlayerScore
    extra = 1

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('ign', 'uid', 'email', 'phone_no', 'college_name', 'team', 'total_tournament_score')
    search_fields = ('ign', 'uid', 'email', 'team__name')
    inlines = [PlayerScoreInline]

    def total_tournament_score(self, obj):
        return obj.total_tournament_score()
    total_tournament_score.short_description = 'Total Tournament Score'

class PlayerInline(admin.TabularInline):
    model = Player
    extra = 1
    max_num = 6

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_score', "player_list")
    inlines = [PlayerInline]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(total_score=Sum('players__scores__score'))

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

admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(PlayerScore, PlayerScoreAdmin)
