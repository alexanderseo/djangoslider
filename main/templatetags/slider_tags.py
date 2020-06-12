from django import template
from main.models import Slider

register = template.Library()

@register.inclusion_tag('layouts/widget_slider.html')
def block_slider():
    slider_block = Slider.objects.all()
    return {'slider_block': slider_block,}