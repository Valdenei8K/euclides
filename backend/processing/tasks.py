from celery import shared_task

import time


@shared_task
def process_numbers_data(process_id):
    time.sleep(2) #Simular demora fila
    from processing.models import Processamento, StatusProcessamento
    from processing.services.calculator_service import CalculatorService
    print('Entrou no celery')
    process = Processamento.objects.filter(id=process_id).first()

    if not process:
        return f"Processamento {process_id} não encontrado"

    if not process.numeros or len(process.numeros) < 1:
        return f"Números ausentes para processamento #{process_id}"

    average = CalculatorService.calculate_average(process.numeros)
    median = CalculatorService.calculate_median(process.numeros)
    process.media = average
    process.mediana = median
    process.status = StatusProcessamento.CONCLUIDO
    process.save()

