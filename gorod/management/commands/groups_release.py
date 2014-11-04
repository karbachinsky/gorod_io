# -*- coding: utf-8 -*-

"""
    Groups release
"""

from django.core.management.base import BaseCommand, CommandError
from gorod.models import *
from django.utils.decorators import method_decorator

from django.db import transaction


class Command(BaseCommand):
    @method_decorator(transaction.atomic)
    def handle(self, *args, **options):
        """
            Command execution
        """
        for city in City.objects.all():
            event_rubric, is_created = ArticleRubric.objects.get_or_create(
                city=city,
                name='event',
                title='Событие',
                title_plural='События'
            )

            event_rubric.save()

            message_rubric, is_created = ArticleRubric.objects.get_or_create(
                city=city,
                name='message',
                title='Новость',
                title_plural='Новости'
            )

            message_rubric.save()

            for article in Article.objects.filter(rubric__name='event', city=city):
                article.rubric = event_rubric
                article.save()

            for article in Article.objects.filter(rubric__name='message', city=city):
                article.rubric = message_rubric
                article.save()

            # Remove rubrics wo city
            ArticleRubric.objects.filter(city__isnull=True, name__in=['event', 'message']).delete()

