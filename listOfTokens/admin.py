from django.contrib import admin
from .models import bscToken, network, user

class networkToken(admin.ModelAdmin):
  list_display = ('name', 'networkName')

class tokenCount(admin.ModelAdmin):
  list_display = ('networkName', 'display_tokenAmmount')

admin.site.register(bscToken, networkToken)
admin.site.register(network, tokenCount)
admin.site.register(user)

# Register your models here.
