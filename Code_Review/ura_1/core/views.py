from django.views.generic import TemplateView, FormView


class BaseView(TemplateView):
    template_name = 'core/base.html'


class SettingChangeView(FormView):
    template_name = 'core/change_setting.html'
