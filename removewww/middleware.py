from __future__ import unicode_literals

from django.conf import settings
from django.http import HttpResponsePermanentRedirect

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object


class RemoveWwwMiddleware(MiddlewareMixin):
    """
    Middleware that inspects the request's host and path and
    checks the ``REMOVE_WWW`` setting and the beginning of the
    URL path. If has www, redirects without www and full path
    """
    def process_request(self, request):
        if settings.PREPEND_WWW is True:
            return None
        else:
            remove_www = getattr(settings, 'REMOVE_WWW', False)
            host = request.get_host()
            if remove_www and host and host.startswith('www.'):
                redirect_url = request.build_absolute_uri().replace('//www.', '//')
                return HttpResponsePermanentRedirect(redirect_url)

    def process_response(self, request, response):
        return response
