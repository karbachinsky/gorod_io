from gorod.models import City

def save_avatar(strategy, user, response, details, is_new=False, *args, **kwargs):
    """
        Save user avatars pipeline after authorization
    """
    #if is_new:
    #    return
    image_url = None

    # VK
    if strategy.backend.name == 'vk-oauth2':
        image_url = response.get('photo')
    # Add your backend here
    else:
        return

    if not image_url:
        return

    try:
        user.avatar = image_url
        user.save()
    # FIXME
    except Exception as e:
        raise e


def set_city(strategy, user, response, details, is_new=False, *args, **kwargs):
    """
        Set city to user if city isn't set
    """
    if user.city:
        return

    try:
        city = City.objects.get(id=1); 
        user.city = city
        user.save()
    # FIXME
    except Exception as e:
        raise e

