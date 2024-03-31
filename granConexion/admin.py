from django.contrib import admin
from .models import Nominacion, GalaDeNominacion, votoDelPublico, GalaEliminacion

# Register your models here.
admin.site.register(Nominacion)
admin.site.register(GalaDeNominacion)
admin.site.register(votoDelPublico)
admin.site.register(GalaEliminacion)
