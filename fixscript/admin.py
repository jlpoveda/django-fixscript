from django.contrib import admin

from fixscript.models import Fixscript


class FixscriptAdmin(admin.ModelAdmin):
    pass


admin.register(Fixscript, FixscriptAdmin)
