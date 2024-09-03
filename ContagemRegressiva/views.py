from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.http import Http404, HttpResponse,JsonResponse
import datetime
import pytz

# Create your views here.
dataEncontro = datetime.date(2024, 11, 23)

def index(request):
	return render(request, "ContagemRegressiva/index.html",{
		"dataEncontro": dataEncontro
		})

@require_GET
def time(request):
	brazilTz = pytz.timezone("America/Belem")
	now = datetime.datetime.now(brazilTz)
	tempoFaltando = dataEncontro - datetime.date.today()
	dias = tempoFaltando.days
	horas = abs(19 - now.hour)
	minutos = 60 - now.minute
	segundos = 60 - now.second

	data = {
		'dias': dias,
		'horas': horas,
		'minutos': minutos,
		'segundos': segundos
	}
	return JsonResponse(data)