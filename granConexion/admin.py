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
        datos_finales = []
        
        for nominado in nominados:
            id_nominado = nominado.id
            nickname_nominado = nominado.player.nickname
            resultado_filter = resultados.filter(player__id=id_nominado)
            if resultado_filter.exists():
                votos = resultado_filter[0]['total_votos']
            else:
                votos = 0
            
            dato = {
                'nickname': nickname_nominado,
                'votos': votos
            }
            datos_finales.append(dato)
        
        #ordenamos segun cantidad de votos
        datos_finales.sort(key=lambda x: x['votos'], reverse=True)
        return_datos = ''
        
        for dato in datos_finales:
            return_datos += f'{dato["nickname"]}: {dato["votos"]} votos\n'    
        
        return datos_finales
            
        # resultados_html = '<h3>Resultados de la votación:</h3>'
        # for jugador, votos in resultados:
        #     resultados += f'<p>{jugador}: {votos} votos</p>'
        # return resultados

    ver_resultados.short_description = 'Resultados'

admin.site.register(Votacion, VotacionAdmin)
admin.site.register(VotoDelPublico)
