from rest_framework import serializers
from proyectos.models import Centros_de_formacion

class Centros_de_formacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Centros_de_formacion
        fields = ['id','nombre', 'regional']

