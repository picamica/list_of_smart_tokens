from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import bscToken, network
from datetime import datetime, timedelta

def index(request):

  num_tokens = bscToken.objects.all()
  num_networks = network.objects.all()

  context = {
    'num_tokens': num_tokens,
    'num_networks': num_networks,
  }

  return render(request, 'index.html', context=context)


def bsc_tokens_view(request):
  time_threshold = datetime.now() - timedelta(hours=24)
  bscTokens = bscToken.objects.all().filter(networkName=1).filter(created_on__gte=time_threshold)
  tokensList = []
  for i in bscTokens:
    item = {
      'name': i.name,
      'symbol': i.symbol,
      'address': i.address,
      'Scanner': i.scannerLink,
      'Exchange': i.exchangerLink,
      'created': i.created_on
    }
    tokensList.append(item)
  return JsonResponse({'tokens': tokensList})

def eth_tokens_view(request):
  ethTokens = bscToken.objects.all().filter(networkName=2)
  tokensList = []
  for i in ethTokens:
    item = {
      'name': i.name,
      'symbol': i.symbol,
      'address': i.address,
      'Scanner': i.scannerLink,
      'Exchange': i.exchangerLink,
    }
    tokensList.append(item)
  return JsonResponse({'tokens': tokensList})

def matic_tokens_view(request):
  maticTokens = bscToken.objects.all().filter(networkName=3)
  tokensList = []
  for i in maticTokens:
    item = {
      'name': i.name,
      'symbol': i.symbol,
      'address': i.address,
      'Scanner': i.scannerLink,
      'Exchange': i.exchangerLink,
    }
    tokensList.append(item)
  return JsonResponse({'tokens': tokensList})

def ftm_tokens_view(request):
  ftmTokens = bscToken.objects.all().filter(networkName=4)
  tokensList = []
  for i in ftmTokens:
    item = {
      'name': i.name,
      'symbol': i.symbol,
      'address': i.address,
      'Scanner': i.scannerLink,
      'Exchange': i.exchangerLink,
    }
    tokensList.append(item)
  return JsonResponse({'tokens': tokensList})

# Create your views here.
