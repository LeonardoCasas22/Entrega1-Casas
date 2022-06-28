from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppHospital.models import Medicos, Enfermeros, Pacientes
from AppHospital.forms import enfermerosFormulario, medicosFormulario, pacientesFormulario

  
def inicio(request):
    return render(request, 'AppHospital/inicio.html')

def medicos(request):
    
    if request.method == "POST": 

        elformulario = medicosFormulario(request.POST)

        if elformulario.is_valid(): 
        
            informacion = elformulario.cleaned_data

            medicos = Medicos (nombre = informacion['nombre'], apellido = informacion['apellido'], especialidad = informacion['especialidad'], matricula = informacion['matricula']) 

            medicos.save()
    
            return render(request, 'AppHospital/inicio.html')  
    
    else:
         elformulario = medicosFormulario() 
    
    return render(request, 'AppHospital/medicos.html', {'form': elformulario})
    

def enfermeros(request):
    if request.method == "POST": 

        elformulario = enfermerosFormulario(request.POST)

        if elformulario.is_valid(): 
        
            informacion = elformulario.cleaned_data

            enfermeros = Enfermeros (nombre = informacion['nombre'], 
                apellido = informacion['apellido'], 
                turno = informacion['turno'], 
                n_empleado = informacion['n_empleado'])
                

            enfermeros.save()
    
            return render(request, 'AppHospital/inicio.html')  
    
    else:
         elformulario = enfermerosFormulario() 
    
    return render(request, 'AppHospital/enfermeros.html', {'form': elformulario})

def pacientes(request):
    
    if request.method == "POST": 

        elformulario = pacientesFormulario(request.POST)

        if elformulario.is_valid(): 
        
            informacion = elformulario.cleaned_data

            pacientes = Pacientes (nombre = informacion['nombre'], 
                apellido = informacion['apellido'], 
                dni = informacion['dni'], 
                fecha_ingreso = informacion['fecha_ingreso'], 
                mail = informacion['mail']) 

            pacientes.save() 
    
            return render(request, 'AppHospital/inicio.html')   
    
    else:
         elformulario = pacientesFormulario() 
    
    return render(request, 'AppHospital/pacientes.html', {'form': elformulario})     



def resultados(request):

    if request.GET['especialidad']:

        especialidad = request.GET['especialidad']

        medicos = Medicos.objects.filter(especialidad=especialidad) 

        return render(request, 'AppHospital/resultados.html', {'medicos': medicos, 'especialidad':especialidad, }) 
    

    else: 

        respuesta = 'No enviste datos'


    return render(request, 'AppHospital/inicio.html', {'respuesta': respuesta})



 

