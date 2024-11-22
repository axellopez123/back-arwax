from rest_framework import serializers
from .models import Bots

class BotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bots
        fields = '__all__'

    def validate_ip_address(self, value):
        from django.core.exceptions import ValidationError
        from django.core.validators import validate_ipv4_address, validate_ipv6_address
        
        try:
            validate_ipv4_address(value)
        except ValidationError:
            try:
                validate_ipv6_address(value)
            except ValidationError:
                raise serializers.ValidationError("La dirección IP no es válida.")
        return value
