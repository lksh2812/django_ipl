from rest_framework import serializers

from .models import Matches, Delivery

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matches
        count_matches = serializers.SerializerMethodField()
        fields = '__all__'

        def get_count_matches(self, obj):
            return obj.season.count()


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'
