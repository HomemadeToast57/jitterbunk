from django.utils import timezone
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    photo = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now)

class Bunk(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    pub_date = models.DateTimeField('date published',default=timezone.now)