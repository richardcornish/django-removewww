.. _install:

Install
*******

Install with the `pip <https://pip.pypa.io/en/stable/>`_ package manager.

.. code-block:: bash

   $ mkvirtualenv myvenv -p python3
   $ pip install django
   $ pip install django-removewww

After `creating a project <https://docs.djangoproject.com/en/1.10/intro/tutorial01/>`_, add ``removewww.middleware.RemoveWwwMiddleware`` to ``MIDDLEWARE`` in ``settings.py``. Set the ``REMOVE_WWW`` boolean to ``True``.

.. code-block:: python

   MIDDLEWARE = [
       # ...
       'removewww.middleware.RemoveWwwMiddleware',
   ]

   REMOVE_WWW = True

The middleware is compatible with `pre-Django 1.10-style middleware <https://docs.djangoproject.com/en/1.10/topics/http/middleware/#upgrading-pre-django-1-10-style-middleware>`_ because it inherits from ``django.utils.deprecation.MiddlewareMixin``.

Remember to update your ``requirements.txt`` file. In your project directory:

.. code-block:: bash

   $ pip freeze > requirements.txt
