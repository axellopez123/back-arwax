from django.db import models
from django.core.validators import validate_ipv4_address, validate_ipv6_address

class Bot(models.Model):
    events = models.JSONField()
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    website = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    email = models.EmailField(blank=True, null=True)
    user_agent = models.CharField(max_length=255, blank=True, null=True, help_text="Información del navegador y dispositivo del usuario")
    referrer = models.URLField(blank=True, null=True, help_text="URL de referencia")
    ip_address = models.GenericIPAddressField(blank=True, null=True, help_text="Dirección IP del usuario")
    session_duration = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True, help_text="Duración de la sesión en segundos con decimales")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora de creación")
    updated_at = models.DateTimeField(auto_now=True, help_text="Fecha y hora de última actualización")
    
    def __str__(self):
        return self.name  # Mostrar el nombre del bot en el admin