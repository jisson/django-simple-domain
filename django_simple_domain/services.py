import logging

from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _
from django.apps import apps
from django.core.exceptions import ImproperlyConfigured, FieldError, ValidationError

from django_simple_domain.site_id_local import SiteID

__author__ = 'Jisson | pierre@jisson.com'

std_logger = logging.getLogger(__name__)


def get_or_create_sites(domain_name):
    """
    Retrieve or create a Site entity based on given domain_name.

    :param  domain_name:    The domain name to look for. That property should come from user settings
    :type   domain_name:    str

    :return:    A Site entity if found
    :raise      ImproperlyConfigured
    """

    try:
        site = Site.objects.get(domain=domain_name)
    except Site.DoesNotExist:
        site = Site(domain=domain_name, name=_("Created with django_simple_domain"))
        site.save()
    except Site.MultipleObjectsReturned:
        raise ImproperlyConfigured("Multiple site object returned for defined SIMPLE_SITES_DOMAIN_NAME. "
                                   "Please verify sites models in your database.")
    except (FieldError, ValidationError) as e:
        std_logger.error(e)
        raise ImproperlyConfigured("Can't create Site model with given SIMPLE_SITES_DOMAIN_NAME. "
                                   "Please ensure that the provided domain name is correctly formatted.")
    return site


def check_installed_apps_setting():
    """
    Check if INSTALLED_APPS contains 'django.contrib.sites' which is required to run 'django_simple_domain'.

    :raise  ImproperlyConfigured:   if 'django.contrib.sites' not in INSTALLED_APPS
    """

    if not apps.is_installed('django.contrib.sites'):
        error_message = _("django.contrib.sites must be added to INSTALLED_APPS to use django_simple_domain")
        raise ImproperlyConfigured(error_message)


def check_site_id_setting(site_id):
    """
    Check if SITE_ID was correctly defined by verifying if it is an instance of
    'django_simple_domain.site_id_local.SiteId'.

    :param  site_id:            Define the setting to use for the django site framework
    :type   site_id:            django_simple_domain.site_id_local.SiteId

    :raise  ImproperlyConfigured:   if SITE_ID was not correctly defined in global settings
    """

    if site_id is None or not isinstance(site_id, SiteID):
        error_message = _("SITE_ID is invalid. Please verify that SITE_ID is an instance of type "
                          "'django_simple_domain.site_id_local.SiteId'")
        raise ImproperlyConfigured(error_message)
