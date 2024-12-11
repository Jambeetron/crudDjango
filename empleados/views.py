from django.shortcuts import render
from .models import Empleado
from django.db import IntegrityError
from decimal import Decimal

def calcular_salario(request):
    if request.method == 'POST':
        cedula = request.POST['cedula']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        telefono = request.POST['telefono']
        horas_trabajadas = int(request.POST['horas_trabajadas'])
        valor_hora = Decimal(request.POST['valor_hora'])  # Convertir a Decimal

        # Crear empleado temporal para calcular el salario
        empleado = Empleado(
            cedula=cedula,
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
            horas_trabajadas=horas_trabajadas,
            valor_hora=valor_hora
        )
        salario = empleado.calcular_salario()

        # Formatear el salario
        salario_formateado = f"${salario:,.2f}"

        return render(request, 'resultado.html', {
            'empleado': empleado,
            'salario_formateado': salario_formateado
        })
    return render(request, 'formulario.html')