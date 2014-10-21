"""
    Plate with random organizations, questions and welcome banner.
    Author: I. Karbachinsky
"""

from gorod.models import Organization, HubQuestion, Payment


class AdStartPlate(object):
    def __init__(self, city_name):
        self.organizations = Organization.objects.filter(city__name=city_name).order_by('?')[0:8]
        self.questions = HubQuestion.objects.filter(city__name=city_name).select_related().order_by('?')[0:4]
        self.payments = Payment.objects.filter(city__name=city_name).order_by('?')[0:8]

    def get_context(self):
        """
            Return dict with necessary data to frontend.
        """

        if len(self.payments) > 3: 
            self.organizations = self.organizations[0:4]
        else:
            self.payments = []

        return {
            'organizations': self.organizations,
            'questions': self.questions,
            'payments': self.payments
        }
