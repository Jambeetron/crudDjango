from django.contrib import admin
from django.urls import path
from empleados import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.calcular_salario, name='home'),  # Redirige "/" al formulario
    path('calcular/', views.calcular_salario, name='calcular_salario'),
]