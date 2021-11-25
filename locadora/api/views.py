from rest_framework import viewsets

from .serializers import EnderecoSerializer
from .models import Endereco


class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all().order_by('bairro_id')
    serializer_class = EnderecoSerializer
