Django Remove WWW
*********************

|PyPI version|_ |Build status|_

.. |PyPI version| image::
   https://badge.fury.io/py/django-removewww.svg
.. _PyPI version: https://pypi.python.org/pypi/django-removewww

.. |Build status| image::
   https://travis-ci.org/richardcornish/django-removewww.svg?branch=master
.. _Build status: https://travis-ci.org/richardcornish/django-removewww

**Django Remove WWW** is a `Django <https://www.djangoproject.com/>`_ `middleware <https://docs.djangoproject.com/en/1.11/topics/http/middleware/>`_ application that removes the WWW subdomain.

The middleware inspects the request's host for the ``www`` subdomain, and redirects if ``REMOVE_WWW`` is ``True``. It silently passes if |prepend_www|_ is also ``True``. For some reason, Django `won't include <https://code.djangoproject.com/ticket/6342>`_ a ``REMOVE_WWW`` setting. Thanks to Daniel Ryan's `GitHub Gist <https://gist.github.com/dryan/290771>`_ for some inspiration.

.. |prepend_www| replace:: ``PREPEND_WWW``
.. _prepend_www: https://docs.djangoproject.com/en/1.11/ref/settings/#prepend-www

* `Package distribution <https://pypi.python.org/pypi/django-removewww>`_
* `Code repository <https://github.com/richardcornish/django-removewww>`_
* `Documentation <https://django-removewww.readthedocs.io/>`_
* `Tests <https://travis-ci.org/richardcornish/django-removewww>`_

Install
=======

.. code-block:: bash

   $ pip install django-removewww

Add to ``settings.py``.

.. code-block:: python

   MIDDLEWARE = [
       # ...
       'removewww.middleware.RemoveWwwMiddleware',
   ]

   REMOVE_WWW = True

Adding to ``INSTALLED_APPS`` is unnecessary unless you want to run the tests.
