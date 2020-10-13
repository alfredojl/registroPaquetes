from django.contrib import admin

# Register your models here.

from .models import *

class ArticleAdmin(admin.ModelAdmin):
    raw_id_fields = ("newspaper",)


admin.site.register(Verificador)
admin.site.register(Preparador)
admin.site.register(Estado)
admin.site.register(Folio)
admin.site.register(Digitalizador)
admin.site.register(Paquete)
admin.site.register(Usuario)

