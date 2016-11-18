from django.contrib.sites.models import Site

from django_simple_domain import django_simple_domain_settings

__author__ = 'Jisson | pierre@jisson.com'


class SetDynamicSitesMiddleware(object):
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
