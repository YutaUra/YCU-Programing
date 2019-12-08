from markdownx.admin import MarkdownxModelAdmin
from django_press.models import PageContent, PageText
from polymorphic.admin import StackedPolymorphicInline, PolymorphicInlineSupportMixin


class PageContentInline(StackedPolymorphicInline):
    class PageTextInline(StackedPolymorphicInline.Child):
        model = PageText

    model = PageContent
    child_inlines = (
        PageTextInline,
    )


class PageAdmin(PolymorphicInlineSupportMixin, MarkdownxModelAdmin):
    inlines = [PageContentInline, ]
    pass
