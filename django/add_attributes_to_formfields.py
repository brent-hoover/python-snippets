from django import template

register = template.Library()

@register.simple_tag
def formfield(field,**kwargs):
    field.field.widget.attrs.update(kwargs)
    return field
