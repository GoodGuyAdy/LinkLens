from django.db import models


class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    email = models.EmailField()
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
