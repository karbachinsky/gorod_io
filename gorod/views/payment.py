from django.shortcuts import render
from django.views.generic import View

from gorod.models import City, Payment


class PaymentsView(View):
    """
        City payments list page.
    """
    def dispatch(self, request, city_name):
        payments = Payment.objects.filter(city__name=city_name)

        context = dict(
            payments=payments
        )

        return render(request, 'gorod/payments.html', context)

