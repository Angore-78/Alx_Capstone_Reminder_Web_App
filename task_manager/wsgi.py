"""
WSGI config for task_manager project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys

## assuming your django settings file is at '/home/Angore78/mysite/mysite/settings.py'
## and your manage.py is is at '/home/Angore78/mysite/manage.py'

path = '/home/Angore78/Alx_Capstone_Reminder_Web_App'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'task_manager.settings'

## then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

