from django.db import models

class Assignment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    musicGenre = models.CharField(max_length=50)
    dailyPracticeTime = models.IntegerField()
    days = models.IntegerField()
    daysPracticed = models.IntegerField()

    def __str__(self):
        return self.title