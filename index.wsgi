# -*- coding: utf-8 -*-

import os, sys, site

activate_this = '/home/g/gorodin/.venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
site.addsitedir('/home/g/gorodin/.venv/lib/python2.7/site-packages')
sys.path.insert(1,'/home/g/gorodin/gorod.in/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'gorod_io.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

