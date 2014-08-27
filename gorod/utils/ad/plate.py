"""
    Plate with random organizations, questions and welcome banner.
    Author: I. Karbachinsky
"""

from gorod.models import Organization, HubQuestion


class AdStartPlate(object):
    def __init__(self):
        self.organizations = Organization.objects.order_by('?')[0:8]
        self.questions = HubQuestion.objects.order_by('?')[0:4]

    def get_context(self):
        """
            Return dict with necessary data to frontend.
        """
        return {
            'organizations': self.organizations,
            'questions': self.questions
        }
