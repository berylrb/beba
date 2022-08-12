from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Prompt, Car
# , Qualities
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CarForm
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
      return redirect('prompts_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

# class QualitiesCreate(CreateView):
#   model = Qualities
#   fields = '__all__'

# class QualitiesUpdate(UpdateView):
#   model = Qualities
#   fields = ['quality']

# class QualitiesDelete(DeleteView):
#   model = Qualities
#   success_url = '/qualities/'

# class QualitiesList(ListView):
#   model = Qualities

# class QualitiesDetail(DetailView):
#   model = Qualities

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
  cars = Car.objects.all()
  car_form = CarForm()
  return render(request, 'prompts/detail.html', { 'prompt': prompt, 'car_form': car_form, 'cars': cars })

def add_car(request, prompt_id):
  form = CarForm(request.POST)
  if form.is_valid():
    new_car = form.save(commit=False)
    new_car.prompt_id = prompt_id
    new_car.save()
  return redirect('prompts_detail', prompt_id=prompt_id)