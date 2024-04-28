from django.contrib import admin
from .models import Klub, ExtraInfo, Sezon, Zawodnik

admin.site.register(Zawodnik)

class ExtraInfoInline(admin.TabularInline):
    model = ExtraInfo

class SezonInline(admin.TabularInline):
    model = Sezon
    extra = 0

class ZawodnikInline(admin.TabularInline):
    model = Zawodnik.kluby.through
    extra = 0

@admin.register(Klub)
class KlubAdmin(admin.ModelAdmin):
    inlines = [ExtraInfoInline, SezonInline, ZawodnikInline]