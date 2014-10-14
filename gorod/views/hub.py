# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View, TemplateView
from django.utils.translation import ugettext as _
from django.db import IntegrityError, DatabaseError

from gorod.models import HubQuestion, HubAnswer, City, HubQuestionCategory
from gorod.utils.forms.hub import HubAnswerAddForm, HubQuestionAddForm
from gorod.utils.views.mixins import JSONResponseMixin


class HubView(View):
    """
        City list of hub questions
    """
    def dispatch(self, request, city_name):
        questions = HubQuestion.objects.get_questions_by_city_name(city_name)

        context = {
            'questions': questions,
            'question_form': HubQuestionAddForm(),
            # FIXME: Remove it if categories are redundant on frontend
            'categories': HubQuestionCategory.objects.all()
        }

        return render(request, 'gorod/hub.html', context)


class HubQuestionView(View):
    """
        One hub question view
    """
    def dispatch(self, request, city_name, question_id):
        question = get_object_or_404(HubQuestion, city__name=city_name, is_published=True, id=question_id)

        answers = HubQuestion.objects.get_question_answers(question.id)

        # Other questions
        questions = HubQuestion.objects.get_questions_by_city_name(city_name).exclude(id=question.id)

        context = {
            'question': question,
            'answers': answers,
            'other_questions': questions,
            'answer_form': HubAnswerAddForm(instance=HubAnswer(question=question))
        }

        return render(request, 'gorod/hub_question.html', context)


class HubAnswerAddView(JSONResponseMixin, TemplateView):
    """
        Post answer
    """
    def _get(self, *args, **kwargs):
        return self.json_forbidden_context(_(u'Ошибка!'))

    @method_decorator(login_required)
    def _post(self, request, city_name, question_id):
        city = get_object_or_404(City, name=city_name)
        data = request.POST.copy()

        if not 'question' in data or not question_id or question_id != data['question']:
            return self.json_form_error_context(
                _(u'Hacker?')
            )

        if request.user.can_action('add-hubanswer'):
            form = HubAnswerAddForm(request.POST, instance=HubAnswer())
            user = self.request.user
            if form.is_valid():
                answer = form.save(commit=False)
                answer.city = city
                answer.user = user
                try:
                    answer.save()
                except (DatabaseError, IntegrityError) as e:
                    raise e

                if not user.is_superuser:
                    user.make_action('add-hubanswer')
                    return self.json_success_context()
            else:
                return self.json_error_context(form.errors.items())
        else:
            return self.json_form_error_context(
                _(u'Вы не можете добавлять новые ответы так часто. Попробуйте позже!')
            )

        return self.json_success_context()


class HubQuestionAddView(JSONResponseMixin, TemplateView):
    """
        Post question
    """
    def _get(self, *args, **kwargs):
        return self.json_forbidden_context(_(u'Ошибка!'))

    @method_decorator(login_required)
    def _post(self, request, city_name):
        city = get_object_or_404(City, name=city_name)
        data = request.POST.copy()

        if request.user.can_action('add-hubquestion'):
            form = HubQuestionAddForm(data)
            user = self.request.user
            if form.is_valid():
                question = form.save(commit=False)
                question.city = city
                question.user = user
                try:
                    question.save()
                except (DatabaseError, IntegrityError) as e:
                    raise e

                if not user.is_superuser:
                    user.make_action('add-hubquestion')

                return self.json_success_context({
                    'redirect_url': question.get_absolute_url()
                })
            else:
                return self.json_error_context(form.errors.items())
        else:
            return self.json_form_error_context(
                _(u'Вы не можете добавлять новые вопросы так часто. Попробуйте позже!')
            )

