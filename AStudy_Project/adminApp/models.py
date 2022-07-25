from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

# Create your models here.
class user(AbstractUser):
    pass
    #user_name = models.CharField(max_length=50)
    #email = models.CharField(max_length=100)
    #password = models.CharField(max_length=100)

class topics (models.Model):
    topic_name = models.CharField(max_length=50)

class subtopics (models.Model):
    topic_id = models.ForeignKey(topics , max_length=50  , on_delete=models.CASCADE , related_name='topic_id')
    subtopic_name = models.CharField(max_length=50)
    iframe = models.CharField(max_length=1000)


class content (models.Model):
    subtopic_id = models.ForeignKey(subtopics , max_length=50  , on_delete=models.CASCADE , related_name='subtopic_id')
    data = models.CharField(max_length = 1000)

