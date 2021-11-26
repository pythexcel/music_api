from django.db import models

class Assignment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    music_genre = models.CharField(max_length=50)
    daily_practice_time = models.IntegerField()
    days = models.IntegerField()
    days_practiced = models.IntegerField()

    def __str__(self):
        return self.title