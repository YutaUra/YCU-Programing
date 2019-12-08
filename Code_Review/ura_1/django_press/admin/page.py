from markdownx.admin import MarkdownxModelAdmin
from django_press.models import PageContent, PageText, ImageSlider
from polymorphic.admin import StackedPolymorphicInline, PolymorphicInlineSupportMixin


class PageContentInline(StackedPolymorphicInline):
    class PageTextInline(StackedPolymorphicInline.Child):
        model = PageText

    class ImageSliderInline(StackedPolymorphicInline.Child):
        model = ImageSlider

    model = PageContent
    child_inlines = (
        PageTextInline,
        ImageSliderInline,
    )


class PageAdmin(PolymorphicInlineSupportMixin, MarkdownxModelAdmin):
    inlines = [PageContentInline, ]
    pass
