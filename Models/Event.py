from django.db import models
from Models.User import User
from Models.Entity import Entity


class Event(models.Model):
    class EventType(models.TextChoices):
        VIEWED = "viewed", "viewed"
        LIKED = "liked", "liked"
        HATED = "hated", "hated"
        FOLLOWED = "followed", "followed"
        BLOCKED = "blocked", "blocked"

    event_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=20, choices=EventType.choices)
    timestamp = models.DateTimeField(auto_now_add=True)
