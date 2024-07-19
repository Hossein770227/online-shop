from django import template

register = template.Library()

@register.filter
def translate(value):
    value = str(value)
    english_persian_to=value.maketrans('0123456789','۰١٢٣٤٥٦٧٨٩')
    return value.translate(english_persian_to)