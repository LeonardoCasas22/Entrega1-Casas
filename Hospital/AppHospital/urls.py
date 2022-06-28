from unicodedata import name
from django.urls import path
from AppHospital import views

urlpatterns = [
    
    path('', views.inicio, name = 'inicio'),
    path('medicos/' , views.medicos, name = 'medicos'),
    path('pacientes/' , views.pacientes, name = 'pacientes'),
    path('enfermeros/' , views.enfermeros, name = 'enfermeros'),
    path('resultados/', views.resultados, name = 'resultados')
]














