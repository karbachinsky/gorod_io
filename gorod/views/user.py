from django.shortcuts import render,  get_object_or_404
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model

from gorod.models import Article

USER_LAST_FEEDS_CNT = 10

# User profile page
def profile(request, city_name, user_id):
    user = get_object_or_404(get_user_model(), id=user_id, city__name=city_name)

    user_last_feeds = Article.objects.filter(user__id=user_id).order_by('-add_date').select_related().all()[:USER_LAST_FEEDS_CNT]

    context = {
        'user_info': user,
        'user_last_feeds': user_last_feeds
    }

    return render(request, 'gorod/user/profile.html', context)


def logout_view(request):
    logout(request)
    # FIXME please
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
