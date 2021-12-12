from django import template

register = template.Library()


########################
# math methods
@register.simple_tag
def div(a, b, count_num=False):
    """
    :param count_num: int only
    :param a: int or float
    :param b: int or float
    :return: template内割り算
    """
    if count_num:
        b = b * 800
    try:
        get_num = a / b * 100
    except ZeroDivisionError:
        return 0
    return round(get_num, 1)

########################
