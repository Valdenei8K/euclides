from rest_framework import serializers
from .models import Processamento

class ProcessamentoSerializer(serializers.ModelSerializer):
    numeros = serializers.ListField(
        child=serializers.FloatField(),
        write_only=False,
        min_length=3,
        max_length=100
    )

    class Meta:
        model = Processamento
        fields = ['id', 'numeros', 'media', 'mediana', 'status', 'criado_em']
        read_only_fields = ['id', 'media', 'mediana', 'status', 'criado_em']

    def create(self, validated_data):
        numeros = validated_data.pop('numeros')
        instance = Processamento()
        instance.numeros = numeros
        instance.save()

        return instance
