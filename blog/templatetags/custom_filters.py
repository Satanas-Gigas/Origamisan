from django import template
import random

register = template.Library()

@register.filter(name='add_class')
def add_class(value, class_name):
    return value.as_widget(attrs={'class': class_name})

@register.filter
def shuffle(value):
    """Перемешивает список."""
    if isinstance(value, list):
        random.shuffle(value)
        return value
    return value