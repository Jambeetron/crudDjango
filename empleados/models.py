from django.db import models
from decimal import Decimal
from django.utils.timezone import now

class Empleado(models.Model):
    cedula = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    horas_trabajadas = models.PositiveIntegerField()
    valor_hora = models.DecimalField(max_digits=10, decimal_places=2)

    def calcular_salario(self):
        if self.horas_trabajadas <= 40:
            return self.horas_trabajadas * self.valor_hora
        elif self.horas_trabajadas <= 48:
            extras_simples = self.horas_trabajadas - 40
            return (40 * self.valor_hora) + (extras_simples * self.valor_hora * Decimal('1.2'))
        else:
            extras_simples = 8
            extras_dobles = self.horas_trabajadas - 48
            return (40 * self.valor_hora) + (extras_simples * self.valor_hora * Decimal('1.2')) + (extras_dobles * self.valor_hora * Decimal('1.4'))
        
    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.cedula}'

class HistorialSalarios(models.Model):
    empleado = models.CharField(max_length=255)
    cedula = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    horas_trabajadas = models.IntegerField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_calculo = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.empleado} - {self.salario} ({self.fecha_calculo})"