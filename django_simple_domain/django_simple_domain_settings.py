from django.conf import settings

__author__ = 'Jisson | pierre@jisson.com'

DOMAIN_NAME = getattr(settings, 'SIMPLE_DOMAIN_NAME', 'example.com')
ENABLED = getattr(settings, 'SIMPLE_DOMAIN_ENABLED', True)

# Define the the list commands in connection with which django-simple-domain should be deactivated
_commands = ['migrate', 'makemigrations']
DEACTIVATING_COMMANDS = getattr(settings, 'SIMPLE_DOMAIN_DEACTIVATING_COMMANDS', _commands)

# Retrieving SITE_ID from global settings
SITE_ID = getattr(settings, 'SITE_ID', None)
