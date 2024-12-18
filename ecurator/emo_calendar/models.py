from django.db import models
from django.conf import settings

class Emotion(models.Model):
    EMOTION_TYPE = [
        ('happy', 'happy'),
        ('sad', 'sad'),
        ('surprised', 'surprised'),
        ('loving', 'loving'),
        ('sleepy', 'sleepy'),
        ('nervous', 'nervous'),
        ('pensive', 'pensive'),
        ('relieved', 'relieved'),
        ('joyful', 'joyful'),
    ]

    name = models.CharField(max_length=20, choices=EMOTION_TYPE)

    def __str__(self):
        return f"{self.name}"

class Music(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

class Movie(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100, default="Unknown")

    def __str__(self):
        return f"{self.title}"
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

class MyMoodHistory(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, related_name="moodhistories")
    emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE)
    date = models.DateField()