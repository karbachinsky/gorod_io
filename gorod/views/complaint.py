from django.shortcuts import render, HttpResponse
from django.db import IntegrityError, DatabaseError
from django.views.generic import View
from django.conf import settings

from gorod.models import Complaint
from gorod.utils.forms.complaint import ComplaintAddForm
from gorod.utils.exceptions import ComplaintError

import json


class ComplaintAddView(View):
    """
        Add complaint
    """
    MAIL_SUBJECT_PREFIX = "Complaint from"

    def dispatch(self, request):
        if request.method == 'POST':
            return self._save_complaint(request)
        else:
            # Show form
            form = ComplaintAddForm()
            return render(request, 'gorod/forms/complaint_add.html', {
                'form': form,
            })

    def _save_complaint(self,request):
        """
            Save complaint from POST data
        """
        form = ComplaintAddForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)

            try:
                complaint.save()
            except (DatabaseError, IntegrityError) as e:
                raise e

            self._send_complaint_form_to_mail(complaint)

            json_response = dict(success=True)
        else:
            json_response = dict(success=False, errors=form.errors.items())

        return HttpResponse(json.dumps(json_response), content_type='application/json')

    def _send_complaint_form_to_mail(self, complaint_form):
        """
            Sends complaint to managers
        """
        from django.core.mail import EmailMessage, BadHeaderError

        sender = complaint_form.email

        mail = EmailMessage(
            subject="%s %s" % (self.MAIL_SUBJECT_PREFIX, sender),
            body="%s\n\nReason: %s\nLocation:%s" % (
                complaint_form.comment,
                Complaint.COMPLAINT_TYPES[complaint_form.type][1],
                complaint_form.url
            ),
            from_email=sender,
            to=[manager[1] for manager in enumerate(settings.MANAGERS) if manager[0] % 2 == 1]
        )

        try:
            mail.send()
        except BadHeaderError as e:
            raise ComplaintError(e)
