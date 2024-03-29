import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

from rango.models import Category, Page


def populate():
    python_pages = [
        {'title': 'Official tutorial',
         'url': 'http://docs.python.org/2/tutorial/'},
        {'title': 'HtTLaCS',
         'url': 'http://www.greenteapress.com/thinkpython/'},
        {'title': 'Learn Python on 10 minutes',
         'url': 'http://www.korokithakis.net/tutorials/python/'}
    ]

    django_pages = [
        {'title': 'Official Django Tutorial',
         'url': 'http://docs.djangoproject.com/en/1.9/intro/tutorial01/'},
        {'title': 'Django Rocks',
         'url': 'http://www.djangorocks.com/'},
        {'title': 'How to Tango with Django',
         'url': 'http://www.tangowithdjango.com/'}
    ]

    other_pages = [
        {'title': 'Bottle',
         'url': 'http://bottlepy.org/docs/dev/'},
        {'title': 'Flask',
         'url': 'http://flask.pocoo.org'}
    ]

    cats = {'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
            'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
            'Other': {'pages': other_pages, 'views': 32, 'likes': 16}}

    for cat, cat_data in cats.iteritems():
        c = add_cat(cat, cat_data['views'], cat_data['likes'])
        print c
        for p in cat_data['pages']:
            p = add_page(c, p['title'], p['url'])
            print '\t{}'.format(p)


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


if __name__ == '__main__':
    print "Start population"
    populate()




