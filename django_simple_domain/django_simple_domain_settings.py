from django.conf import settings

__author__ = 'Jisson | pierre@jisson.com'

DOMAIN_NAME = getattr(settings, 'SIMPLE_SITES_DOMAIN_NAME', 'example.com')
ENABLED = getattr(settings, 'SIMPLE_SITES_ENABLED', True)

# Retrieving SITE_ID from global settings
SITE_ID = getattr(settings, 'SITE_ID', None)


# TODO: Check if that method is really use full
def set_site_id(site_id):
    """
    Accessor to simplify attribution of new values to SITE_ID directly from 'django_simple_domain_settings'.

    :param  site_id:    The new value to assign to SITE_ID property
    :type   site_id:    int
    """
    settings.SITE_ID._set(site_id)

