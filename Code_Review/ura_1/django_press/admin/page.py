from markdownx.admin import MarkdownxModelAdmin
from django_press.models import PageContent, PageText, ImageSlider, Service, Tab
from polymorphic.admin import StackedPolymorphicInline, PolymorphicInlineSupportMixin


class PageContentInline(StackedPolymorphicInline):
    class PageTextInline(StackedPolymorphicInline.Child):
        model = PageText

    class ImageSliderInline(StackedPolymorphicInline.Child):
        model = ImageSlider

    class ServiceInline(StackedPolymorphicInline.Child):
        model = Service

    class TabInline(StackedPolymorphicInline.Child):
        model = Tab

    model = PageContent
    child_inlines = (
        PageTextInline,
        ImageSliderInline,
        ServiceInline,
        TabInline,
    )


class PageAdmin(PolymorphicInlineSupportMixin, MarkdownxModelAdmin):
    inlines = [PageContentInline, ]
    pass
