from django.contrib import admin
from .models import  VotoDelPublico, Votacion

# Register your models here.
class VotoDelPublicoInline(admin.TabularInline):
    model = VotoDelPublico
    extra = 0

class VotacionAdmin(admin.ModelAdmin):
    inlines = [VotoDelPublicoInline]
    readonly_fields = ['ver_resultados']

    def ver_resultados(self, obj):
        resultados = obj.obtener_resultados()
        # resultados_html = '<h3>Resultados de la votación:</h3>'
        # for jugador, votos in resultados:
        #     resultados += f'<p>{jugador}: {votos} votos</p>'
        return resultados

    ver_resultados.short_description = 'Resultados'

admin.site.register(Votacion, VotacionAdmin)
admin.site.register(VotoDelPublico)
