from django.contrib import admin
from .models import Bot

class BotAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'ip_address', 'created_at', 'updated_at')

admin.site.register(Bot, BotAdmin)
