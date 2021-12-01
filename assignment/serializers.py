from rest_framework.serializers import ModelSerializer, CharField, IntegerField
from .models import Assignment

class AssignmentSerializer(ModelSerializer):

    musicGenre = CharField(source="music_genre")
    dailyPracticeTime = IntegerField(source="daily_practice_time")
    daysPracticed = IntegerField(source="days_practiced")

    class Meta:
        model = Assignment
        fields = [
            'id', 
            'title', 
            'description', 
            'musicGenre', 
            'dailyPracticeTime', 
            'days', 
            'daysPracticed'
        ]
 