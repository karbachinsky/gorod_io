"""
    Gorod exceptions
    All these classes must be inherited from base Error class.

    Authors: I. Karbachinsky <karbachinsky@corp.mail.ru>
"""


class Error(Exception):
    """
        Base class for all SQ exceptions
    """
    pass


class FeedError(Error):
    """
        Errors associated with feed
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)