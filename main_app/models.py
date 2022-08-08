from django.db import models

# Create your models here.
from django.db import models

class Prompt(models.Model):
  topic = models.CharField(max_length=100)
  question = models.CharField(max_length=250)

  def __str__(self):
    return self.topic