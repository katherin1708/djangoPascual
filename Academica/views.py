from django.shortcuts import render
from Academica.models import Faculty

# Create your views here.

def listadoFacultades(request):
    facultades = Faculty.objects.all() # Sekect * from Fcaulty
    return render(request, 'facultades/listado_facultades.html',
                 {'facultades':facultades})
                 

