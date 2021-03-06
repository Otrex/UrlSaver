from django import template
register = template.Library()

cnt = [0]
@register.filter
def counter(v ):
    v["i"] = 1
    # cnt = v
    # cnt += 1
    return cnt

@register.filter
def segment(v, c):
    if c == 0:
        return
    if c % 4 == 0:
        c = True
        return c
    return False