from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import bscToken, network
from datetime import datetime, timedelta, timezone

def index(request):

  num_tokens = bscToken.objects.all()
  num_networks = network.objects.all()

  context = {
    'num_tokens': num_tokens,
    'num_networks': num_networks,
  }

  return render(request, 'index.html', context=context)


def bsc_tokens_view(request, num_tokens):
  time_threshold = datetime.now() - timedelta(hours=24)
  bscTokens = bscToken.objects.all().filter(networkName=1).filter(created_on__gte=time_threshold).order_by('-created_on')
  size = bscTokens.count()

  if num_tokens == size:
    lower = 0
    upper = size
  else:
    visible = 20
    upper = num_tokens
    lower = upper - visible

  tokensList = []
  for i in bscTokens:
    time_diff = datetime.now(timezone.utc) - i.created_on
    item = {
      'name': i.name,
      'symbol': i.symbol,
      'address': i.address,
      'Scanner': i.scannerLink,
      'Exchange': i.exchangerLink,
      'age' : round(time_diff.total_seconds(), 0)
    }
    tokensList.append(item)
  return JsonResponse({'tokens': tokensList[lower:upper], 'size':size})

def eth_tokens_view(request, num_tokens):
  time_threshold = datetime.now() - timedelta(hours=24)
  ethTokens = bscToken.objects.all().filter(networkName=2).filter(created_on__gte=time_threshold).order_by('-created_on')
  size = ethTokens.count()

  if num_tokens == size:
    lower = 0
    upper = size
  else:
    visible = 20
    upper = num_tokens
    lower = upper - visible

  tokensList = []
  for i in ethTokens:
    time_diff = datetime.now(timezone.utc) - i.created_on
    item = {
      'name': i.name,
      'symbol': i.symbol,
      'address': i.address,
      'Scanner': i.scannerLink,
      'Exchange': i.exchangerLink,
      'age' : round(time_diff.total_seconds(), 0)
    }
    tokensList.append(item)
  return JsonResponse({'tokens': tokensList[lower:upper], 'size': size})

def matic_tokens_view(request, num_tokens):
  time_threshold = datetime.now() - timedelta(hours=24)
  maticTokens = bscToken.objects.all().filter(networkName=3).filter(created_on__gte=time_threshold).order_by('-created_on')
  size = maticTokens.count()

  if num_tokens == size:
    lower = 0
    upper = size
  else:
    visible = 20
    upper = num_tokens
    lower = upper - visible

  tokensList = []
  for i in maticTokens:
    time_diff = datetime.now(timezone.utc) - i.created_on
    item = {
      'name': i.name,
      'symbol': i.symbol,
      'address': i.address,
      'Scanner': i.scannerLink,
      'Exchange': i.exchangerLink,
      'age' : round(time_diff.total_seconds(), 0)
    }
    tokensList.append(item)
  return JsonResponse({'tokens': tokensList[lower:upper], 'size': size})

def ftm_tokens_view(request, num_tokens):
  time_threshold = datetime.now() - timedelta(hours=24)
  ftmTokens = bscToken.objects.all().filter(networkName=4).filter(created_on__gte=time_threshold).order_by('-created_on')
  size = ftmTokens.count()

  if num_tokens == size:
    lower = 0
    upper = size
  else:
    visible = 20
    upper = num_tokens
    lower = upper - visible

  tokensList = []
  tokensList = []
  for i in ftmTokens:
    time_diff = datetime.now(timezone.utc) - i.created_on
    item = {
      'name': i.name,
      'symbol': i.symbol,
      'address': i.address,
      'Scanner': i.scannerLink,
      'Exchange': i.exchangerLink,
      'age' : round(time_diff.total_seconds(), 0)
    }
    tokensList.append(item)
  return JsonResponse({'tokens': tokensList[lower:upper], 'size': size})

# Create your views here.
