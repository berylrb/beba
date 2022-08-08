from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class Qualities(models.Model):
  quality = models.CharField(max_length=50)

  def __str__(self):
    return self.asked

  def get_absolute_url(self):
    return reverse('used_detail', kwargs={'pk': self.id})

class Prompt(models.Model):
  topic = models.CharField(max_length=100)
  question = models.CharField(max_length=250)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.topic

  def get_absolute_url(self):
    return reverse('prompts_detail', kwargs={'prompt_id': self.id})


class Car(models.Model):
  date = models.DateField('Response date')
  challenge = models.CharField(max_length=2250)
  action = models.CharField(max_length=2250)
  response = models.CharField(max_length=2250)

  prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_car_display()} on {self.date}"