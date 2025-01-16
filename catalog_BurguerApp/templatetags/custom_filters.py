from django import template
from django.utils.html import format_html

register = template.Library()

@register.filter
def add_class(field, css_class):
    """
    Adiciona uma classe CSS ao campo de formulário.
    """
    return field.as_widget(attrs={"class": css_class})
