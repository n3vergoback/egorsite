from django import template

from shop.models import WatchesMechanism, WatchesCompany

register = template.Library()


@register.simple_tag()
def get_watches_mechanism():
    return WatchesMechanism.objects.all()


@register.inclusion_tag('shop/list_watches_filters.html')
def show_watches_filters():
    mechanisms = WatchesMechanism.objects.all()
    companies = WatchesCompany.objects.all()
    return {'mechanisms': mechanisms, 'companies': companies}