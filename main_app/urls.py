from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('prompts/', views.prompts_index, name='prompts_index'),
  path('prompts/<int:prompt_id>/', views.prompts_detail, name='prompts_detail'),
]