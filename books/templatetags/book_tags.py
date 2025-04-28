from django import template
register = template.Library()

@register.filter

def two_lower(value, arg):
    return f'{arg}: {value.lower()}'
