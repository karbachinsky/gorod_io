# -*- coding: utf-8 -*-

from django.test import TestCase
from gorod.templatetags.stringutils import smart_truncate


class StringUtilsTestCase(TestCase):
    def setUp(self):
        pass

    def test_smart_truncate(self):
        """
            smart_truncate
        """
        text = 'Test. Test'

        self.assertEqual(smart_truncate(text, 20), text)

        self.assertEqual(smart_truncate(text, 2), 'Te...')

        self.assertEqual(smart_truncate(text, 4), 'Test...')

        self.assertEqual(smart_truncate(text, 5), 'Test.')

        self.assertEqual(smart_truncate(text, 6), 'Test....')

        # Unicode
        text = u'Привет.'
        self.assertEqual(smart_truncate(text, 4), u'Прив...')

        self.assertEqual(smart_truncate(text, 7), u'Привет.')
