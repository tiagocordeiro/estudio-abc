from django.contrib import admin
from .models import Fotolito


class FotolitoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'added_by', 'finalidade',
                    'camada', 'lineatura', 'created_date',)

    def get_list_filter(self, request):
        return ('added_by', 'created_date',)


admin.site.register(Fotolito, FotolitoAdmin)
