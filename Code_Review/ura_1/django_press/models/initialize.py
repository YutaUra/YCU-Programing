from django_press.models import Context, Page, PageText


def create_initial_pages(sender, **kwargs):
    top = Page.objects.get_or_create(title='top', path='')
    top_content = PageText.objects.get_or_create(page=top[0])
    about = Page.objects.get_or_create(title='about', path='about')
    about_content = PageText.objects.get_or_create(page=about[0])

