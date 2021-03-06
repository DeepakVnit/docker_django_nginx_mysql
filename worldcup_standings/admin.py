from django.contrib import admin

from .models import Cards
from .models import Goals
from .models import Matches
from .models import Players
from .models import Teams


# admin.site.register(Teams)
# admin.site.register(Matches)
# admin.site.register(Goals)
# admin.site.register(Players)


@admin.register(Matches)
class MatchesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'result',
        'team1',
        'team2',
        'score1',
        'score2',
        'penality1',
        'penality2',
        'gametime',
        'venue'
    )
    ordering = ('gametime',)
    search_fields = ['team1__name', 'team2__name']


@admin.register(Teams)
class TeamsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'short_name',
        'id',
        'flag',
        'group'
    )
    ordering = ('name',)
    search_fields = ['name']


@admin.register(Goals)
class GoalsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'time',
        'get_scorer_name',
        'assist_name',
        'match',
        'allowed',
        'awarded_team_name',
        'owngoal',
        'is_penalty'
    )
    ordering = ('id',)

    def get_scorer_name(self, obj):
        return obj.scorer.name

    def assist_name(self, obj):
        return obj.assist.name

    def awarded_team_name(self, obj):
        return obj.awarded_team.name

    def match_id(self, obj):
        return obj.match.id

    search_fields = ['scorer__name']
    raw_id_fields = ['scorer', 'assist', 'match',]


@admin.register(Players)
class PlayersAdmin(admin.ModelAdmin):
    list_display = (
        'team',
        'name',
        'id',
        'rating',
        'position',
    )
    ordering = ('team', 'name')
    search_fields = ['name']


@admin.register(Cards)
class GoalsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'match',
        'card_type',
        'player',
        'time'
    )

    ordering = ('id',)

    search_fields = ['player__name']
    raw_id_fields = ['player',]