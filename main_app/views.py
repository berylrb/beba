from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Prompt
from django.http import HttpResponse


# class Prompt:
#   def __init__(self, topic, question):
#     self.topic = topic
#     self.question = question

# prompts = [
#   Prompt('Leadership', 'Tell me about a time you exhibited leadership.'),
#   Prompt('Teamwork', 'Tell me about a time you had to work as a team.'),
#   Prompt('Failure', 'Tell me about a time you failed.'),
#   Prompt('Adaptability', 'Tell me about a time you overcame an obstacle.')
# ]

class PromptCreate(CreateView):
  model = Prompt
  fields = ['topic', 'question']
  success_url = '/prompts/'

class PromptUpdate(UpdateView):
  model = Prompt
  fields = ['topic', 'question']

class PromptDelete(DeleteView):
  model = Prompt
  success_url = '/prompts/'



def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')


def home(request):
  return render(request, 'home.html')

def prompts_index(request):
  prompts = Prompt.objects.all()
  return render(request, 'prompts/index.html', { 'prompts': prompts })

def prompts_detail(request, prompt_id):
  prompt = Prompt.objects.get(id=prompt_id)
  return render(request, 'prompts/detail.html', { 'prompt': prompt })