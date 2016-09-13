# django-simple-domain #

Make setting and use of the Django Site Framework easier.

By simply add a host name in the settings of your Django project, django-simple-domain will ensure that an instance of Site corresponding to your host name has been created at launch. It also will ensure that the Django Site Framework always give you the Site instance corresponding to your domain name.

The purpose of that application is to facilitate the deployment of a project on many environments. It makes possible to specify a specific host name for each settings file (local, dev, production, etc...) and to not worry about forgot to update the Site model from the admin.

## Features ##

* Automatic creation of a Site model instance based on a domain name from your settings
* Ensuring that the Django Site Framework will ALWAYS returns to you the appropriate instance of Site based on the defined domain name.
* It won't delete any previous instance of Site

## How to setup? ##

First, add the application and the middleware to your application. Don't forget to enable 'django.contrib.sites'!

```
# settings.py
INSTALLED_APPS = (
    ...
    'django.contrib.sites',
    'django_simple_domain',
    ...
)

MIDDLEWARE_CLASSES = (
    ...
    'django_simple_domain.middleware.SetDynamicSitesMiddleware',
    ...
)
```

Then, specify the desired domain name (**SIMPLE_DOMAIN_NAME**) and ensure that **SITE_ID** is initialized as an instance of **django_simple_domain.site_id_local.SiteID**:

```
# settings.py
from django_simple_domain.site_id_local import SiteID

# Your domain name according to your development environment
SIMPLE_DOMAIN_NAME = "localhost:8080"

# Dynamic and thread safe SITE_ID
SITE_ID = SiteID()
```

That's it! If your settings are correct, an instance of Site with the specified SIMPLE_DOMAIN_NAME will be created during the startup of your project and the correct instance of Site will be returned by the Django Site Framework.

You are able to test it by executing the following python code in the console:
```
>>> from django.contrib.sites.models import Site
>>> current_site = Site.objects.get_current()
>>> current_site.domain
u'localhost:8080'
```

## Disabling the application ##

You can disable the application by setting the property **SIMPLE_DOMAIN_ENABLED** to False. The default value for **SIMPLE_DOMAIN_ENABLED** is True.

For example, if you want to disable the app during unit tests:

```
# settings.py
import sys

if 'test' not in sys.argv and 'jenkins' not in sys.argv:
    SIMPLE_DOMAIN_ENABLED = False
```

## Unit tests ##

You can run unit tests with the following command:

```
python manage.py test django_simple_domain
```

## Resources ##
Some parts of that module (the **SiteID** class and the **Middleware** class used for thread safe access to SITE_ID) come from that excellent django snippet from [jhg](https://djangosnippets.org/users/jhg/):
[Dynamic SITE_ID thread-safe](https://djangosnippets.org/snippets/3041/).

## TODO ##
* The code creating the Site instance during startup is located in the AppConfig of the module. But according to the Django documentation it is not a proper way to do. Find a better way to accomplish that?
* Tests on previous django version (currently tested on 1.8), add more unit tests.
* Find a way to use django cache for the middleware?

