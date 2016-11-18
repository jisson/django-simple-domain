from setuptools import setup

__author__ = 'Jisson | pierre@jisson.com'


setup(name='django-simple-domain',
      packages=['django_simple_domain'],
      version='0.5',
      url='https://github.com/jisson/django-simple-domain',
      download_url='https://github.com/jisson/django-simple-domain/tarball/0.5',
      license='Public',
      author='Jisson',
      author_email='pierre@jisson.fr',
      description='Simple domain name settings for Django site framework',
      setup_requires=[
      ],
      tests_require=[
          'django >=1.8',
      ],
      test_suite='django_simple_domain.tests',
      include_package_data=True,
      keywords=['site', 'domain', 'django'],
      classifiers=[
          'Framework :: Django',
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 2.7',
      ],
      )

