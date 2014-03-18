from django.core.exceptions import ValidationError

from django.core.validators import RegexValidator 

# TODO
def validate_list_of_phones(value):
    if value % 2 != 0:
        raise ValidationError(u'%s is not an even number' % value)
