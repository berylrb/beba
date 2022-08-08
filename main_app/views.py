from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Prompt
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.http import HttpResponse


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

class Home(LoginView):
  template_name = 'home.html'


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cats_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)


class PromptCreate(LoginRequiredMixin, CreateView):
  model = Prompt
  fields = ['topic', 'question']
  success_url = '/prompts/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class PromptUpdate(LoginRequiredMixin, UpdateView):
  model = Prompt
  fields = ['topic', 'question']

class PromptDelete(LoginRequiredMixin, DeleteView):
  model = Prompt
  success_url = '/prompts/'



# def home(request):
#   return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')


def home(request):
  return render(request, 'home.html')

@login_required
def prompts_index(request):
  prompts = Prompt.objects.filter(user=request.user)
  return render(request, 'prompts/index.html', { 'prompts': prompts })

@login_required
def prompts_detail(request, prompt_id):
  prompt = Prompt.objects.get(id=prompt_id)
  return render(request, 'prompts/detail.html', { 'prompt': prompt })