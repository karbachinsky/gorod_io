from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader


from gorod.models import City, Article, Organization


# Main page
def index(request):
    cities = City.objects.all

    context = {
        'cities': cities
    }

    return render(request, 'gorod/index.html', context)


# One city main page (feed)
def feed(request, city):
    city = get_object_or_404(City, name=city)
   
    articles = Article.objects.filter(city=city.id).order_by('-add_date').all 

    context = {
        'articles': articles,
        'city': city 
    }

    return render(request, 'gorod/feed.html', context)




# One city organizations 
def organizations(request, city):
    city = get_object_or_404(City, name=city)
   
    organizations = Organization.objects.filter(city=city.id).order_by('name').all 

    context = {
        'organizations': organizations,
        'city': city 
    }

    return render(request, 'gorod/organizations.html', context)




def article(request, article_id): 
    article = get_object_or_404(Article, pk=article_id)

    city = get_object_or_404(City, id=article.city.id)

    context = {
        'article': article,
        'city': city
    }

    return render(request, 'gorod/article.html', context)


def organization(request, organization_id): 
    organization = get_object_or_404(Organization, pk=organization_id)

    city = get_object_or_404(City, id=organization.city.id)

    context = {
        'organization': organization,
        'city': city
    }

    return render(request, 'gorod/organization.html', context)



