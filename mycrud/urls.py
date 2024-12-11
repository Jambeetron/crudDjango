from django.contrib import admin
from django.urls import path
from empleados import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.calcular_salario, name='formulario'),  # Redirige "/" al formulario
    path('calcular/', views.calcular_salario, name='calcular_salario'),
    path('resultado/', views.calcular_salario, name='resultado'),
    path('historial/', views.ver_historial, name='ver_historial'),
    path('borrar/<int:registro_id>/', views.borrar_dato, name='borrar_dato'),
    path('borrar-todo/', views.borrar_todo, name='borrar_todo'),
]