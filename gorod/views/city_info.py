from django.shortcuts import render, get_object_or_404

from django.views.generic import View

from gorod.models import CityInfo, CityInfoQuestion


class CityInfoView(View):
    """
        City info/about.
    """
    def dispatch(self, request, city_name):
        info = get_object_or_404(CityInfo, city__name=city_name)

        questions = CityInfoQuestion.objects.filter(cityinfo=info)

        context = {
            'info': info,
            'questions': questions
        }

        return render(request, 'gorod/city_info.html', context)


class CityInfoQuestionView(View):
    """
        City info one question page
    """
    def dispatch(self, request, city_name, question_id):
        question = get_object_or_404(CityInfoQuestion, cityinfo__city__name=city_name, id=question_id)

        # Other questions
        questions = CityInfoQuestion.objects.filter(cityinfo=question.cityinfo)

        context = {
            'question': question,
            'other_questions': questions
        }

        return render(request, 'gorod/city_info_question.html', context)
