from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado, HistorialSalarios
from decimal import Decimal
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt

# Vista para mostrar el formulario
def mostrar_formulario(request):
    return render(request, 'formulario.html')

# Vista para calcular el salario y mostrar el resultado
def calcular_salario(request):
    if request.method == 'POST':
        cedula = request.POST['cedula']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        telefono = request.POST['telefono']
        horas_trabajadas = int(request.POST['horas_trabajadas'])
        valor_hora = Decimal(request.POST['valor_hora'])

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

        # Guardar en el historial
        HistorialSalarios.objects.create(
            empleado=f"{nombre} {apellido}",
            cedula=cedula,
            telefono=telefono,
            horas_trabajadas=horas_trabajadas,
            salario=salario,
            fecha_calculo=now()
        )

        return render(request, 'resultado.html', {
            'empleado': empleado,
            'salario_formateado': salario_formateado
        })

    return render(request, 'formulario.html')

def ver_historial(request):
    historial = HistorialSalarios.objects.all().order_by('-fecha_calculo')  # Ordenar por fecha descendente
    return render(request, 'historial.html', {'historial': historial})

# Vista para borrar un registro específico
@csrf_exempt
def borrar_dato(request, registro_id):
    if request.method == 'POST':
        registro = get_object_or_404(HistorialSalarios, id=registro_id)
        registro.delete()
    return redirect('ver_historial')

# Vista para borrar todo el historial
@csrf_exempt
def borrar_todo(request):
    if request.method == 'POST':
        HistorialSalarios.objects.all().delete()
    return redirect('ver_historial')