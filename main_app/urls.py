from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('prompts/', views.prompts_index, name='prompts_index'),
  path('prompts/<int:prompt_id>/', views.prompts_detail, name='prompts_detail'),
  path('prompts/create/', views.PromptCreate.as_view(), name='prompts_create'),
  path('prompts/<int:pk>/update/', views.PromptUpdate.as_view(), name='prompts_update'),
  path('prompts/<int:pk>/delete/', views.PromptDelete.as_view(), name='prompts_delete'),
  path('accounts/signup/', views.signup, name='signup'),
]