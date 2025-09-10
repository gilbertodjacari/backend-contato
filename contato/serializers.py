from rest_framework import serializers
from .models import Contato

class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = '__all__'
        read_only_fields = ['criado_em', 'atualizado_em', 'lido']

    def validate_mensagem(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("A mensagem deve ter pelo menos 10 caracteres.")
        return value
