from rest_framework import serializers
from guias.models import Registro

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = '__all__'
