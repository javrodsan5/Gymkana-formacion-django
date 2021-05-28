from rest_framework import serializers
from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['title', 'subtitle', 'body', 'start_date', 'end_date']

    def validate(self, data):
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError(
                "The end date must be after the start one.")
        return data
