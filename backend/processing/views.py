from statistics import median

from celery import shared_task
from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Processamento
from .serializers import ProcessamentoSerializer
from processing.tasks import process_numbers_data



class CriarProcessamentoView(generics.CreateAPIView):
    queryset = Processamento.objects.all()
    serializer_class = ProcessamentoSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        instance = serializer.save()
        process_numbers_data.delay(instance.id)


class ListaProcessamentosView(generics.ListAPIView):
    serializer_class = ProcessamentoSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        limit = self.request.query_params.get('limit', 10)
        queryset = Processamento.objects.all().order_by('-criado_em')
        if limit and limit.isdigit():
            return queryset[:int(limit)]
        return queryset


class StatusProcessamentoView(APIView):
    def get(self, request, pk):
        try:
            processamento = Processamento.objects.get(pk=pk)
        except Processamento.DoesNotExist:
            return Response({'erro': 'Processamento não encontrado'}, status=404)

        serializer = ProcessamentoSerializer(processamento)
        return Response(serializer.data)

