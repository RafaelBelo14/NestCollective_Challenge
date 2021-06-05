from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
      path('', views.index, name='index'),
      path('detalhes/<int:tasca_id>', views.detalhes, name='detalhes'),
      path('delete/<int:tasca_id>', views.delete, name='delete'),
      path('create/', views.goToCreate, name='create'),
      path('registTasca/', views.create, name='registTasca'),
      path('edit/<int:tasca_id>', views.goToEdit, name='edit'),
      path('editTasca/<int:tasca_id>', views.edit, name='editTasca')
]