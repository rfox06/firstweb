from django.contrib import admin

# Register your models here.
# empleado es el nombre de la clase que esta en models
from .models import Empleado, Habilidades

admin.site.register(Habilidades)


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
        'id',
    )
    # full_name para que funcione

    def full_name(self, obj):
        print(obj.first_name)
        return obj.first_name + ' ' + obj.last_name

    # Personalizacion del Administrador
    search_fields = ('first_name',)
    list_filter = ('departamento', 'job', 'habilidades',)

    # para seleccionar habilidades
    filter_horizontal = ('habilidades',)


admin.site.register(Empleado, EmpleadoAdmin)
