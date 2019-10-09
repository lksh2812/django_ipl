from rest_framework import serializers

from .models import Matches, Delivery

class MatchSerializer(serializers.HyperlinkedModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = Matches
        count_matches = serializers.SerializerMethodField()
        # fields = ('season', 'city', 'date', 'team1', 'team2', 'toss_winner', 'toss_decision', 'result', 'dl_applied', 'winner', 'win_by_runs', 'win_by_wickets', 'player_of_match', 'venue', 'umpire1', 'umpire2', 'umpire3')

        fields = ('season')

        def get_count_matches(self, obj):
            return obj.season.count()
