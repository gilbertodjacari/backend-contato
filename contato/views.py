from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Contato
from .serializers import ContatoSerializer

class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all().order_by('-criado_em')
    serializer_class = ContatoSerializer

    def create(self, request, *args, **kwargs):
        """Cria contato com resposta customizada"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"message": "Contato enviado com sucesso!", "data": serializer.data},
            status=status.HTTP_201_CREATED,
            headers=headers
        )
