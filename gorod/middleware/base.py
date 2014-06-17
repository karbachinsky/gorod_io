from gorod.models import City

class UserCityMiddleware(object):
    """ 
        Set user city if he is authorized 
        ans city is not set yet
    """
    def __init__(self):
        pass

    def process_view(self, request, view_func, view_args, view_kwargs):
        if not request.user.is_authenticated() or request.user.city:
            return None

        city = None
        current_url_params = request.resolver_match.kwargs

        if current_url_params.get('city_name'):
            city = City.objects.get(name=current_url_params.get('city_name'));

        if not city:
            return None

        try:
            request.user.city = city
            request.user.save()
        # FIXME
        except Exception as e:
            raise e

        return None

