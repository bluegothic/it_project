import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

django.setup()

from rango.models import Comment, Topic

# For an explanation of what is going on here, please refer to the TwD book.

def populate():

    commems = [
        {'context': 'comment something',
         'author_user_id': 1,
         'topic_id_id': 1
         }]

    cats = [
        {
            'authou_user_id': 1,
            'title': 'Which one is better?',
            'type': 'S',
            'option1': ' Coca-Cola',
            'option2': ' Pepsi-Cola', }]

    for cat in cats:
        add_cat(cat['authou_user_id'],cat['title'], cat['option1'], cat['option2'])
    for p in commems:
        add_com(p['context'], p['author_user_id'], p['topic_id_id'])


def add_com(context, author_user_id, topic_id_id):
    p = Comment.objects.get_or_create(author_user_id=author_user_id)[0]
    p.context = context
    p.topic_id_id = topic_id_id
    p.save()
    return p


def add_cat(authou_user_id, title, option1, option2):
    c = Topic.objects.get_or_create(title=title)[0]
    c.authou_user_id = authou_user_id
    c.option1 = option1
    c.option2 = option2
    c.save()
    return c


# Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
