from django.shortcuts import render, get_object_or_404

from django.views.generic import View

from gorod.models import HubQuestion, HubAnswer
from gorod.utils.forms.hub_answer import HubAnswerAddForm


class HubView(View):
    """
        City list of hub questions
    """
    def dispatch(self, request, city_name):
        questions = HubQuestion.objects.get_questions_by_city_name(city_name)

        context = {
            'questions': questions
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
