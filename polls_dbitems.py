import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

django.setup()

from rango.models import Topic, Page


def populate():
    python_pages = [
        {'title': 'interesting',
         'url': 'http://docs.python.org/3/tutorial/',
         'views': 302, }, ]

    django_pages = [
        {'title': 'good luck',
         'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
         'views': 32, }, ]

    other_pages = [
        {'title': 'my point',
         'url': 'http://bottlepy.org/docs/dev/',
         'views': 302, }, ]

    cats = {'Apple vs Google?': {'pages': python_pages, 'views': 32, 'likes': 64},
            'CCCP vs US?': {'pages': django_pages, 'views': 25, 'likes': 32},
            'Glasgow vs Edingberg?': {'pages': other_pages, 'views': 200, 'likes': 16}}

    for cat, cat_data in cats.items():
        c = add_cat(cat, views=cat_data['views'], likes=cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], views=p['views'])

    for c in Topic.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name, views=0, likes=0):
    c = Topic.objects.get_or_create(title=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


# Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
