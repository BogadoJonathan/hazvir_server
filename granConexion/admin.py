from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import  VotoDelPublico, Votacion

# Register your models here.
class VotoDelPublicoInline(admin.TabularInline):
    model = VotoDelPublico
    extra = 0

class VotacionAdmin(admin.ModelAdmin):
    inlines = [VotoDelPublicoInline]
    readonly_fields = ['ver_resultados']

    def ver_resultados(self, obj):
        nominados = obj.nominados.all()
        resultados = obj.obtener_resultados()
        
        for nominado in nominados:
            id_nominado = nominado.id
            nickname_nominado = nominado.player.nickname
            resultado_filter = resultados.filter(player__id=id_nominado)
            if resultado_filter.exists():
                votos = resultado_filter[0]['total_votos']
            else:
                votos = 0
            resultados_html += f'<p>{nickname_nominado}: {votos} votos</p>'
        return mark_safe(resultados_html)
            
        # resultados_html = '<h3>Resultados de la votación:</h3>'
        # for jugador, votos in resultados:
        #     resultados += f'<p>{jugador}: {votos} votos</p>'
        # return resultados

    ver_resultados.short_description = 'Resultados'

admin.site.register(Votacion, VotacionAdmin)
admin.site.register(VotoDelPublico)
