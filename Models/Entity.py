from django.db import models


class Entity(models.Model):
    entity_id = models.BigAutoField(primary_key=True)
    entity_type = models.CharField(max_length=100)
    entity_name = models.CharField(max_length=500)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
