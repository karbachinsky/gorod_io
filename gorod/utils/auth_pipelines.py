from django.db import IntegrityError
from gorod.models import City


def save_avatar(strategy, user, response, details, is_new=False, *args, **kwargs):
    """
        Save user avatars pipeline after authorization
    """
    image_url = None

    # VK
    if strategy.backend.name == 'vk-oauth2':
        image_url = response.get('photo')
    if strategy.backend.name == 'facebook':
        #assert False, response
        image_url = 'http://graph.facebook.com/%d/picture' % int(response.get(u'id'))
    # Add your backend here

    if not image_url:
        return

    try:
        user.avatar = image_url
        user.save()
    except IntegrityError as e:
        raise RuntimeError(e)


def set_city(strategy, user, response, details, is_new=False, *args, **kwargs):
    """
        Set city to user if city isn't set
    """
    if user.city:
        return

    try:
        city = City.objects.get(id=1)
        user.city = city
        user.save()
    # FIXME
    except IntegrityError as e:
        raise RuntimeError(e)

