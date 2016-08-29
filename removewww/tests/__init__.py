from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.test import RequestFactory, TestCase, override_settings

from ..middleware import RemoveWwwMiddleware


class RemoveWwwMiddlewareTestCase(TestCase):

    def setUp(self):
        self.rf = RequestFactory()

    def get_path(self, secure=False, host='', path='', params={}):
        return self.rf.get(path, params, secure=secure, SERVER_NAME=host)

    @override_settings(PREPEND_WWW=True)
    def test_request_url_of_prepend_examplecom(self):
        """
        Return None if PREPEND_WWW is True
        """
        host = 'example.com'
        path = '/admin/login/'
        params = {'next': 'admin'}
        request = self.get_path(host=host, path=path, params=params)
        r = RemoveWwwMiddleware().process_request(request)
        self.assertIsNone(r)

    @override_settings(REMOVE_WWW=True)
    def test_request_url_of_remove_examplecom(self):
        """
        Return None if host has no ``www``
        """
        host = 'example.com'
        path = '/admin/login/'
        params = {'next': 'admin'}
        request = self.get_path(host=host, path=path, params=params)
        r = RemoveWwwMiddleware().process_request(request)
        self.assertIsNone(r)

    @override_settings(PREPEND_WWW=True, REMOVE_WWW=True)
    def test_request_url_of_prepend_remove_examplecom(self):
        """
        Return None if PREPEND_WWW is True and REMOVE_WWW is True
        """
        host = 'example.com'
        path = '/admin/login/'
        params = {'next': 'admin'}
        request = self.get_path(host=host, path=path, params=params)
        r = RemoveWwwMiddleware().process_request(request)
        self.assertIsNone(r)

    @override_settings(PREPEND_WWW=True)
    def test_request_url_of_prepend_wwwexamplecom(self):
        """
        Return None if PREPEND_WWW is True
        """
        host = 'www.example.com'
        path = '/admin/login/'
        params = {'next': 'admin'}
        request = self.get_path(host=host, path=path, params=params)
        r = RemoveWwwMiddleware().process_request(request)
        self.assertIsNone(r)

    @override_settings(REMOVE_WWW=True)
    def test_request_url_of_remove_wwwexamplecom(self):
        """
        Return new URL if REMOVE_WWW is True and host has ``www``
        """
        host = 'www.example.com'
        path = '/admin/login/'
        params = {'next': 'admin'}
        request = self.get_path(host=host, path=path, params=params)
        r = RemoveWwwMiddleware().process_request(request)
        self.assertEqual(r.url, 'http://example.com/admin/login/?next=admin')

    @override_settings(PREPEND_WWW=True, REMOVE_WWW=True)
    def test_request_url_of_prepend_remove_wwwexamplecom(self):
        """
        Return None if PREPEND_WWW is True and REMOVE_WWW is True
        """
        host = 'www.example.com'
        path = '/admin/login/'
        params = {'next': 'admin'}
        request = self.get_path(host=host, path=path, params=params)
        r = RemoveWwwMiddleware().process_request(request)
        self.assertIsNone(r)

    @override_settings(REMOVE_WWW=True)
    def test_request_url_of_remove_httpwwwexamplecom(self):
        """
        Return new URL if REMOVE_WWW is True and host has ``www``,
        despite ``http://`` or ``https://``
        """
        secure = False
        host = 'www.example.com'
        path = '/admin/login/'
        params = {'next': 'admin'}
        request = self.get_path(secure=secure, host=host, path=path, params=params)
        r = RemoveWwwMiddleware().process_request(request)
        self.assertEqual(r.url, 'http://example.com/admin/login/?next=admin')

    @override_settings(REMOVE_WWW=True)
    def test_request_url_of_remove_httpswwwexamplecom(self):
        """
        Assert new URL if REMOVE_WWW is True and host has ``www``,
        despite ``http://`` or ``https://``
        """
        secure = True
        host = 'www.example.com'
        path = '/admin/login/'
        params = {'next': 'admin'}
        request = self.get_path(secure=secure, host=host, path=path, params=params)
        r = RemoveWwwMiddleware().process_request(request)
        self.assertEqual(r.url, 'https://example.com/admin/login/?next=admin')

    @override_settings(REMOVE_WWW=True)
    def test_response_of_examplecom(self):
        """
        Assert response is instance of HttpResponse and status code 200
        """
        host = 'example.com'
        path = '/admin/login/'
        params = {'next': 'admin'}
        request = self.get_path(host=host)
        response = HttpResponse("Here's the text of the Web page.")
        r = RemoveWwwMiddleware().process_response(request, response)
        self.assertEqual(r, response)
        self.assertEqual(r.status_code, 200)

    @override_settings(REMOVE_WWW=True)
    def test_response_of_wwwexamplecom(self):
        """
        Assert response is instance of HttpResponse and status code 301
        """
        host = 'www.example.com'
        path = '/admin/login/'
        params = {'next': 'admin'}
        request = self.get_path(host=host, path=path, params=params)
        response = HttpResponsePermanentRedirect
        r = RemoveWwwMiddleware().process_response(request, response)
        self.assertEqual(r, response)
        self.assertEqual(r.status_code, 301)
