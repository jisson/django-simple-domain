from setuptools import setup

__author__ = 'Jisson | pierre@jisson.com'


setup(name='django-simple-domain',
      version='0.0.1',
      packages=['django_simple_domain'],
      # TODO: Github url
      license='Public',
      author='Jisson',
      author_email='pierre@jisson.com',
      description='Simple domain name settings for Django site framework',
      setup_requires=[
      ],
      tests_require=[
          'django >=1.8',
      ],
      test_suite='django_simple_domain.tests',
      include_package_data=True,
      classifiers=[
          'Framework :: Django',
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 2.7',
      ],
      )

