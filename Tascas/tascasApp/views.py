from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tasca

# Create your views here.
def index(request):
      tasca = Tasca.objects.all()
      context = {
            'objectList': tasca
      }
      return render(request, "../templates/html/index.html", context)

def detalhes(request, tasca_id):
      tasca = Tasca.objects.get(pk=tasca_id)
      context = {
            'object': tasca
      }
      return render(request, "../templates/html/edit.html", context)

def delete(request, tasca_id):
      tasca = Tasca.objects.get(pk=tasca_id)
      tasca.delete()
      return redirect("../../")

def create(request):
      return render(request, "../templates/html/create.html")
