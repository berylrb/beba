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
  path('prompts/<int:prompt_id>/add_car/', views.add_car, name='add_car'),
]
#   path('qualities/create/', views.QualitiesCreate.as_view(), name='qualities_create'),
#   path('qualities/', views.QualitiesList.as_view(), name='qualities_index'),
#   path('qualities/<int:quality_id>/', views.QualitiesDetail.as_view(), name='qualities_detail'),
#   path('qualities/<int:quality_id>/update/', views.QualitiesUpdate.as_view(), name='qualities_update'),
#   path('qualities/<int:quality_id>/delete/', views.QualitiesDelete.as_view(), name='qualities_delete'),
# ]