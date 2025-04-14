from django import template
from decimal import Decimal, ROUND_HALF_UP

register = template.Library()

@register.filter
def multiply(value, arg):
    try:
        result = Decimal(str(value)) * Decimal(str(arg))
        return result.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    except (ValueError, TypeError):
        return ''
