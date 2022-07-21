from django.contrib import admin
from .models import bscToken, network, user

admin.site.register(bscToken)
admin.site.register(network)
admin.site.register(user)

# Register your models here.
