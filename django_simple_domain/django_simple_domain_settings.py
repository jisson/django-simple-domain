from django.conf import settings

__author__ = 'Jisson | pierre@jisson.com'

DOMAIN_NAME = getattr(settings, 'SIMPLE_DOMAIN_NAME', 'example.com')
ENABLED = getattr(settings, 'SIMPLE_DOMAIN_ENABLED', True)

# Define the the list commands in connection with which django-simple-domain should be deactivated
_commands = ['migrate', 'makemigrations']
DEACTIVATING_COMMANDS = getattr(settings, 'SIMPLE_DOMAIN_DEACTIVATING_COMMANDS', _commands)

# Retrieving SITE_ID from global settings
SITE_ID = getattr(settings, 'SITE_ID', None)


# TODO: Check if that method is really use full. TODO: Seems to be not used finally
# def set_site_id(site_id):
#     """
#     Accessor to simplify attribution of new values to SITE_ID directly from 'django_simple_domain_settings'.
#
#     :param  site_id:    The new value to assign to SITE_ID property
#     :type   site_id:    int
#     """
#     settings.SITE_ID._set(site_id)
