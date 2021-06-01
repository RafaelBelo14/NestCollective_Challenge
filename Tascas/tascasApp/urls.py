from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
      path('', views.index, name='index'),
      path('detalhes/<int:tasca_id>', views.detalhes, name='detalhes'),
      path('delete/<int:tasca_id>', views.delete, name='delete'),
      path('', views.create, name='create'),
]