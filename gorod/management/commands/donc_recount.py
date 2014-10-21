"""
    Script allows to recount number of comments for articles.
    Script is executed by crontab.
"""

from django.core.management.base import BaseCommand, CommandError

from gorod.utils.exceptions import DONCError
from gorod.utils.donc import *

from optparse import make_option


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--type',
            help='articles, questions'
        ),
        make_option('--object-id',
            default=None,
            help='certain object id'
        )
    )

    def handle(self, *args, **options):
        """
            Command execution
        """
        type = options.get('type')
        object_id = options.get('object_id', None)

        if not type:
            raise CommandError("Specify type!")

        if 'articles' == type:
            donc = ArticleCommentsCounter()
        elif 'questions' == type:
            donc = HubQuestionAnswersCounter()

        try:
            donc.recount(object_id)
        except DONCError as e:
            raise CommandError(e)
