"""
    Script allows to recount number of comments for articles.
    Script is executed by crontab.
"""

from django.core.management.base import BaseCommand, CommandError

from gorod.utils.exceptions import DONCError
from gorod.utils.donc import ArticleCommentsCounter


class Command(BaseCommand):

    def handle(self, *args, **options):
        """
            Command execution
        """
        try:
            donc = ArticleCommentsCounter()
            donc.recount()
        except DONCError as e:
            raise CommandError(e)
