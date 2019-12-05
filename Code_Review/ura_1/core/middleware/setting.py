from django.http import HttpRequest
from django.template.response import TemplateResponse
from core.models import Setting


class RenderingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        return response

    @staticmethod
    def process_template_response(request: HttpRequest, response: TemplateResponse):
        response.context_data.update(dict(core=dict(Setting.objects.values_list('key', 'value'))))
        return response
