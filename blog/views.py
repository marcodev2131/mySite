from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render

def show_datetime(request):
    now = timezone.localtime()
    html = f"<h1>Data e Hora Atual</h1><p>{now.strftime('%d/%m/%Y %H:%M:%S')}</p>"
    return HttpResponse(html)

# Create your views here.
