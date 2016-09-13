import logging
import sys

from django.apps import AppConfig
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import ugettext_lazy as _

import django_simple_domain.django_simple_domain_settings as simple_site_settings
from django_simple_domain import services

__author__ = 'Jisson | pierre@jisson.com'


std_logger = logging.getLogger(__name__)


class DjangoSimpleSiteConfig(AppConfig):
    """
    AppConfig for django_simple_domain application. Will perform check on settings at django startup and will
    create a new Site model according to specified DOMAIN_NAME from settings.
    """

    name = 'django_simple_domain'
    verbose_name = _('Django Simple Sites')

    @staticmethod
    def _check_settings():
        """
        Perform check on settings. Checks are not performed during unit tests.
        """

        # Disabling AppConfig during unit tests
        if 'test' not in sys.argv and 'jenkins' not in sys.argv:
            # Checking INSTALLED_APPS setting
            services.check_installed_apps_setting()
            # Checking SITE_ID setting
            services.check_site_id_setting(simple_site_settings.SITE_ID)

    def ready(self):
        """
        During application startup, that method will ensure that Site model corresponding to given DOMAIN_NAME has
        been created and then assign the appropriate id to SITE_ID in settings.
        """

        # TODO: Apps are not supposed to write in the database from AppConfig. Is there a better approach?

        # Not performing anything if the application has been disabled
        if simple_site_settings.ENABLED:
            std_logger.info("Loading AppConfig for django_simple_settings...")

            try:
                # Checking settings...
                self._check_settings()
                # Retrieving or creating the Site model corresponding to defined DOMAIN_NAME in settings
                current_site = services.get_or_create_sites(simple_site_settings.DOMAIN_NAME)
                # Attributing the correct value to SITE_ID
                simple_site_settings.settings.SITE_ID._set(int(current_site.id))
            except ImproperlyConfigured as e:
                raise e
        else:
            std_logger.info("Not loading AppConfig because of unit test mode")
