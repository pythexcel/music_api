from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Assignment

class AssignmentSerializer(ModelSerializer):
    musicGenre = SerializerMethodField()
    dailyPracticeTime = SerializerMethodField()
    daysPracticed = SerializerMethodField()

    class Meta:
        model = Assignment
        fields = ['title', 'description', 'musicGenre', 'dailyPracticeTime', 'days', 'daysPracticed']

    def get_musicGenre(self, obj):
        return obj.music_genre

    def get_dailyPracticeTime(self, obj):
        return obj.daily_practice_time

    def get_daysPracticed(self, obj):
        return obj.days_practiced