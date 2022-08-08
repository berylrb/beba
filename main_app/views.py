from django.shortcuts import render

from django.http import HttpResponse


class Prompt:
  def __init__(self, topic, question):
    self.topic = topic
    self.question = question

prompts = [
  Prompt('Leadership', 'Tell me about a time you exhibited leadership.'),
  Prompt('Teamwork', 'Tell me about a time you had to work as a team.'),
  Prompt('Failure', 'Tell me about a time you failed.'),
  Prompt('Adaptability', 'Tell me about a time you overcame an obstacle.')
]

def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')

def prompts_index(request):
  return render(request, 'prompts/index.html', { 'prompts': prompts })

def home(request):
  return render(request, 'home.html')