"""
    Mixins for Django class-based views.
"""

from django import http

import json as json


class JSONResponseMixin(object):
    status_code = 200

    def get(self, *args, **kwargs):
        context_dict = self._get(*args, **kwargs)
        return self._get_json_response(self._convert_context_to_json(context_dict))

    def post(self, *args, **kwargs):
        context_dict = self._post(*args, **kwargs)
        return self._get_json_response(self._convert_context_to_json(context_dict))

    def _get_json_response(self, content, **httpresponse_kwargs):
        """
            Construct an `HttpResponse` object.
        """
        return http.HttpResponse(content, content_type='application/json', status=self.status_code, **httpresponse_kwargs)

    @staticmethod
    def _convert_context_to_json(context):
        """
            Convert the context dictionary into a JSON object.
        """
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return json.dumps(context)

    def json_error_context(self, msg):
        """
            Prepare and response context for json error.
        """
        self.status_code = 500
        return {'error': msg}

    def json_form_error_context(self, msg, type='internal'):
        """
            Prepare and response context for json error after form validation.
        """
        # FIXME: check if type is valid
        self.status_code = 500
        return {'error': [[type, [msg]]]}

    def json_forbidden_context(self, msg):
        """
            Prepare and response context for json forbidden.
        """
        self.status_code = 403
        return {'error': msg}

    def json_success_context(self, msg=None):
        """
            Prepare and response context for json success.
        """
        context = {'success': True}
        if msg:
            if isinstance(msg, dict):
                context.update(msg)
            elif isinstance(msg, basestring):
                context['message'] = msg
            else:
                raise TypeError('Undefined type of message passed. Must be string or tuple!')

        return context