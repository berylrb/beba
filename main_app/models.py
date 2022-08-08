from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Prompt(models.Model):
  topic = models.CharField(max_length=100)
  question = models.CharField(max_length=250)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.topic

  def get_absolute_url(self):
    return reverse('prompts_detail', kwargs={'prompt_id': self.id})