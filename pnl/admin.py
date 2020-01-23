from django.contrib import admin
from .models import Tecnologico, Usuario, Aprendizaje, Temas, SubTemas, Ejercicio, TemaUsuario, EjercicioR

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("NombreUsuario", "Nombre", "ApellidoPaterno", "ApellidoMaterno","Password","Email","FechaNacimiento","Nivel","Progreso","IdTecnologico","Foto")
    save_on_top = True

admin.site.register(Usuario, UsuarioAdmin)

class TecnologicoAdmin(admin.ModelAdmin):
	list_display= ("Nombre", "ClavePlantel")
	save_on_top=True
admin.site.register(Tecnologico, TecnologicoAdmin)

class AprendizajeAdmin(admin.ModelAdmin):
	list_display = ("Visual", "Auditivo", "Kinestesico", "CantidadVisuales","CantidadAuditivos","CantidadKinestesicos","IdUsuario")
	save_on_top = True
admin.site.register(Aprendizaje, AprendizajeAdmin)

class TemasAdmin(admin.ModelAdmin):
	list_display=("Nombre","NSubtemas","Numero")
	save_on_top=True
admin.site.register(Temas,TemasAdmin)

class TemaUsuarioAdmin(admin.ModelAdmin):
   list_display=("IdUsuario","IdTema","Evaluacion")
   save_on_top=True
admin.site.register(TemaUsuario,TemaUsuarioAdmin)

class SubTemasAdmin(admin.ModelAdmin):
	list_display=("Nombre","IdTemas","Numero", "NEjercicios")
	save_on_top=True
admin.site.register(SubTemas,SubTemasAdmin)

class EjercicioAdmin(admin.ModelAdmin):
   list_display=("IdUsuario", "IdSubtema","Nombre","Tipo","Evaluacion","Fecha","R1","R2","R3","R4","R5","R6")
   save_on_top=True
admin.site.register(Ejercicio,EjercicioAdmin)

class EjercicioRAdmin(admin.ModelAdmin):
	list_display=("IdTem", "Descripcion", "NEjer", "Tipo", "RP1", "RP2", "RP3", "RP4", "RP5", "RP6", "RP7", "RP8", "RP9", "RP10")
	save_on_top=True
admin.site.register(EjercicioR, EjercicioRAdmin)
# Register your models here.
