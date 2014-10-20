"""
    Gorod exceptions
    All these classes must be inherited from base Error class.

    Authors: I. Karbachinsky <karbachinsky@corp.mail.ru>
"""


class Error(Exception):
    """
        Base class for all Gorod exceptions
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class FeedError(Error):
    """
        Errors associated with feed
    """
    pass


class ComplaintError(Error):
    """
        Errors associated with complaints
    """
    pass


class DONCError(Error):
    """
        Errors associated with Depending Object Numbers Counter
    """
    pass