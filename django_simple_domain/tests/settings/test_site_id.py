from django.core.exceptions import ImproperlyConfigured
from django.test import TestCase

from django_simple_domain import services
from django_simple_domain.site_id_local import SiteID

__author__ = 'Jisson | pierre@jisson.com'


class SiteIdTestCase(TestCase):

    def test_no_site_id(self):

        with self.assertRaises(ImproperlyConfigured):
            services.check_site_id_setting(None)

    def test_correct_site_id(self):

        id_local = SiteID()
        with self.settings(SITE_ID=id_local):
            services.check_site_id_setting(id_local)

    def test_invalid_site_id(self):

        with self.assertRaises(ImproperlyConfigured):
            services.check_site_id_setting(1)
