"""
WSGI config for my_timetable project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_timetable.settings')

application = get_wsgi_application() 