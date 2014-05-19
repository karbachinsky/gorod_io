"""
    Gorod validators
"""

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

class DayScheduleValidator(object):
    """
        Checks whether DaySchedule is valid
    """
    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, value):
        """
            Validates that the input matches the regular expression.
        """
        assert False, value
        if isinstance(value, DaySchedule):
            return value.validate()
        else:
            raise ValidationError("Not a DaySchedule object!")
