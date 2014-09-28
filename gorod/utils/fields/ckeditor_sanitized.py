"""
    Secure version of django ckeditor field.
    Allows to validate allowed html tags
"""

from django.db import models
from django import forms

import ckeditor.fields


class RichTextField(ckeditor.fields.RichTextField):
    def formfield(self, **kwargs):
        defaults = {
            'form_class': RichTextFormField,
            'config_name': self.config_name,
        }
        defaults.update(kwargs)
        return super(RichTextField, self).formfield(**defaults)


class RichTextFormField(ckeditor.fields.RichTextFormField):
    def __init__(self, config_name='default', *args, **kwargs):
        kwargs.update({'widget': CKEditorWidget(config_name=config_name)})
        super(RichTextFormField, self).__init__(*args, **kwargs)


try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^gorod\.utils\.fields\.ckeditor_secure.\RichTextField"])
except:
    pass
