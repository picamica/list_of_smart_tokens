from django.shortcuts import render
from django.http import HttpResponse
from .models import bscToken, network


def index(request):

  num_tokens = bscToken.objects.all()
  num_networks = network.objects.all()

  context = {
    'num_tokens': num_tokens,
    'num_networks': num_networks,
  }

  return render(request, 'index.html', context=context)
# Create your views here.
