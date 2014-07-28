from django.shortcuts import render, get_object_or_404, Http404, HttpResponse
from django.db import IntegrityError, DatabaseError
from django.views.generic import View

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from gorod.models import City, Complaint
from gorod.utils.forms.complaint import ComplaintAddForm

import json


class ComplaintAddView(View):
    """
        Add complaint
    """

    @method_decorator(login_required)
    def dispatch(self, request):
        if request.method == 'POST':
            return self._save_complaint(request)
        else:
            # Show form
            form = ComplaintAddForm()
            return render(request, 'gorod/forms/complaint_add.html', {
                'form': form,
            })

    @staticmethod
    def _save_complaint(request):
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

            json_response = dict(success=True)
        else:
            json_response = dict(success=False, errors=form.errors.items())

        return HttpResponse(json.dumps(json_response), content_type='application/json')