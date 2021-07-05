from .models import Libro, Categoria
from rest_framework import serializers

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    nombre_marca = serializers.CharField(read_only=True, source="nombre.marca")
    marca = MarcaSerializer(read_only=True)
    marca_id = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(), source="marca")
    nombre = serializers.CharField(required=True, min_length=3)

    def validate_nombre(self, value):
        existe = Libro.objects.filter(nombre__iexact=value).exists()

        if existe:
            raise serlializers.ValidationError("Ya existe") 

        return value
    class Meta:
        model = Libro
        fields = '__all__' 