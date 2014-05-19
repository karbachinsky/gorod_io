# coding=utf-8
""" Working time Django custom field """

# -*- coding: utf-8 -*-

from django.db import models
from django.forms import widgets
from south.modelsinspector import add_introspection_rules

add_introspection_rules([], ["^gorod\.fields\.schedule\.DayScheduleField"])

_days = [
    ('weekdays', u'Будние дни'),
    ('weekend', u'Выходные'),
    ('monday', u'Понедельник'),
    ('tuesday', u'Вторник'),
    ('wednesday', u'Среда'),
    ('thursday', u'Четверг'),
    ('friday', u'Пятница'),
    ('saturday', u'Суббота'),
    ('sunday', u'Воскресенье'),
]

class DayScheduleWidget(widgets.MultiWidget):
    """ Widget for Day Schedule Field """
    def __init__(self, attrs=None):
        _input_attrs = {"size": 5, "placeholder": "9:00"}
        _select_attrs = {}

        _widgets = (
            widgets.Select(attrs=_select_attrs, choices=_days),
            widgets.TextInput(attrs=_input_attrs),
            widgets.TextInput(attrs=_input_attrs)
        )
        super(DayScheduleWidget, self).__init__(_widgets, attrs)

    def render(self, name, value, attrs=None):
        return super(DayScheduleWidget, self).render(name, value, attrs) 

    def decompress(self, value):
        if value and isinstance(value, DaySchedule):
            return value.as_list()
        return [None, None, None]

    def format_output(self, rendered_widgets):
        return rendered_widgets[0] + ' ' + u' - '.join(rendered_widgets[1:])

    def value_from_datadict(self, data, files, name):
        # FIXME
        try:
            return DaySchedule(data[name + '_0'], data[name + '_1'], data[name + '_2'])
        except ValueError:
            return ''


class DaySchedule(object):
    """ One day schedule """
    def __init__(self, time_from=None, time_to=None, day_name=None):

        self.day_name = day_name
        self.time_from = time_from
        self.time_to = time_to

    def as_list(self):
        return [self.day_name, self.time_from, self.time_to]

    def __unicode__(self):
        is_empty = True
        for elem in self.as_list():
            if elem:
                is_empty = False
                break

        if is_empty:
            return ''
        else:
            return ','.join(map(lambda(x): str(x), self.as_list()))

    def __str__(self):
        return unicode(self).encode('utf-8')

    @property
    def day_name_rus(self):
        """
            Russian day name
        """
        try:
            return filter(lambda x: x[0] == self.day_name, _days)[0][1]
        except:
            return self.day_name




class DayScheduleField(models.Field):
    description = "One day schedule field type for django"

    __metaclass__ = models.SubfieldBase

    def db_type(self, connection):
        # FIXME: Support all db types
        return 'MEDIUMBLOB'

    def __init__(self, *args, **kwargs):
        super(DayScheduleField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if value is None:
            return DaySchedule()
        elif isinstance(value, DaySchedule):
            return value
        else:
            schedule_opts = value.split(',')
            return DaySchedule(*schedule_opts)
    
    def get_prep_value(self, value):
        if isinstance(value, DaySchedule):
            return value
        return None
        
    def formfield(self, **kwargs):
        defaults = {'widget': DayScheduleWidget}
        defaults.update(kwargs)
        return super(DayScheduleField, self).formfield(**defaults)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_prep_value(value)

