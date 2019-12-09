from django.shortcuts import get_object_or_404
from django.views import generic
from django_press.models import Page


class TestView(generic.TemplateView):
    template_name = 'django_press/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        path = kwargs.get('path', '')
        page = get_object_or_404(Page, path=path)
        context.update(title=page.title)
        context.update(page=page)
        context.update(contents=page.contents.all())
        return context
