"""
    Script allows to recount number of comments for articles.
    Script is executed by crontab.
"""

from django.core.management.base import BaseCommand, CommandError

from gorod.utils.exceptions import DONCError
from gorod.utils.donc import ArticleCommentsCounter

from optparse import make_option


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--article-id',
            default=None,
            help='Article id'),
    )

    def handle(self, *args, **options):
        """
            Command execution
        """
        article_id = options.get('article_id', None)

        try:
            donc = ArticleCommentsCounter()
            donc.recount(article_id)
        except DONCError as e:
            raise CommandError(e)
