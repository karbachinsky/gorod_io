import logging


class RequestExceptionMiddleware(object):
    """
        Log any exceptions that happen in a view.
    """
    logger = logging.getLogger('exceptions')

    def process_exception(self, request, exception):
        self.logger.exception('Got view exception!')

        return None