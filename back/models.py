from django.db import models
from django.core.validators import validate_ipv4_address, validate_ipv6_address

class Bots(models.Model):
    events = models.JSONField()
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    website = models.URLField(blank=True, null=True)
    message = models.TextField()
    email = models.EmailField(blank=True, null=True)
    user_agent = models.CharField(max_length=255, blank=True, null=True, help_text="Información del navegador y dispositivo del usuario")
    referrer = models.URLField(blank=True, null=True, help_text="URL de referencia")
    ip_address = models.GenericIPAddressField(blank=True, null=True, help_text="Dirección IP del usuario")
    session_duration = models.PositiveIntegerField(blank=True, null=True, help_text="Duración de la sesión en segundos")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora de creación")
    updated_at = models.DateTimeField(auto_now=True, help_text="Fecha y hora de última actualización")
