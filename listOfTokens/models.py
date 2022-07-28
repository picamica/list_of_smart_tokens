from django.db import models
from django.urls import reverse


class general(models.Model):
  created_on = models.DateTimeField(auto_now_add=True)
  scannerLink = models.URLField('name', max_length=128)
  exchangerLink = models.URLField('exchanger', max_length=128)

  class Meta:
    abstract = True
    ordering = ['scannerLink', 'exchangerLink', 'created_on']

  def __str__(self):
    return f'{self.scannerLink} | {self.exchangerLink} | {self.created_on}'

class network(models.Model):
  networkName = models.CharField(max_length=15)

  def display_tokenAmmount(self):
    return self.tokens.count()

  def __str__(self):
    return self.networkName

class bscToken(general):
  name = models.CharField('Token name', max_length=50)
  symbol = models.CharField('Token symbol', max_length=20)
  address = models.CharField('Token address', max_length=45)
  networkName = models.ForeignKey('network', on_delete=models.SET_NULL, null=True, related_name='tokens')

  def __str__(self):
    return f'{self.name} | {bscToken.created_on}'

class user(models.Model):
  userName = models.CharField(max_length=20)
  password = models.CharField(max_length=30)
  email = models.EmailField(max_length=120)

# Create your models here.
