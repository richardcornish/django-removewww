from __future__ import unicode_literals

from django.conf import settings


REMOVE_WWW = getattr(settings, 'REMOVE_WWW', False)
