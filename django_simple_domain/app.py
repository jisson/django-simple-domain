import logging
import sys

from django.apps import AppConfig
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import ugettext_lazy as _

import utils as simple_site_utils

__author__ = 'Jisson | pierre@jisson.com'


std_logger = logging.getLogger(__name__)


class DjangoSimpleSiteConfig(AppConfig):
    """
    AppConfig for django_simple_domain application. Will perform check on settings at django startup and will
    create a new Site model according to specified DOMAIN_NAME from settings.
    """

    name = 'django_simple_domain'
    verbose_name = _('Django Simple Domain')     # TODO: Make translation files

    # App services and settings
    simple_domain_services = None
    simple_domain_settings = None

    def _check_settings(self):
        """
        Perform check on settings. Checks are not performed during unit tests.
        """

        try:
            # Disabling AppConfig during unit tests
            # TODO: Create command list specific to settings?
            if 'test' not in sys.argv and 'jenkins' not in sys.argv:
                # Checking INSTALLED_APPS setting
                self.simple_domain_services.check_installed_apps_setting()
                # Checking SITE_ID setting
                self.simple_domain_services.check_site_id_setting(self.simple_domain_settings.SITE_ID)
        except AttributeError as e:
            std_logger.error("Can't access app settings or services")

    def _get_enabled(self):
        """
        Check if one of the commands given in sys.argv is should deactivate django-simple-domain or if
        SIMPLE_DOMAIN_ENABLED is False.

        :return:    True will be returned if there is no command related to DEACTIVATING_COMMANDS in sys.argv and
        if SIMPLE_DOMAIN_ENABLED is True
        """
        try:
            std_logger.info("Checking if module should be enabled...")
            return self.simple_domain_settings.ENABLED and not simple_site_utils.is_item_in_list_a_in_list_b(
                self.simple_domain_settings.DEACTIVATING_COMMANDS, sys.argv
            )
        except AttributeError as e:
            std_logger.error("Can't access app settings or services")

    def ready(self):
        """
        During application startup, that method will ensure that Site model corresponding to given DOMAIN_NAME has
        been created and then assign the appropriate id to SITE_ID in settings.
        """

        # TODO: Apps are not supposed to write in the database from AppConfig. Is there a better approach?

        # Importing services in ready method to ensure apps have been loaded
        from django_simple_domain import services as simple_domain_services
        self.simple_domain_services = simple_domain_services
        import django_simple_domain.django_simple_domain_settings as simple_domain_settings
        self.simple_domain_settings = simple_domain_settings

        try:
            # Not performing anything if the application has been disabled
            if self._get_enabled():
                std_logger.info("Loading AppConfig for django_simple_settings...")

                try:
                    # Checking settings...
                    self._check_settings()
                    # Retrieving or creating the Site model corresponding to defined DOMAIN_NAME in settings
                    current_site = self.simple_domain_services.get_or_create_sites(
                        self.simple_domain_settings.DOMAIN_NAME
                    )
                    # Attributing the correct value to SITE_ID
                    self.simple_domain_settings.settings.SITE_ID._set(int(current_site.id))
                except ImproperlyConfigured as e:
                    raise e
            else:
                std_logger.info("Not loading AppConfig. Module is not enabled or a command given to sys.argv is in "
                                "SIMPLE_DOMAIN_DEACTIVATING_COMMANDS.")
        except AttributeError as e:
            std_logger.error(e.message)
