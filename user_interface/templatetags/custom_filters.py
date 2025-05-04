from django.template.library import Library

register = Library()


@register.filter
def is_iterable_not_string(value):
    return hasattr(value, "__iter__") and not isinstance(value, str)
