from django.core.exceptions import ImproperlyConfigured
from django.test import TestCase

from django_simple_domain import services

__author__ = 'Jisson | pierre@jisson.com'


class CheckInstalledAppsTestCase(TestCase):

    def test_check_site_framework_disabled(self):

        # Disabling django site framework
        installed_apps = (
            # Base django apps
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',

            # Application
            'django_simple_domain',
        )

        with self.settings(INSTALLED_APPS=installed_apps):
            with self.assertRaises(ImproperlyConfigured):
                services.check_installed_apps_setting()

    def test_check_site_framework_enabled(self):

        # Enabling django site framework
        installed_apps = (
            # Base django apps
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',

            # Django site Framework
            'django.contrib.sites',

            # Application
            'django_simple_domain',
        )

        with self.settings(INSTALLED_APPS=installed_apps):
            services.check_installed_apps_setting()
