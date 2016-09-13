from django.contrib.sites.models import Site
from django.core.exceptions import ImproperlyConfigured
from django.test import TestCase

from django_simple_domain import services


__author__ = 'Jisson | pierre@jisson.com'


class GetOrCreateSitesTestCase(TestCase):

    default_domain_name = "example.com"
    default_site_id = None

    def setUp(self):

        try:
            site = Site.objects.get(domain=self.default_domain_name)
        except Site.DoesNotExist:
            site = Site(domain=self.default_domain_name, name=self.default_domain_name)
            site.save()

        self.default_site_id = site.id

    def test_default_domain_name(self):

        site = services.get_or_create_sites(self.default_domain_name)
        self.assertEqual(site.id, self.default_site_id)
        self.assertEqual(site.domain, self.default_domain_name)

    def test_new_domain_names(self):

        domain_name_2 = "domain_name_2.com"
        domain_name_3 = "domain_name_3.com"

        site = services.get_or_create_sites(domain_name_2)
        self.assertEqual(site.domain, domain_name_2)
        domain_name_2_id = site.id
        site = services.get_or_create_sites(domain_name_2)
        self.assertEqual(site.id, domain_name_2_id)

        site = services.get_or_create_sites(domain_name_3)
        self.assertEqual(site.domain, domain_name_3)
        domain_name_3_id = site.id
        site = services.get_or_create_sites(domain_name_3)
        self.assertEqual(site.id, domain_name_3_id)

    def test_multiple_objects_returned(self):

        site = Site(domain=self.default_domain_name, name=self.default_domain_name)
        site.save()

        with self.assertRaises(ImproperlyConfigured):
            services.get_or_create_sites(self.default_domain_name)
