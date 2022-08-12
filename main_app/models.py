from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# class Qualities(models.Model):
#   quality = models.CharField(max_length=50)

#   def __str__(self):
#     return self.quality

#   def get_absolute_url(self):
#     return reverse('qualities_detail', kwargs={'quality_id': self.id})

# PICS = (
#   ('static/images/alien2.png', 'alien'),
#   ('static/images/stars.png', 'stars'),
#   ('static/images/day-and-night.png', 'day/night'),
#   ('static/images/galaxy.png', 'galaxy'),
#   ('static/images/abduction.png', 'ufo'),
#   ('static/images/spacedog.png', 'space dog'),
#   ('static/images/meteor.png', 'meteor')
# )


class Prompt(models.Model):
  topic = models.CharField(max_length=100)
  question = models.CharField(max_length=250)
  # pics = models.CharField(
  #   max_length=255,
  #   choices=PICS,
  #   default=PICS[0][0]
  # )
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.topic

  def get_absolute_url(self):
    return reverse('prompt_detail', kwargs={'prompt_id': self.id})


class Car(models.Model):
  date = models.DateField('Response date')
  challenge = models.CharField(max_length=2250)
  action = models.CharField(max_length=2250)
  response = models.CharField(max_length=2250)

  prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.challenge}, {self.action}, {self.response} on {self.date}"