from django.shortcuts import get_object_or_404
from django.views import generic
from django_press.models import Page


class BaseView(generic.TemplateView):
    template_name = 'django_press/base.html'


class TestView(generic.TemplateView):
    template_name = 'django_press/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        path = kwargs.get('path', '')
        # page_content = get_object_or_404(PageContent, page__path=path)
        # context.update(title=page_content.page.title)
        # context.update(content=page_content.text)
        return context
