from django.shortcuts import render
from Academica.models import Faculty , Department

# Create your views here.

def listadoFacultades(request):
    facultades = Faculty.objects.all() # Sekect * from Fcaulty
    return render(request, 'facultades/listado_facultades.html',
                 {'facultades':facultades})
                 

def listadoDepartamentos(request):
    departamentos = Department.objects.select_related('faculty')
    return render(request, 'departamentos/department_list.html',
                     {'departamentos': departamentos })
