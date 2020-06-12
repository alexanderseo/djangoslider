from django.contrib import admin
from main.models import Slider

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.site_title = 'Личный кабинет сайта'
admin.site.site_header = 'Личный кабинет'
