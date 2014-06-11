def save_avatar(strategy, user, response, details,
                is_new=False, *args, **kwargs):
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

    if image_url:
        try:
            user.avatar = image_url
            user.save()
        # FIXME
        except Exception as e:
            raise e