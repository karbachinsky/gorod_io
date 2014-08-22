"""
    Plate with random organizations, questions and welcome banner.
    Author: I. Karbachinsky
"""

from gorod.models import Organization, HubQuestion, CityWelcome


class AdStartPlate(object):
    def __init__(self):
        self.organizations = Organization.objects.all()
        self.questions = HubQuestion.objects.all()

    def get_context(self):
        """
            Return dict with necessary data to frontend.
        """
        return {
            'organizations': self.organizations,
            'questions': self.questions
        }
