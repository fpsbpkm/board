from django import template
register = template.Library()


@register.filter
def new_line(text):
    text = text.replace('\n', '<br/>')
    return text
