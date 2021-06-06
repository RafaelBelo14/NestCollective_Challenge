from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.db.models import Q
from .models import Tasca

# Create your views here.
def index(request):
      searched = request.POST.get('searched', None)

      if searched:
            tascas = Tasca.objects.filter(Q(name__contains=searched) | Q(address__contains=searched))

            if not tascas:    
                  print("Nothing")
                  tasca = Tasca.objects.all()
                  context = {
                        'objectList': tasca
                  }
            else:
                  print("Something")
                  context = {
                        'objectList': tascas
                  } 
      
      else:
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
      return render(request, "../templates/html/details.html", context)

def delete(request, tasca_id):
      tasca = Tasca.objects.get(pk=tasca_id)
      tasca.delete()
      return redirect("../../")

def goToCreate(request):
      return render(request, "../templates/html/create.html")

def create(request):
      n = request.POST.get('name')
      a = request.POST.get('address')
      r = request.POST.get('rating')
      i = request.FILES['imageTasca']

      o_ref = Tasca(name = n, address = a, rating = r, tascaPicture = i)
      o_ref.save()

      return redirect("../../")

def goToEdit(request, tasca_id):
      tasca = Tasca.objects.get(pk=tasca_id)
      context = {
            'object': tasca
      }
      return render(request, "../templates/html/edit.html", context)

def edit(request, tasca_id):
      tasca = Tasca.objects.get(pk=tasca_id)
      n = request.POST.get('name')
      a = request.POST.get('address')
      r = request.POST.get('rating')
      if ('imageTasca' in request.FILES):
            i = request.FILES['imageTasca']

            if (i != tasca.tascaPicture):
                  tasca.tascaPicture = i

      if (n != tasca.name):
            tasca.name = n
      if (a != tasca.address):
            tasca.address = a
      if (r != tasca.rating):
            tasca.rating = r
      
      tasca.save()

      return redirect("../../")

