
from django.core.management.base import BaseCommand, CommandError
from gorod.models import OrganizationCategory

import yaml, os.path
from optparse import make_option

from gorod.models import User, Article, City

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--yaml-file',
            default=False,
            help='Yaml file with organization categories'),
    )

    def handle(self, *args, **options):
        """ Command execution """ 
        articles = Article.objects.all()
        for article in articles:
            r_user = User.objects.filter(city=article.city, username__contains='user').order_by('?')[0]
            article.user = r_user
            article.save()

        return None

