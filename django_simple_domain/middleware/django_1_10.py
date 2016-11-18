# coding=utf-8
from django.contrib.sites.models import Site
from django_simple_domain import django_simple_domain_settings
from django.utils.deprecation import MiddlewareMixin

"""
According to Django 1.10 release notes, Middleware have been updated:

    '''
    Changed in Django 1.10:

    A new style of middleware was introduced for use with the new MIDDLEWARE setting.
    If you’re using the old MIDDLEWARE_CLASSES setting, you’ll need to adapt old, custom middleware
    before using the new setting. This document describes new-style middleware. Refer to this page in older versions
    of the documentation for a description of how old-style middleware works.

    @see: https://docs.djangoproject.com/en/1.10/topics/http/middleware/#upgrading-middleware
    '''

That python module provide middleware compatible with django 1.10
"""


__author__ = 'Jisson | pierre@jisson.com'


# TODO: Reformat middleware classes to handle compatibility issues
class SetDynamicSitesMiddleware(MiddlewareMixin):
    """
    That middleware change SITE_ID dynamically in a thread safe way.
    """

    @staticmethod
    def process_request(request):
        """
        Assign the correct value to the SITE_ID property, ensuring thread safe access to that value.
        """

        domain_name = django_simple_domain_settings.DOMAIN_NAME
        try:
            current_site = Site.objects.get(domain=domain_name)
            django_simple_domain_settings.settings.SITE_ID._set(int(current_site.id))
        except Site.DoesNotExist:
            # TODO: It should not happen
            django_simple_domain_settings.settings.SITE_ID._set(1)
        return None

