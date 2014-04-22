""" Working time Django custom field """

from django.db import models
from django.forms import widgets

from south.modelsinspector import add_introspection_rules

import pickle
import logging

add_introspection_rules([], ["^gorod\.fields\.schedule\.ScheduleField"])
add_introspection_rules([], ["^gorod\.fields\.schedule\.DayScheduleField"])


class DayScheduleWidget(widgets.MultiWidget):
    """ Widget for Day Schedule Field """
    def __init__(self, attrs=None):
        _input_attrs = {"size": 5, "placeholder": "9:00"}
        _widgets = (
            widgets.TextInput(attrs=_input_attrs),
            widgets.TextInput(attrs=_input_attrs)
        )
        super(DayScheduleWidget, self).__init__(_widgets, attrs)

    def render(self, name, value, attrs=None):
        return super(DayScheduleWidget, self).render(name, value, attrs) 

    def decompress(self, value):
        if value and isinstance(value, DaySchedule):
            return value.as_list()
        return [None, None]

    def format_output(self, rendered_widgets):
        return u' - '.join(rendered_widgets)

    def value_from_datadict(self, data, files, name):
        # FIXME
        return DaySchedule(data[name + '_0'], data[name + '_1'])



class DaySchedule(object):
    """ One day schedule """
    def __init__(self, time_from=None, time_to=None, day_name=None):
        #if day_name is None:
        #raise Exception('Specify name for Dayschedule!')
        
        self.time_from = time_from
        self.time_to = time_to    
        self.day_name = day_name

    def as_list(self):
        return [self.time_from, self.time_to]

    def __unicode__(self):
        return ','.join(map( lambda(x): str(x), self.as_list() ))

    def __str__(self):
        return unicode(self).encode('utf-8')


class DayScheduleField(models.Field):
    description = "One day schedule field type for django"

    __metaclass__ = models.SubfieldBase

    def db_type(self, connection):
        # FIXME: Support all db types
        return 'MEDIUMBLOB'

    def __init__(self, *args, **kwargs):
        super(DayScheduleField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            return DaySchedule()
        elif isinstance(value, DaySchedule):
            return value
        else:
            #assert False, value
            schedule_times = value.split(',')
            return DaySchedule(*schedule_times)
    
    def get_prep_value(self, value):
        if isinstance(value, DaySchedule):
            return value

        return value
        
    def formfield(self, **kwargs):
        defaults = {'widget': DayScheduleWidget}
        defaults.update(kwargs)
        return super(DayScheduleField, self).formfield(**defaults)


