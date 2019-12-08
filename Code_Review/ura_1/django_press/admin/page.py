from markdownx.admin import MarkdownxModelAdmin
from django_press.models import PageContent, PageText, ImageSlider, Service
from polymorphic.admin import StackedPolymorphicInline, PolymorphicInlineSupportMixin


class PageContentInline(StackedPolymorphicInline):
    class PageTextInline(StackedPolymorphicInline.Child):
        model = PageText

    class ImageSliderInline(StackedPolymorphicInline.Child):
        model = ImageSlider

    class ServiceInline(StackedPolymorphicInline.Child):
        model = Service

    model = PageContent
    child_inlines = (
        PageTextInline,
        ImageSliderInline,
        ServiceInline,
    )


class PageAdmin(PolymorphicInlineSupportMixin, MarkdownxModelAdmin):
    inlines = [PageContentInline, ]
    pass
