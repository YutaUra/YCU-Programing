from django import template
from site_page.models import Page

register = template.Library()


@register.inclusion_tag('site_page/nav/main.html', takes_context=True)
def nav(context, core):
    nav_pages = Page.objects.filter(in_nav=True).all()
    return {
        'nav_pages': nav_pages,
        'core': core,
    }
